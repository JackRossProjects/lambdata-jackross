# my_lambdata/my_script.py

import my_lambdata.my_mod as my_mod
import pandas as pd
import numpy as np

df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})

print("Original")
print(df.head())

print("NaNs dropped")
my_mod.drop_nans(df)
