import pycaret
from pycaret.regression import *
import os
import pandas as pd

def save_test(_df):
    print('test')
    # print(df)
    exp = setup(data=_df, target='target')
    best_model = compare_models()
    print(best_model)
    pd.set_option('display.max_columns', 100)
    df = pd.DataFrame(pull(best_model))
    print(df)