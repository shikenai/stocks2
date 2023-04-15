import pandas as pd


def main(df, brand):
    evaluated_list = ['Close', 'High', 'Low', 'Open', 'Volume', 'Upper_band', 'Lower_band', 'Close_10ma', 'Close_60ma',
                      'diff_10ma', '10ma_positive', 'diff_60ma', '60ma_positive', 'brand', 'momentum',
                      'deviation_band_close']
    empty_df = pd.DataFrame(columns=evaluated_list)
    df['diff_10ma'] = df['Close_10ma'].diff()
    df['10ma_positive'] = df['diff_10ma'].apply(lambda x: x > 0)
    df['diff_60ma'] = df['Close_60ma'].diff()
    df['60ma_positive'] = df['diff_60ma'].apply(lambda x: x > 0)
    last_df = df.tail(1)
    last_df['brand'] = brand
    if last_df['10ma_positive'][0] and last_df['60ma_positive'][0] and last_df['Close'][0] > last_df['Close_10ma'][0]:
        last_df['momentum'] = (last_df['diff_10ma'] - last_df['diff_60ma']) / last_df['Close']
        # プレス局面で、Upper_band - Closeを考える。
        # Ub>Closeのとき、つまり、Closeが上のラインに達していないとき、deviationは正となる。この時は、まだ買いシグナルは出ていない。
        # Ub<Closeのとき、つまり、Closeが上のラインに達しているとき、deviationは負となる。この時は、すでに売りシグナルが出ている。
        last_df['deviation_band_close'] = (last_df['Upper_band'][0] - last_df['Close'][0]) / last_df['Close'][0]
        kind = 'buy'
        return kind, last_df
    elif last_df['10ma_positive'][0] == False and last_df['60ma_positive'][0] == False and last_df['Close'][0] < \
            last_df['Close_10ma'][0]:
        last_df['momentum'] = (last_df['diff_10ma'] - last_df['diff_60ma']) / last_df['Close']
        # マイナス局面で、Lower_band - Closeを考える。
        # Lb<Closeのとき、つまり、Closeが下のラインに達していないとき、deviationは負となる。この時は、まだいわゆる買いシグナルは出ていない。
        # Lb>Closeのとき、つまり、Closeが下のラインに達しているとき、deviationは正となる。この時は、すでに買いシグナルが出ている。
        last_df['deviation_band_close'] = (last_df['Lower_band'][0] - last_df['Close'][0]) / last_df['Close'][0]
        kind = 'sell'
        return kind, last_df
    else:
        last_df = empty_df
        kind = 'None'
        return kind, last_df
