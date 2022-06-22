'''
데이터 설명 : 이직여부 판단 데이터 (target: 1: 이직 , 0 : 이직 x)
x_train: https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/X_train.csv
y_train: https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/y_train.csv
x_test: https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/X_test.csv
x_label(평가용) : https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/y_test.csv
'''
import pandas as pd
xtr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/X_train.csv'
train = pd.read_csv(xtr_data)
#print(train)
#print(train.info())
#print(train.describe())
#print(train.isnull().sum())
#print(train.shape)
ytr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/y_train.csv'
ytr = pd.read_csv(ytr_data)
#print(ytr)
#print(ytr.info())
#print(ytr.describe())
#print(ytr.isnull().sum())
xte_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/X_test.csv'
test = pd.read_csv(xte_data)
#print(test)
#print(test.info())
#print(test.describe())
#print(test.isnull().sum())
#print(test.shape)

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier()

#전처리
#train.loc[train.gender.isnull(), 'gender'] = train.gender.fillna(method = 'ffill')
#test.loc[test.gender.isnull(), 'gender'] = test.gender.fillna(method = 'ffill')
train = train.fillna('missing')
test = test.fillna('missing')

train = pd.get_dummies(train)
test = pd.get_dummies(test)
train = train.loc[:, (train.columns.isin(test.columns))]
test = test.loc[:, (test.columns.isin(train.columns))]

from sklearn.preprocessing import MinMaxScaler
scaler = ['city_development_index', 'training_hours']
minmax = MinMaxScaler()
minmax.fit(train[scaler])
train[scaler] = minmax.transform(train[scaler])
test[scaler] = minmax.transform(test[scaler])

x = train.drop(columns = ['enrollee_id'])
xd = pd.get_dummies(x)
y = ytr['target']


#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test rf_roc_score : ', roc_auc_score(y_test, pred[:, 1]))

ada.fit(x_train, y_train)
ada_pred = ada.predict_proba(x_test)
print('test ada_roc_score : ', roc_auc_score(y_test, ada_pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['enrollee_id']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict_proba(test_preprocessing)
rf_submission = pd.DataFrame({'enrollee_id':test.enrollee_id,'target':test_pred[:, 1]})

ada_test_pred = ada.predict_proba(test_preprocessing)
ada_submission = pd.DataFrame({'enrollee_id':test.enrollee_id, 'target': ada_test_pred[:, 1]})

#출력&저장
print('rf_submission file\n', rf_submission.head(7))
rf_submission.to_csv('sonyreal02_002_01_rf.csv', index = False)

print('ada_submission file\n', ada_submission.head(7))
ada_submission.to_csv('sonyreal02_002_01_ada.csv', index = False)
