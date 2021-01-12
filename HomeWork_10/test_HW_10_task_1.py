import os
import pickle

from HomeWork_10.task_threads import (
    get_all_companies_from_page,
    get_paginator_pages_sp500,
    get_top_10_min_pe,
    get_top_10_most_expensive_companies,
    get_top_10_profit_52_weeks,
    get_top_10_year_growth,
)

import pytest


def open_html_from_pickle(file: str):
    with open(file, "rb") as f:
        return pickle.load(f)


@pytest.fixture(autouse=True)
def _change_dir():
    os.chdir(os.path.dirname(__file__))


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
        for i in range(14, 4, -1)
    ]


def test_get_top_10_min_pe(all_companies):
    assert get_top_10_min_pe(*all_companies) == all_companies[:10]


def test_get_top_10_year_growth(all_companies):
    assert get_top_10_year_growth(all_companies) == all_companies[14:4:-1]


def test_get_top_10_profit_52_weeks(all_companies):
    assert get_top_10_profit_52_weeks(all_companies) == all_companies[14:4:-1]
