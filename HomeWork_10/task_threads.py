import itertools
import json
import re
from concurrent.futures import ThreadPoolExecutor
from heapq import nlargest, nsmallest
from typing import Dict, List

from bs4 import BeautifulSoup

import requests
from requests import Response


def get_paginator_pages_sp500(html: Response) -> List:
    paginator_pages = []
    content = BeautifulSoup(html.text, "html.parser")
    for i in content.find("div", class_="finando_paging").find_all("a"):
        paginator_pages.append(
            "https://markets.businessinsider.com/index/components/s&p_500" + i["href"]
        )
    return paginator_pages


def get_all_companies_from_page(html: Response) -> List[Dict]:
    companies = []
    content = BeautifulSoup(html.text, "html.parser")
    for company in content.find("main", class_="site-content").find_all(
        "a", {"href": re.compile("/stocks/\w*")}
    ):
        companies.append(
            {
                "company_url": "https://markets.businessinsider.com" + company["href"],
                "name": company["title"],
            }
        )
    for img, comp in zip(content.find_all("img"), companies):
        if re.match("https://pproxy.markets.businessinsider.com", img["src"]) != "":
            comp[
                "1_year_growth"
            ] = img.parent.previous_sibling.previous_sibling.contents[4].get_text()
    return companies


def get_info_from_company_url(company: Dict) -> Dict:
    html = requests.get(company["company_url"])
    bsObj = BeautifulSoup(html.text, "html.parser")
    company["name"] = (
        bsObj.find("h1", class_="price-section__identifiers")
        .find("span", class_="price-section__label")
        .get_text()
    )
    company["code"] = (
        bsObj.find("span", class_="price-section__category")
        .find("span")
        .get_text()
        .split(" ")[1]
        .replace(" ", "")
    )
    for tag_line in bsObj.find_all("div", class_="snapshot__header"):
        if tag_line.get_text() == "P/E Ratio":
            company["P/E"] = float(tag_line.previous_element.replace(",", ""))
            break
    search_price_and_weeks = re.split(
        "high52weeks: (.*),\s*low52weeks: (.*),\s*price: (.*),", html.text
    )[1:-1]
    high52weeks = float(search_price_and_weeks[0])
    low52weeks = float(search_price_and_weeks[1])
    company["price_in_USD"] = float(search_price_and_weeks[2])
    company["profit_52_weeks"] = (high52weeks - low52weeks) / low52weeks * 100
    return company


def get_usd_to_rub() -> float:
    return float(
        BeautifulSoup(
            requests.get("http://www.cbr.ru/scripts/XML_daily.asp?").text, "html.parser"
        )
        .find(id="R01235")
        .find("value")
        .get_text()
        .replace(",", ".")
    )


def convert_usd_to_rub_in_company(company: Dict, usd_to_rub: float) -> Dict:
    company["price_in_RUB"] = company["price_in_USD"] * usd_to_rub
    return company


def get_top_10_most_expensive_companies(
    data: List[Dict], usd_to_rub: float
) -> List[Dict]:
    top_10 = nlargest(10, data, key=lambda x: x["price_in_USD"])
    for company in top_10:
        company["price_in_RUB"] = company["price_in_USD"] * usd_to_rub
    return top_10


def get_top_10_min_pe(*data: Dict) -> List[Dict]:
    return list(
        nsmallest(
            10,
            filter(lambda x: "P/E" in x, data),
            key=lambda x: x["P/E"],
        ),
    )


def get_top_10_year_growth(data: List[Dict]) -> List[Dict]:
    return list(nlargest(10, data, key=lambda x: float(x["1_year_growth"][:-1])))


def get_top_10_profit_52_weeks(data: List[Dict]) -> List[Dict]:
    return list(nlargest(10, data, key=lambda x: x["profit_52_weeks"]))


def write_json_file(data: List[Dict], filename: str) -> None:
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def get_all_companies_data() -> None:
    all_urls_main_pages_with_companies = get_paginator_pages_sp500(
        requests.get("https://markets.businessinsider.com/index/components/s&p_500")
    )

    with ThreadPoolExecutor(max_workers=100) as pool:
        usd_to_rub = get_usd_to_rub()
        all_html_main_pages_with_companies = pool.map(
            requests.get, all_urls_main_pages_with_companies
        )
        all_companies_dicts_before_parsing_its_page = list(
            pool.map(get_all_companies_from_page, all_html_main_pages_with_companies)
        )
        all_companies_dicts_after_parsing_its_page = list(
            pool.map(
                get_info_from_company_url,
                itertools.chain(*all_companies_dicts_before_parsing_its_page),
            )
        )

        top_10_most_expensive_companies = get_top_10_most_expensive_companies(
            all_companies_dicts_after_parsing_its_page, usd_to_rub
        )
        write_json_file(
            top_10_most_expensive_companies, "top_10_most_expensive_companies.json"
        )

        top_10_min_pe = get_top_10_min_pe(*all_companies_dicts_after_parsing_its_page)
        write_json_file(top_10_min_pe, "top_10_min_pe.json")

        top_10_year_growth = get_top_10_year_growth(
            all_companies_dicts_after_parsing_its_page
        )
        write_json_file(top_10_year_growth, "top_10_year_growth.json")

        top_10_profit_52_weeks = get_top_10_profit_52_weeks(
            all_companies_dicts_after_parsing_its_page
        )
        write_json_file(top_10_profit_52_weeks, "top_10_profit_52_weeks.json")
