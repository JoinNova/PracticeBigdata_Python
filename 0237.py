'''
데이터 설명 : 고객의 신상정보 데이터를 통한 회사 서비스 이탈 예측 (종속변수 : Exited)
x_train : https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/X_train.csv
y_train : https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/y_train.csv
x_test : https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/X_test.csv
x_label(평가용) : https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/y_test.csv
'''
import pandas as pd
xtr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/X_train.csv'
train = pd.read_csv(xtr_data)
#print(train)
#print(train.info())
#print(train.describe())
#print(train.isnull().sum())
ytr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/y_train.csv'
ytr = pd.read_csv(ytr_data)
#print(ytr)
#print(ytr.info())
#print(ytr.describe())
#print(ytr.isnull().sum())
xte_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/X_test.csv'
test = pd.read_csv(xte_data)
#print(test)
#print(test.info())
#print(test.describe())
#print(test.isnull().sum())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier()

#전처리
train['Gender'] = train.Gender.str.lower()
train['Gender'] = train.Gender.str.replace(' ', '')
test['Gender'] = test.Gender.str.lower()
test['Gender'] = test.Gender.str.replace(' ', '')

x = train.drop(columns = ['CustomerId', 'Surname'])
xd = pd.get_dummies(x)
y = ytr['Exited']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test rf_roc_score : ', roc_auc_score(y_test, pred[:, 1]))
ada.fit(x_train, y_train)
ada_pred = ada.predict_proba(x_test)
print('test ada_roc_score : ', roc_auc_score(y_test, ada_pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['CustomerId', 'Surname']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
rf_test_pred = rf.predict(test_preprocessing)
rf_submission = pd.DataFrame({'CustomerId':test.CustomerId, 'Exited':rf_test_pred})

ada_test_pred = ada.predict(test_preprocessing)
ada_submission = pd.DataFrame({'CustomerId':test.CustomerId, 'Exited':ada_test_pred})

#출력&저장
print('rf submission file\n', rf_submission.head(7))
rf_submission.to_csv('sonyreal01_002_01_rf.csv', index = False)

print('ada submission file\n', ada_submission.head(7))
ada_submission.to_csv('sonyreal01_002_01_ada.csv', index = False)
