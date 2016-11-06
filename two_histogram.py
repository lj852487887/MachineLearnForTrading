from utils import get_data,plot_data
import pandas as pd
import matplotlib.pyplot as plt

def compute_daily_returns_with_pandas(df):
    # Compute and return the daily return values
    daily_returns = (df/df.shift(1))-1
    daily_returns.ix[0,:] = 0
    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range('2009-07-01', '2016-07-31')  # one month only
    symbols = ['01','02']
    df = get_data(symbols, dates)

    # Compute daily returns
    daily_returns = compute_daily_returns_with_pandas(df)



    daily_returns['01'].hist(bins=20,label='01')
    daily_returns['02'].hist(bins=20,label='02')
    plt.legend(loc='upper right')
    plt.show()


if __name__ == "__main__":
    test_run()