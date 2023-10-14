# import libs

import pandas as pd


# fill the NaNs to cat columns

df = pd.read_csv('/home/data_srv_admin/MLOPS_2-part_1/data/raw/stage_1.csv')

df = df.fillna("Unknown")

df.to_csv(('/home/data_srv_admin/MLOPS_2-part_1/data/raw/stage_2.csv'))