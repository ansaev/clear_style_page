import pytest
from style_cleaner import StyleCleanerService
import string


class TestClass:
    @pytest.fixture(params=["<body> <p style='font-size: 12pt'>Example</p></body>"])
    def page(self, request):
        return request.param

    @pytest.fixture(params=["http://habrahabr.ru/some/", "http://www.oracle.com/some/index.html"])
    def url(self, request):
        return request.param

    def test_style_cleaner(self, page):
        page = StyleCleanerService._clear_page(page)
        assert "style=" not in page

    def test_get_page(self, url):
        page = StyleCleanerService.get_page(url)
        assert "html" in page

    def test_get_clean_page(self, url):
        page = StyleCleanerService.get_clean_page(url)
        strings = string.split(page, "/n")
        for str in strings:
            assert "style=" not in str




