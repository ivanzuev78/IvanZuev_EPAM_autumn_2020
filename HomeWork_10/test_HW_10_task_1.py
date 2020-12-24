import os
import pickle

from HomeWork_10.task_threads import (
    convert_usd_to_rub_in_company,
    get_all_companies_from_page,
    get_paginator_pages_sp500,
    get_top_10_min_pe,
    get_top_10_most_expensive_companies,
    get_top_10_profit_52_weeks,
    get_top_10_year_growth,
)

import pytest

os.chdir(os.path.dirname(__file__))


def open_html_from_pickle(file: str):
    with open(file, "rb") as f:
        return pickle.load(f)


@pytest.fixture()
def all_companies():
    return [
        {
            "company_url": f"some_url_{i}",
            "name": f"comp_{i}",
            "1_year_growth": f"{i}%",
            "P/E": i,
            "profit_52_weeks": i,
            "price_in_USD": i,
        }
        for i in range(15)
    ]


def test_get_paginator_pages_sp500():
    html = open_html_from_pickle(
        "main_page_for_test_47companies_10paginator_pages_html_pickle"
    )
    assert len(get_paginator_pages_sp500(html)) == 10


def test_get_all_companies_from_page():
    html = open_html_from_pickle(
        "main_page_for_test_47companies_10paginator_pages_html_pickle"
    )
    assert len(get_all_companies_from_page(html)) == 47


def test_get_top_10_most_expensive_companies(all_companies):

    assert get_top_10_most_expensive_companies(all_companies, 75) == [
        {
            "company_url": f"some_url_{i}",
            "name": f"comp_{i}",
            "1_year_growth": f"{i}%",
            "P/E": i,
            "profit_52_weeks": i,
            "price_in_USD": i,
            "price_in_RUB": i * 75,
        }
        for i in range(5, 15)
    ]


def test_get_top_10_min_pe(all_companies):
    assert get_top_10_min_pe(all_companies) == all_companies[:10]


def test_get_top_10_year_growth(all_companies):
    assert get_top_10_year_growth(all_companies) == all_companies[5:15]


def test_get_top_10_profit_52_weeks(all_companies):
    assert get_top_10_profit_52_weeks(all_companies) == all_companies[5:15]


def test_convert_usd_to_rub_in_company():
    assert convert_usd_to_rub_in_company({"price_in_USD": 1}, 75) == {
        "price_in_USD": 1,
        "price_in_RUB": 75,
    }
