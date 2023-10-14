# import libs

import pandas as pd


# One hot encoding

df = pd.read_csv('/home/data_srv_admin/MLOPS_2-part_1/data/raw/stage_2.csv')

df = pd.get_dummies(df)

df.to_csv(('/home/data_srv_admin/MLOPS_2-part_1/data/final/stage_fin.csv'))