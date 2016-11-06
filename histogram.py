import utils as pt
import pandas as pd
import matplotlib.pyplot as plt

def compute_daily_returns_with_pandas(df):
    # Compute and return the daily return values
    daily_returns = (df/df.shift(1))-1
    daily_returns.ix[0,:] = 0
    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range('2000-07-01', '2016-07-31')  # one month only
    symbols = ['01']
    df = pt.get_data(symbols, dates)

    # Compute daily returns
    daily_returns = compute_daily_returns_with_pandas(df)

    daily_returns.hist(bins=20)


    mean = daily_returns['01'].mean()
    std = daily_returns['01'].std()

    plt.axvline(mean,color='w',linestyle='dashed',linewidth=2)
    plt.axvline(std,color='r',linestyle='dashed',linewidth=2)
    plt.axvline(-std,color='r',linestyle='dashed',linewidth=2)

    plt.show()

    print daily_returns.kurtosis()

if __name__ == "__main__":
    test_run()