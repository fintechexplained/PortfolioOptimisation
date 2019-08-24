import numpy as np
from scipy.optimize import minimize
import pandas as pd

class optimiser:
    Constraints = []
    def __init__(self, mc, risk_function, return_function, targets, portfolio_size):
        self.__portfolio_size = portfolio_size
        self.__targets = targets
        self.__mc = mc
        self.__risk_function = risk_function
        self.__return_function = return_function

    def generate_portfolios(self, returns, covariance, risk_free_rate):
        x0 = np.ones(self.__portfolio_size) * (1.0 / self.__portfolio_size) 
        bounds = ((0, 1),) * (self.__portfolio_size)

        portfolios_allocations_df = pd.DataFrame({'Symbol':returns.index,'MeanReturn':returns.values})
        extra_data = pd.DataFrame({'Symbol':['Return','Risk','SharpeRatio'], 'MeanReturn':[0,0,0]})
        portfolios_allocations_df = portfolios_allocations_df.append(extra_data, ignore_index=True)

        
        i = 0
        counter_to_print =  int(len(self.__targets)/10)
        for my_return in self.__targets:
            constraints=[]
            constraints.append({'type': 'eq', 'fun': lambda inputs: 1.0 - np.sum(inputs)})
            constraints.append({'type': 'eq', 'args': (returns,),
                                     'fun': lambda allocations, returns:
                                     my_return - self.__return_function(returns, allocations)})

            #optimised allocations
            allocations = self.solve(x0, constraints, bounds, covariance).x
            expectedreturns = self.__return_function(returns, allocations)

            #Calculate volatility
            volatility = self.__risk_function(allocations, covariance)

            sharpe_ratio = self.__mc.calculate_sharpe_ratio(volatility, expectedreturns, risk_free_rate)

            portfolio_data = allocations
            portfolio_data = np.append(portfolio_data,expectedreturns)
            portfolio_data = np.append(portfolio_data,volatility)
            portfolio_data = np.append(portfolio_data,sharpe_ratio)

            i = i+1
            portfolio_id = 'Portfolio_'+str(i)
            portfolios_allocations_df[portfolio_id] = portfolio_data

            #printing approx 10x
            if (i%counter_to_print==0):
                print('Completed Generating '+str(i)+' Portfolios')
        return portfolios_allocations_df
        
    def solve(self, x0, constraints, bounds, covariance):
        return minimize(self.__risk_function, x0,
                       args=(covariance), method='SLSQP',
                       #prints covergence msgs
                       options={'disp': True},
                       constraints=constraints,
                       bounds=bounds)

    
    