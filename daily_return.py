import utils as pt
import pandas as pd
import matplotlib.pyplot as plt

def compute_daily_returns(df):
    # Compute and return the daily return values
    daily_returns = df.copy()
    daily_returns[1:] = (daily_returns[1:]/daily_returns[:-1].values)-1
    daily_returns.ix[0,:] = 0 #set daily returns for row 0 to 0
    return daily_returns

def compute_daily_returns_with_pandas(df):
    # Compute and return the daily return values
    daily_returns = (df/df.shift(1))-1
    daily_returns.ix[0,:] = 0
    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range('2016-07-01', '2016-07-31')  # one month only
    symbols = ['01','02']
    df = pt.get_data(symbols, dates)
    pt.plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns_with_pandas(df)
    pt.plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")


if __name__ == "__main__":
    test_run()