# import libs

import pandas as pd


# drops the bads columns

df = pd.read_csv('/home/data_srv_admin/MLOPS_2-part_1/data/raw/Expanded_data_with_more_features.csv')

df = df.drop(df.columns[0], axis=1)

df.to_csv('/home/data_srv_admin/MLOPS_2-part_1/data/raw/stage_0.csv', index=False)