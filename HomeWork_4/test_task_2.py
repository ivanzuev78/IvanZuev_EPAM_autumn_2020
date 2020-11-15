import urllib.request
from urllib.error import URLError

import pytest
from unittest.mock import MagicMock

from HomeWork_4.task_2_mock_input import count_dots_on_i


def test_count_dots_on_i_data_from_internet():
    url = "https://example.com/"
    assert count_dots_on_i(url) == 59


def test_count_dots_on_i_data_from_mock():
    url = "https://example.com/"
    urllib.request.urlopen = MagicMock(
        return_value=[b"<html>", b"<head>iii</head>", b"<body>qqq</body>", b"</html>"]
    )
    assert count_dots_on_i(url) == 3


def test_count_dots_on_i_mock_unreachable_url():
    url = "https://unreachable-url.com/"
    urllib.request.urlopen = MagicMock(
        return_value=URLError("<urlopen error [Errno 11001] getaddrinfo failed>")
    )
    with pytest.raises(ValueError, match=f"Unreachable {url}"):
        count_dots_on_i(url)
