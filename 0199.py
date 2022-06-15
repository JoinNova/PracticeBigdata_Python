'''
데이터 출처 : https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset (후처리 작업)
데이터 설명 : 뇌졸증 발생여부 예측
train : https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv
test : https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/test.csv
'''
import pandas as pd
tr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv'
train = pd.read_csv(tr_data)
#print(train)
#print(train.info())
#print(train.describe())
te_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/test.csv'
test = pd.read_csv(te_data)
#print(test)
#print(test.info())
#print(test.describe())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

#전처리
train['age'] = train.age.str.replace('*', '').astype('int')
train.loc[train.bmi.isnull(), 'bmi'] = train.bmi.fillna(train.bmi.mean())
test.loc[test.bmi.isnull(), 'bmi'] = test.bmi.fillna(test.bmi.mean())
x = train.drop(columns = ['id', 'stroke'])
xd = pd.get_dummies(x)
y = train['stroke']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc_score : ', roc_auc_score(y_test, pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['id']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict_proba(test_preprocessing)
submission = pd.DataFrame({'id': test.id,'predict':test_pred[:, 1]})

#출력&저장
print(submission.head())
submission.to_csv('sony02_002_11.csv', index = False)
