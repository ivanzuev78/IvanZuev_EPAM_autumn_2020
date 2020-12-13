import os
import sqlite3

from HomeWork_8.task_2 import TableData

import pytest


@pytest.fixture()
def database_name():
    database_name = "test_database.sqlite"
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


def test_tabledata_create_with_good_database_name_and_column(database_name):
    data = TableData(database_name, "test")
    assert data["Yeltsin"] == {"name": "Yeltsin", "param_str": "test_str"}
    assert data["Name_not_DB"] is None


def test_tabledata_len_protocol(database_name):
    data = TableData(database_name, "test")
    assert len(data) == 2


def test_tabledata_iterable_protocol(database_name):
    data = TableData(database_name, "test")
    names = ["Yeltsin", "Trump"]
    for index, man in enumerate(data):
        assert man["name"] == names[index]


def test_tabledata_contains_protocol(database_name):
    data = TableData(database_name, "test")
    assert ("Trump" in data) is True
    assert ("Bill" in data) is False


def test_tabledata_returns_recent_data(database_name):
    data = TableData(database_name, "test")
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO test(name, param_str) VALUES(?, ?)", ("man1", "test_str")
    )
    conn.commit()
    conn.close()
    assert ("man1" in data) is True
