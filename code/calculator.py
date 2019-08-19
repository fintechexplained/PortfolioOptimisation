import numpy as np
from functools import reduce
import pandas as pd

class risk_return_calculator:
    @staticmethod
    def calculate_assets_expectedreturns(returns):        
            return returns.mean() * 252

    @staticmethod
    def calculate_assets_covariance(returns):        
            return returns.cov() * 252

    @staticmethod
    def calculate_portfolio_expectedreturns(returns, allocations):
        return sum(returns * allocations)

    @staticmethod    
    def calculate_portfolio_risk(allocations, cov):
        return np.sqrt(reduce(np.dot, [allocations, cov, allocations.T]))

    @staticmethod
    def calculate_daily_asset_returns(stock_prices, return_type):
        return np.log(stock_prices / stock_prices.shift(1))

class metrics_calculator:  
    

    @staticmethod
    def calculate_sharpe_ratio(risk, returns, risk_free_rate):
        return (returns-risk_free_rate)/risk

    @staticmethod
    def get_max_sharpe_ratio(df):
        return df.ix[df['SharpeRatio'].astype(float).idxmax()]

    @staticmethod
    def get_min_risk(df):
        return df.ix[df['Risk'].astype(float).idxmin()]