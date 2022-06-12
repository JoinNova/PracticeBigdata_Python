'''
데이터 설명 : 이직여부 판단 데이터
train: https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/X_train.csv
test : https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/y_train.csv
'''
import pandas as pd
xtr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/X_train.csv'
x_tra = pd.read_csv(xtr_data)
#print(x_train)
#print(x_train.info())
#print(x_train.describe())
ytr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/y_train.csv'
y_tra = pd.read_csv(ytr_data)
#print(y_train)
#print(y_train.info())
#print(y_train.describe())

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
rf = RandomForestClassifier()

x = x_tra#.drop(columns = ['enrollee_id'])
xd = pd.get_dummies(x)
y = y_tra['target']

x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

submission = pd.DataFrame({'enrollee_id': x_test.enrollee_id, 'predic': pred[:, 1]})
print(submission.head())
submission.to_csv('sonysklearn_002_01.csv', index = False)
