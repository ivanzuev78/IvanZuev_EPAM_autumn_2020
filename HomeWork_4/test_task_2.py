import urllib.request
from urllib.error import URLError, HTTPError

import pytest
from unittest.mock import MagicMock

from HomeWork_4.task_2_mock_input import count_dots_on_i


def test_count_dots_on_i_good_(monkeypatch):
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        MagicMock(
            return_value=[
                b"<html>",
                b"<head>iii</head>",
                b"<body>qqq</body>",
                b"</html>",
            ]
        ),
    )
    assert count_dots_on_i("https://example.com/") == 3


def test_count_dots_on_i_mock_unreachable_url(monkeypatch):
    url = "https://unreachable-url.com/"

    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        MagicMock(side_effect=HTTPError(404, "NF", "", "", "")),
    )
    with pytest.raises(ValueError, match=f"Unreachable {url}"):
        count_dots_on_i(url)
