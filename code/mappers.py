import pandas as pd
class portfolios_allocation_mapper:
    @staticmethod
    def map_to_risk_return_ratios(input):
        portfolios = input.columns.values[2:]
        returns = input.loc[input['Symbol'] == 'Return'].values[0][2:]
        risks = input.loc[input['Symbol'] == 'Risk'].values[0][2:]
        sharpe_ratios = input.loc[input['Symbol'] == 'SharpeRatio'].values[0][2:]
        df = pd.DataFrame(
            {'Portfolio': portfolios,
            'Return': returns,
            'Risk': risks, 
            'SharpeRatio': sharpe_ratios})
        return df