import os
import sqlite3

from HomeWork_8.task_2 import TableData

import pytest


@pytest.fixture()
def database_name():
    database_name = "test_database.sqlite"
    if os.path.exists(database_name):
        os.remove(database_name)
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test(name text, param_str text)")
    cursor.executemany(
        "INSERT INTO test(name, param_str) VALUES(?, ?)",
        [("Yeltsin", "test_str"), ("Trump", "is not presedent")],
    )
    conn.commit()
    conn.close()
    yield database_name
    os.remove(database_name)


def test_tabledata_with_good_database_name_and_column(database_name):
    data = TableData(database_name, "test")
    assert data["Yeltsin"] == {"name": "Yeltsin", "param_str": "test_str"}
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


def test_tabledata_returns_recent_data(database_name):
    data = TableData(database_name, "test")
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO presidents(name, age, country) VALUES(?, ?, ?)",
        ("man1", "4567", "Lapland"),
    )
    conn.commit()
    assert ("man1" in data) is True
    conn.close()


def test_tabledata_get_wrong_column_name():
    with pytest.raises(AttributeError):
        TableData("example.sqlite", "wrong column")
