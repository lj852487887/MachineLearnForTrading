import pandasTest as pt
import pandas as pd
import matplotlib.pyplot as plt

def fill_missing_data(df):
    df.fillna(method='ffill',inplace=True)
    df.fillna(method='bfill',inplace=True)

def test_run():
    #read data
    dates = pd.date_range('1990-05-01', '2016-09-30')
    symbols = ['01','02','03','04']
    df = pt.get_data(symbols, dates)
    fill_missing_data(df)
    pt.plot_data(df)

if __name__ == "__main__":
    test_run()