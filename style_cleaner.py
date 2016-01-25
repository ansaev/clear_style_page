import requests
from bs4 import BeautifulSoup


class StyleCleanerService(object):
    # params:
    # url: String, required, target url to get page
    # throws: requests.exceptions.MissingSchema for worng adress
    @staticmethod
    def get_page(url):
        response = requests.get(url=url)
        return response.content

    # params:
    # url: String, required, target url to get page
    # throws: requests.exceptions.MissingSchema for worng adress
    @staticmethod
    def get_clean_page(url):
        page = StyleCleanerService.get_page(url=url)
        page = StyleCleanerService._clear_page(page=page)
        return page

    # params:
    # page: String, required, text to clear from styles info
    # throws:
    @staticmethod
    def _clear_page(page):
        dom = BeautifulSoup(page, 'html.parser')
        all_elements = dom.find_all()
        for element in all_elements:
            try:
                del element['style']
            except KeyError:
                pass
        return str(dom)

