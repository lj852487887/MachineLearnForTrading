import pandasTest as pt
import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    #read data
    dates = pd.date_range('2015-05-01', '2016-09-30')
    symbols = ['01']
    df = pt.get_data(symbols, dates)

    ax = df['01'].plot(title='01 rolling mean',label='01')
    rm_SPY = pd.rolling_mean(df['01'],window=20)

    rm_SPY.plot(label='Rolling mean',ax=ax)

    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    test_run()