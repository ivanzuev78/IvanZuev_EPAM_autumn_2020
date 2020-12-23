import os
import shutil
import sqlite3

from HomeWork_8.task_2 import TableData

import pytest


@pytest.fixture()
def copied_db_to_test_added_data():
    shutil.copyfile("example.sqlite", "example_2.sqlite")
    yield "example_2.sqlite"
    os.remove("example_2.sqlite")


def test_tabledata_with_good_database_name_and_column():
    data = TableData("example.sqlite", "presidents")
    assert data["Yeltsin"] == {"age": 999, "country": "Russia", "name": "Yeltsin"}
    assert data["Name_not_DB"] is None


def test_tabledata_len_protocol():
    data = TableData("example.sqlite", "presidents")
    assert len(data) == 3


def test_tabledata_iterable_protocol():
    data = TableData("example.sqlite", "presidents")
    names = ["Yeltsin", "Trump", "Big Man Tyrone"]
    for index, man in enumerate(data):
        assert man["name"] == names[index]


def test_tabledata_contains_protocol():
    data = TableData("example.sqlite", "presidents")
    assert ("Trump" in data) is True
    assert ("Bill" in data) is False


def test_tabledata_returns_recent_data(copied_db_to_test_added_data):
    data = TableData(copied_db_to_test_added_data, "presidents")
    conn = sqlite3.connect(copied_db_to_test_added_data)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO presidents(name, age, country) VALUES(?, ?, ?)",
        ("man1", "4567", "Lapland"),
    )
    conn.commit()
    conn.close()
    assert ("man1" in data) is True


def test_tabledata_get_wrong_column_name():
    with pytest.raises(AttributeError):
        TableData("example.sqlite", "wrong column")
