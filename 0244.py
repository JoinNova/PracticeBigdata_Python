'''
데이터 출처 : https://archive.ics.uci.edu/ml/datasets/Bank+Marketing (후처리 작업)
데이터 설명 : 은행의 전화 마케팅에 대해 고객의 반응 여부
train : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv
test : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/test.csv
submission : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/submission.csv
'''
import pandas as pd
tr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv'
train = pd.read_csv(tr_data)
#print(train)
#print(train.info())
#print(train.describe())
#print(train.isnull().sum())
te_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/test.csv'
test = pd.read_csv(te_data)
#print(test)
#print(test.info())
#print(test.describe())
#print(test.isnull().sum())
sub_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/submission.csv'
submission = pd.read_csv(sub_data)
#print(submission)
#print(submission.info())
#print(submission.describe())
#print(submission.isnull().sum())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
acc = accuracy_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier()
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

#전처리
rf_submission = submission
ada_submission = submission
scale = ['balance']
scaler.fit(train[scale])
train[scale] = scaler.transform(train[scale])
test[scale] = scaler.transform(test[scale])

x = train.drop(columns = ['ID', 'y'])
xd = pd.get_dummies(x)
y = train['y']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)

rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test rf_roc_score : ', roc_auc_score(y_test, pred[:, 1]))

ada.fit(x_train, y_train)
ada_pred = ada.predict_proba(x_test)
print('test ada_roc_score : ', roc_auc_score(y_test, ada_pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['ID']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict_proba(test_preprocessing)
rf_submission['predict'] = test_pred[:, 1]

ada_test_pred = ada.predict_proba(test_preprocessing)
ada_submission['predict'] = ada_test_pred[:, 1]

#출력&저장
print('rf submission file\n', rf_submission.head(7))
rf_submission.to_csv('sony01_002_20_rf.csv', index = False)
print('ada submission file\n', ada_submission.head(7))
ada_submission.to_csv('sony01_002_20_ada.csv', index = False)
