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
#print(train.isnull().sum())
te_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/test.csv'
test = pd.read_csv(te_data)
#print(test)
#print(test.info())
#print(test.describe())
#print(test.isnull().sum())

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
train['age'] = train.age.str.replace('*', '').astype('int')
train.loc[train.bmi.isnull(), 'bmi'] = train.bmi.fillna(train.bmi.median())
test.loc[test.bmi.isnull(), 'bmi'] = test.bmi.fillna(test.bmi.median())

scale = ['hypertension', 'heart_disease', 'avg_glucose_level', 'bmi']
scaler.fit(train[scale])
train[scale] = scaler.transform(train[scale])
test[scale] = scaler.transform(test[scale])

x = train.drop(columns = ['id', 'stroke'])
xd = pd.get_dummies(x)
y = train['stroke']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test rf_roc_score : ', roc_auc_score(y_test, pred[:, 1]))

ada.fit(x_train, y_train)
ada_pred = ada.predict_proba(x_test)
print('test ada_roc_score : ', roc_auc_score(y_test, ada_pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['id']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict_proba(test_preprocessing)
rf_submission = pd.DataFrame({'ID':test.id, 'stroke':test_pred[:, 1]})

ada_test_pred = ada.predict_proba(test_preprocessing)
ada_submission = pd.DataFrame({'ID':test.id, 'stroke':ada_test_pred[:, 1]})

#출력&저장
print('rf submission file\n', rf_submission.head(7))
rf_submission.to_csv('sony02_002_02_rf.csv', index = False)
print('ada submission file\n', ada_submission.head(7))
ada_submission.to_csv('sony02_002_02_ada.csv', index = False)
