'''
작업 2유형
데이터 출처 : https://archive.ics.uci.edu/ml/datasets/Bank+Marketing (후처리 작업)
데이터 설명 : 은행의 전화 마케팅에 대해 고객의 반응 여부
train : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv
test : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/test.csv
submission : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/submission.csv
'''
import pandas as pd
train_dt = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv'
test_dt = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/test.csv'
submission_dt = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/submission.csv'
train = pd.read_csv(train_dt)
#print(train.head())
#print(train.columns)
test = pd.read_csv(test_dt)
#print(test.head())
#print(test.columns)
submission = pd.read_csv(submission_dt)
#print(submission.head())
#print(submission.columns)

#01 모델링 및 submission파일 생성까지
from sklearn.model_selection import train_test_split

x = train.drop(columns = ['ID', 'y'])
xd = pd.get_dummies(x)
y = train['y']

x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)

from sklearn.metrics import roc_auc_score, classification_report

print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

test_pred = rf.predict_proba(pd.get_dummies(test.drop(columns = ['ID'])))
submission['predict'] = test_pred[:, 1]

print('submission file')
print(submission.head())
submission.to_csv('00000000000000.csv', index = False)
