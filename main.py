class StyleCleanereWithParams:
    def __init__(self):
        import argparse
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("-url", required=True, dest="url")
        self.url = arg_parser.parse_args().url

    def run(self):
        assert self.url
        from style_cleaner import StyleCleanerService
        style_cleaner = StyleCleanerService()
        self.page = style_cleaner.get_clean_page(url=self.url)

    def print_result(self):
        assert self.page
        print("page:", self.page)

if __name__ == "__main__":
    programm = StyleCleanereWithParams()
    programm.run()
    programm.print_result()

