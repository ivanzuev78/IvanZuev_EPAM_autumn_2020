import os
import sqlite3

from HomeWork_8.task_2 import TableData

import pytest

os.chdir(os.path.dirname(__file__))


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


def test_tabledata_returns_recent_data():
    data = TableData("example.sqlite", "presidents")
    conn = sqlite3.connect("example.sqlite")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO presidents(name, age, country) VALUES(?, ?, ?)",
        ("man1", "4567", "Lapland"),
    )
    conn.commit()
    assert ("man1" in data) is True
    cursor.execute("DELETE FROM presidents WHERE name = ?", ("man1",))
    conn.commit()
    conn.close()


def test_tabledata_get_wrong_column_name():
    with pytest.raises(AttributeError):
        TableData("example.sqlite", "wrong column")
