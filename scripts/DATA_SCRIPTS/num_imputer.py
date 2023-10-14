# import libs

import pandas as pd



def cat_num_split(df: pd.DataFrame) -> tuple:
    '''Ищем категориальные и числовые признаки в датафрейме'''

    cat_columns = []
    num_columns = []

    for column_name in df.columns:
        if (df[column_name].dtypes == object):
            cat_columns +=[column_name]
        else:
            num_columns +=[column_name]

    print('categorical columns:\t ',cat_columns, '\n len = ',len(cat_columns))
    print('numerical columns:\t ',  num_columns, '\n len = ',len(num_columns))

    return cat_columns, num_columns



# fill the NaNs to num columns

df = pd.read_csv('/home/data_srv_admin/MLOPS_2-part_1/data/raw/stage_0.csv')

cat_columns, num_columns = cat_num_split(df)

df[num_columns] = df[num_columns].fillna(df[num_columns].median())

df.to_csv(('/home/data_srv_admin/MLOPS_2-part_1/data/raw/stage_1.csv'))