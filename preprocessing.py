import pandas as pd
import os
import datetime as dt


def init(df, df_date, brand_code):
    df_extracted = df.loc[:, brand_code]
    df = pd.concat([df_date, df_extracted], axis=1)
    df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
    df = df.astype({'Close': float, 'High': float, 'Open': float, 'Low': float, 'Volume': float})
    return df


def main(test=False):
    trades_filename = 'nikkei_trades_20230408.csv'
    df_trades = pd.read_csv(os.path.join(os.getcwd(), 'data', trades_filename))
    new_columns = df_trades.iloc[0].tolist()
    df_trades.columns = new_columns
    df_trades = df_trades.drop([0, 1])
    df_trades = df_trades.rename(columns={"Symbols": 'Date'})
    df_date = df_trades['Date']

    df_init = init(df_trades, df_date, '4911.jp')
    if not test:
        brands_filename = 'nikkei_listed_20230314_.csv'

        # ブランドデータcsvを読み込んでリスト化
        df_brands = pd.read_csv(os.path.join(os.getcwd(), 'data', brands_filename))
        df_brands['0'] = df_brands['0'].astype(str)

        # トレードデータの処理
        _list_brands = list(df_brands['0'])
        list_brands = [b + ".jp" for b in _list_brands]
        for b in list_brands:
            temp_df = init(df_trades, df_date, b)
            df_init = pd.concat([df_init, temp_df])
    df_init = df_init.reset_index(drop=True)

    # # normalize
    # rate = 1000 / df_init['Close'][0]
    # df_init[['Close', 'Open', 'High', 'Low']] = df_init[['Close', 'Open', 'High', 'Low']] * rate
    # volume_rate = 10000 / df_init['Volume'][0]
    # df_init[['Volume']] = df_init[['Volume']] * volume_rate

    return df_init