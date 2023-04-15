import pandas as pd
import os
import plotter


def add_columns(df):
    df = add_candle(df)
    col_list = ['Close', 'High', 'Low', 'Open']
    ma_list = []
    for col in col_list:
        df, ma_list = add_ma(df, col)

    # pd.set_option('display.max_rows', 270)
    pd.set_option('display.max_columns', 20)

    df = df.dropna()
    df = df.set_index('Date')
    plotter.plot1(df, 'Close', ma_list)
    # plotter.plot2(df, col_list, ma_list)
    # for col in col_list:
    #     plotter.plot1(df, col, ma_list)
    df.to_csv(os.path.join(os.path.join(os.getcwd(), 'data', 'test.csv')))

    return df


def add_candle(df):
    # 'entity'は、正なら終値の方が高かった、負なら始値の方が高かったということを示すもの。
    df['entity'] = df['Close'] - df['Open']
    df['upper_beard'] = df['High'] - df[['Close', 'Open']].max(axis=1)
    df['upper_beard_rate'] = df['upper_beard'] / df['entity'].abs().replace(0, 1)
    df['underbelly'] = df['Low'] - df[['Close', 'Open']].min(axis=1)
    df['underbelly_rate'] = df['underbelly'] / df['entity'].abs().replace(0, 1)
    df = df.drop(['upper_beard', 'underbelly'], axis=1)
    return df


def add_ma(df, col):
    ma_list = [5, 10, 14, 21, 60]
    # ma_list = [5, 20]
    for i in ma_list:
        df[f'{col}_{str(i)}ma'] = df[col].rolling(i).mean()
        # df[f'{str(i)}ma_diff'] = df[f'{str(i)}ma'].diff()
        # df[f'{str(i)}ma_trend'] = df[f'{str(i)}ma_diff'].apply(lambda x: 1 if x > 0 else -1)
        # df = df.drop([f'{str(i)}ma_diff'], axis=1)
        # if i == ma_list[0] or i == ma_list[1]:
        #     pass
        # else:
        #     df = df.drop([f'{str(i)}ma'], axis=1)

    # 没
    # df['hist_ma'] = df[f'{str(ma_list[0])}ma'] - df[f'{str(ma_list[1])}ma']
    # for i in ma_list:
    #     df[f'{str(i)}_hist_ma'] = df['hist_ma'].rolling(i).mean()
    # df['acceleration_ma'] = df[f'{str(ma_list[0])}_hist_ma'] > df[f'{str(ma_list[1])}_hist_ma']
    # df['acceleration_shifted'] = df['acceleration'].shift(-1)
    # df['Close+acceleration'] = df['Close'] + df['acceleration_shifted']
    # df[f'GX_{str(ma_list[0])}_{str(ma_list[1])}'] = df[f'{str(ma_list[0])}ma'] > df[f'{str(ma_list[1])}ma']
    # df[f'GX_CA_{str(ma_list[1])}ma'] = df['Close+acceleration'] > df[f'{str(ma_list[1])}ma']
    # df = df.drop(['High', 'Low', 'Open', 'Date'], axis=1)
    return df, ma_list
