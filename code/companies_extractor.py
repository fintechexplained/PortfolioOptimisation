import pandas as pd
class webpage_companies_extractor:
    Url = None

    def __init__(self, url):
        self.__url = url

    def get_companies_list(self, current_portfolio=None):
            dfs = pd.read_html(self.__url, header=0)
            first_table = dfs[2]
            company_names = first_table
            return company_names

class static_companies_extractor:
    def __init__(self, my_companies):
        self.__my_companies = my_companies

    def get_companies_list(self, current_portfolio=None):
        return pd.DataFrame({'Ticker':self.__my_companies})