import pandas as pd
import os
import plotter


def add_columns(df, brand):
    df, index_list = add_bb_rsi_sc(df)

    col_list = ['Close', 'High', 'Low', 'Open']
    ma_list = []
    # for col in col_list:
    #     df, ma_list = add_ma(df, col)
    df, ma_list = add_ma(df, 'Close')
    pd.set_option('display.max_rows', 270)
    pd.set_option('display.max_columns', 20)

    df = df.dropna()
    df = df.set_index('Date')
    print(df.tail(3))
    # plotter.plot1(df, 'Close', ma_list, index_list, brand)
    # df.to_csv(os.path.join(os.path.join(os.getcwd(), 'data', 'test.csv')))

    # return df


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
    ma_list = [3, 10, 60]
    for i in ma_list:
        df[f'{col}_{str(i)}ma'] = df[col].rolling(i).mean()

    return df, ma_list


def add_bb_rsi_sc(df, rsi_period=14, bb_period=20, bb_dev=2,
                  index_list=('RSI', 'Upper_band', 'Lower_band', 'StochK', 'StochD')):
    # # RSIの計算　とりあえず使わないことにしたので凍結。
    # delta = df['Close'].diff()
    # gain = delta.mask(delta < 0, 0)
    # loss = -delta.mask(delta > 0, 0)
    # avg_gain = gain.rolling(rsi_period).mean()
    # avg_loss = loss.rolling(rsi_period).mean()
    # rs = avg_gain / avg_loss
    # rsi = 100 - (100 / (1 + rs))
    # df[index_list[0]] = rsi

    # ボリンジャーバンドの計算
    rolling_mean = df['Close'].rolling(bb_period).mean()
    rolling_std = df['Close'].rolling(bb_period).std()
    upper_band = rolling_mean + (bb_dev * rolling_std)
    lower_band = rolling_mean - (bb_dev * rolling_std)
    df[index_list[1]] = upper_band
    df[index_list[2]] = lower_band

    # # ストキャスティクスの計算 とりあえず使わないことにしたので凍結。
    # highest_high = df['High'].rolling(window=14).max()
    # lowest_low = df['Low'].rolling(window=14).min()
    # stoch_k = ((df['Close'] - lowest_low) / (highest_high - lowest_low)) * 100
    # stoch_d = stoch_k.rolling(window=3).mean()
    # df[index_list[3]] = stoch_k
    # df[index_list[4]] = stoch_d

    return df, index_list
