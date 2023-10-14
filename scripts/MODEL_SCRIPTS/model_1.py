#import libs
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

import pickle
import yaml
import json


# load params
params = yaml.safe_load(open('/home/data_srv_admin/MLOPS_2-part_1/params.yaml'))
split_ratio = params['split']['split_ratio']
alpha = params['alpha']['alpha']
print('split_ratio=', split_ratio)
print('alpha=', alpha)

# load dataset
df = pd.read_csv('/home/data_srv_admin/MLOPS_2-part_1/data/final/stage_fin.csv')

# train-test-split
X = df.drop(['ReadingScore'], axis=1)
y = df.ReadingScore
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_ratio,
                                                          random_state=42)

# create-fit model
model = Ridge(alpha=alpha)
model.fit(X_train, y_train)

# testing model score
score = model.score(X_test, y_test)
print('Model score -->', score)

# Save the model
with open('/home/data_srv_admin/MLOPS_2-part_1/data/final/model_1.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save the metric
metrics = {}
metrics['split_ratio'] = split_ratio
metrics['alpha'] = alpha
metrics['score'] = score
with open('/home/data_srv_admin/MLOPS_2-part_1/score.json', 'w') as f:
    json.dump(metrics, f)