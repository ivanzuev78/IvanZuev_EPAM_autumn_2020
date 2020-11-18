import urllib.request
from urllib.error import URLError

import pytest
from unittest.mock import MagicMock

from HomeWork_4.task_2_mock_input import count_dots_on_i


@pytest.fixture
def magic_mock_into_urlopen_return_good_html():
    func = urllib.request.urlopen
    urllib.request.urlopen = MagicMock(
        return_value=[b"<html>", b"<head>iii</head>", b"<body>qqq</body>", b"</html>"]
    )
    yield
    urllib.request.urlopen = func


def test_count_dots_on_i_data_from_mock(magic_mock_into_urlopen_return_good_html):
    assert count_dots_on_i("https://example.com/") == 3


@pytest.fixture
def magic_mock_into_urlopen_return_url_error():
    func = urllib.request.urlopen
    urllib.request.urlopen = MagicMock(
        return_value=URLError("<urlopen error [Errno 11001] getaddrinfo failed>")
    )
    yield
    urllib.request.urlopen = func


def test_count_dots_on_i_mock_unreachable_url(magic_mock_into_urlopen_return_url_error):
    url = "https://unreachable-url.com/"
    with pytest.raises(ValueError, match=f"Unreachable {url}"):
        count_dots_on_i(url)
