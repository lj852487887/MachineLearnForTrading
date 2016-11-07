from utils import get_data,plot_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def compute_daily_returns_with_pandas(df):
    # Compute and return the daily return values
    daily_returns = (df/df.shift(1))-1
    daily_returns.ix[0,:] = 0
    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range('2009-07-01', '2016-07-31')  # one month only
    symbols = ['01','02','03']
    df = get_data(symbols, dates)
    df.fillna(method='ffill',inplace=True)
    df.fillna(method='bfill',inplace=True)
    # Compute daily returns
    daily_returns = compute_daily_returns_with_pandas(df)


    daily_returns.plot(kind='scatter',x='01',y='02')
    beta_02,alpha_02 = np.polyfit(daily_returns['01'],daily_returns['02'],1)
    plt.plot(daily_returns['01'],beta_02*daily_returns['01']+alpha_02,'-',color='r')
    plt.show()

    daily_returns.plot(kind='scatter',x='01',y='03')
    beta_03,alpha_03 = np.polyfit(daily_returns['01'],daily_returns['03'],1)
    plt.plot(daily_returns['01'],beta_03*daily_returns['01']+alpha_03,'-',color='r')
    plt.show()

    print daily_returns.corr(method='pearson')

    print ghjghj



if __name__ == "__main__":
    test_run()