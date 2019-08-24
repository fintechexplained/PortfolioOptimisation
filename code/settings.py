import numpy as np
import datetime as dt
from calculator import risk_return_calculator

class settings:

    PriceEvent = 'Adj Close'
    ReturnType = 'Geometric'
    Optimisersettings = {}
    OptimiserType = 'OLS'
    CompaniesUrl = 'https://en.wikipedia.org/wiki/NASDAQ-100'#'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    NumberOfPortfolios = 10#0000#0
    API = 'yahoo'
    YearsToGoBack = 3
    RiskFreeRate = 0
    CompanyFetchMode = "PreFixed" #Auto
    MyCompanies = ['ZM','UBER','SWI','RNG','CRWD', 'WORK', 'SYMC']
    PortfolioOptimisationPath = 'C:\Temp\PortfolioOptimisation.xlsx'
    RiskFunction = risk_return_calculator.calculate_portfolio_risk
    ReturnFunction = risk_return_calculator.calculate_portfolio_expectedreturns
    AssetsExpectedReturnsFunction = risk_return_calculator.calculate_assets_expectedreturns
    AssetsCovarianceFunction = risk_return_calculator.calculate_assets_covariance
    DailyAssetsReturnsFunction = risk_return_calculator.calculate_daily_asset_returns

    @staticmethod
    def get_my_targets():
        return np.arange(0, 1.5, 0.05)

    @staticmethod
    def get_end_date():
        return dt.date.today()

    @staticmethod
    def get_start_date(end_date):
        return end_date - dt.timedelta(days=settings.YearsToGoBack*365)
