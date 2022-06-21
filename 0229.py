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

#전처리
x = train.drop(columns = ['ID', 'y'])
xd = pd.get_dummies(x)
y = train['y']

rf_submission = submission
ada_submission = submission

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('randomforest roc_score : ', roc_auc_score(y_test, pred[:, 1]))

ada.fit(x_train, y_train)
ada_pred = ada.predict_proba(x_test)
print('adaboost roc_score : ', roc_auc_score(y_test, ada_pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['ID']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict(test_preprocessing)
rf_submission['predict'] = test_pred
ada_pred = ada.predict(test_preprocessing)
ada_submission['predict'] = ada_pred

#출력&저장
print('randomforest submission file\n', rf_submission.head(7))
print('adaboost submission file\n', ada_submission.head(7))
rf_submission.to_csv('sony01_002_18_rf.csv', index = False)
ada_submission.to_csv('cony01_002_18_ada.csv', index = False)
