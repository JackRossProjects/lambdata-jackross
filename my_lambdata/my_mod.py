# my_lambdata/my_mod.py

import pandas as pd
import numpy as np


def drop_nans(dataframe):
    df = dataframe.dropna()
    print(df.head())
