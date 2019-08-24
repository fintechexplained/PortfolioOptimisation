import matplotlib.pyplot as plt

class chart_plotter:

    def __init__(self, mc):
        self.__mc = mc

    
    def plot_efficient_frontier(self, data):
        plt.plot(data['Risk'], data['Return'], 'r-x')

    def show_plots(self):
        plt.show()

    def plot_single_point(self, x,y,title,colour):
        plt.scatter(x=x, y=y, c=colour, marker='D', s=200)
        plt.annotate(title, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

    def plot_portfolios(self, df):
        # find min Volatility & max sharpe values in the dataframe (df)
        
        max_sharpe_ratio = self.__mc.get_max_sharpe_ratio(df)
        min_risk = self.__mc.get_min_risk(df)

        plt.scatter(df['Risk'], df['Return'],c=df['SharpeRatio'],cmap='viridis', edgecolors='red')
        x = max_sharpe_ratio['Risk']
        y = max_sharpe_ratio['Return']
        name = max_sharpe_ratio['Portfolio']
        
        plt.title(str(len(df))+" Portfolios Risk-Return")
        plt.xlabel("Risk")
        plt.ylabel("Return")

        self.plot_single_point(x,y,'Max Sharpe Ratio: '+name, 'green')
        x = min_risk['Risk']
        y = min_risk['Return']
        name = min_risk['Portfolio']
        self.plot_single_point(x,y,'Min Risk: '+name, 'red')

        equal_allocations_portfolio = df.loc[df['Portfolio'] == 'EqualAllocationPortfolio']
        x = equal_allocations_portfolio['Risk']
        y = equal_allocations_portfolio['Return']
        name = equal_allocations_portfolio['Portfolio']
        self.plot_single_point(x,y,'Portfolio: '+name, 'black')
    

    def plot_prices(self, closing_prices):
        ax = plt.gca()
        columns = [c for c in closing_prices.columns if c not in 'Date']
        closing_prices.plot(kind='line',use_index=True,y=columns,ax=ax, title='Asset (Stock) Prices')
        plt.show()


    def plot_returns(self, returns):
        ax = plt.gca()
        columns = [c for c in returns.columns if c not in 'Date']
        returns.plot(kind='line',use_index=True, y=columns,ax=ax, title='Asset (Stock) Returns')
        plt.show()

    def plot_correlation_matrix(self, df):
        cols = df.columns.values
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(df.corr(), interpolation='nearest')
        fig.colorbar(cax)

        ax.set_xticklabels(cols)
        ax.set_yticklabels(cols)
        plt.show()

