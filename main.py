import datetime as dt
import preprocessing
import edit
import auto_ml
import os

t = dt.datetime.now()

folder_path = os.path.join(os.getcwd(), 'img')  # フォルダのパスを設定

for file_name in os.listdir(folder_path):  # フォルダ内のファイル名を取得
    file_path = os.path.join(folder_path, file_name)  # ファイルのパスを設定
    if os.path.isfile(file_path):  # ファイルであれば
        os.remove(file_path)  # ファイルを削除
    elif os.path.isdir(file_path):  # フォルダであれば
        os.rmdir(file_path)  # フォルダを削除

df = preprocessing.main(test=True)
# df = preprocessing.main()
# df = edit.add_columns(df)
# auto_ml.save_test(df)
# print(df)

# 事後処理
elapsed_time = dt.datetime.now() - t
minutes, seconds = divmod(elapsed_time.total_seconds(), 60)
print(f"{minutes:.0f}分{seconds:.0f}秒")
