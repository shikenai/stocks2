import matplotlib.pyplot as plt
import seaborn as sns


def plot1(df, target, ma_list):
    target_columns = [target]
    for ma in ma_list:
        target_columns.append(target+f'_{str(ma)}ma')
    df = df[target_columns]
    # fig, ax = plt.subplots()
    # df.plot(ax=ax)
    #
    # ax.set_xlabel('Date')
    # ax.set_ylabel('Value')
    #
    # ax.set_title('stock prices')

    x = df.index
    plt.plot(x, df[target], label=target)
    for col in target_columns:
        if not col == target:
            plt.plot(x, df[col], linestyle='--', label=col)
    plt.title('Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


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
