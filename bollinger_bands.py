import utils as pt
import pandas as pd
import matplotlib.pyplot as plt

def get_rolling_mean(df,window):
    return pd.rolling_mean(df,window=window)

def get_rolling_std(df,window):
    return pd.rolling_std(df,window=window)

def get_bollinger_bands(rolling_mean,rolling_std):
    upper_band = rolling_mean + 2*rolling_std
    lower_band = rolling_mean - 2*rolling_std
    return upper_band, lower_band

def test_run():
    #read data
    dates = pd.date_range('2015-05-01', '2016-09-30')
    symbols = ['01']
    df = pt.get_data(symbols, dates)

    # Compute rolling mean
    rm_SPY = get_rolling_mean(df['01'],window=20)

    # Compute rolling standard deviation
    rstd_SPY = get_rolling_std(df['01'], window=20)

    # Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)

    ax = df['01'].plot(title='bollinger bands',label='01')
    rm_SPY.plot(label='Rolling mean',ax=ax)
    upper_band.plot(label='upper band',ax=ax)
    lower_band.plot(label='lower band',ax=ax)

    #add axis labels and legend
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    test_run()