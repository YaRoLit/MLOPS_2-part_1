#import libs
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

import pickle


# load dataset
df = pd.read_csv('/home/data_srv_admin/MLOPS_2-part_1/data/final/stage_fin.csv')

# train-test-split
X = df.drop(['ReadingScore'], axis=1)
y = df.ReadingScore
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33,
                                                          random_state=42)

# create-fit model
model = Ridge(alpha=0.5)
model.fit(X_train, y_train)

# testing model score
print('Model score -->', model.score(X_test, y_test))

# Save the model
with open('/home/data_srv_admin/MLOPS_2-part_1/data/baselines/model_0.pkl', 'wb') as f:
    pickle.dump(model, f)