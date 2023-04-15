import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import os

def plot1(df, target, ma_list, col_list, brand):
    target_columns = [target]
    # _col_list = list(col_list)
    # del _col_list[1]
    # del _col_list[1]
    # df_index = df[_col_list]
    # print('----')
    # print(df_index)
    for ma in ma_list:
        target_columns.append(target + f'_{str(ma)}ma')
    target_columns.append(col_list[1])
    target_columns.append(col_list[2])
    df = df[target_columns]

    fig = plt.figure(figsize=(10, 10), facecolor='lightblue')
    ax1 = fig.add_subplot(1, 1, 1)
    x = df.index
    ax1.plot(x, df[target], label=target)
    for col in target_columns:
        if not col == target:
            ax1.plot(x, df[col], linestyle='dotted', label=col)
            if "band" in col:
                ax1.plot(x, df[col], linestyle='dashdot', label=col)
    ax1.legend()

    # ax2 = fig.add_subplot(2, 1, 2)
    # for i in _col_list:
    #     ax2.plot(x, df_index[i], label=i)
    # ax2.axhline(y=30, color='black', linestyle='--', label='RSI買い目安')
    # ax2.axhline(y=70, color='black', linestyle='--', label='RSI売り目安')
    # ax2.legend()
    plt.savefig(os.path.join(os.getcwd(), 'img', str(brand[:4])+'.png'))


def plot2(df, col_list, ma_list):
    ma = ma_list[0]
    target_columns = [c + f'_{str(ma)}ma' for c in col_list]
    target_columns.insert(0, col_list[0])
    df = df[target_columns]
    fig, ax = plt.subplots()
    df.plot(ax=ax)

    ax.set_xlabel('Date')
    ax.set_ylabel('Value')

    ax.set_title('test')

    plt.show()
