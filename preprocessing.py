import pandas as pd
import os
import datetime as dt
import edit


def init(df, df_date, brand_code):
    df_extracted = df.loc[:, brand_code]
    df = pd.concat([df_date, df_extracted], axis=1)
    df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
    df = df.astype({'Close': float, 'High': float, 'Open': float, 'Low': float, 'Volume': float})
    return df


def main(test=False):
    trades_filename = 'nikkei_trades_20230415.csv'
    df_trades = pd.read_csv(os.path.join(os.getcwd(), 'data', trades_filename))
    new_columns = df_trades.iloc[0].tolist()
    df_trades.columns = new_columns
    df_trades = df_trades.drop([0, 1])
    df_trades = df_trades.rename(columns={"Symbols": 'Date'})
    df_date = df_trades['Date']
    brand = '7832.jp'
    df_init = init(df_trades, df_date, brand)
    edit.add_columns(df_init, brand)

    evaluated_list = ['Close', 'High', 'Low', 'Open', 'Volume', 'Upper_band', 'Lower_band', 'Close_10ma', 'Close_60ma', 'diff_10ma', '10ma_positive', 'diff_60ma', '60ma_positive', 'brand', 'momentum', 'deviation_band_close']
    df_buy = pd.DataFrame(columns=evaluated_list)
    df_sell = pd.DataFrame(columns=evaluated_list)

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
            # df_init = pd.concat([df_init, temp_df])
            # df_init = df_init.reset_index(drop=True)

            buy_df, sell_df = edit.add_columns(temp_df, b)
            if not buy_df.empty:
                df_buy = pd.concat([df_buy, buy_df])
            elif not sell_df.empty:
                df_sell = pd.concat([df_sell, sell_df])

    return df_buy, df_sell
