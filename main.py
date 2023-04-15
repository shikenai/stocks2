import datetime as dt
import preprocessing
import edit
import auto_ml

t = dt.datetime.now()

# df = preprocessing.main(test=True)
df = preprocessing.main(test=True)
df = edit.add_columns(df)
# auto_ml.save_test(df)

print(df)

# 事後処理
elapsed_time = dt.datetime.now() - t
minutes, seconds = divmod(elapsed_time.total_seconds(), 60)
print(f"{minutes:.0f}分{seconds:.0f}秒")
