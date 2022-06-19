'''
데이터 설명 : 비행탑승 경험 만족도 (satisfaction 컬럼 : ‘neutral or dissatisfied’ or satisfied ) (83123, 24) shape
x_train: https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_train.csv
y_train: https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/y_train.csv
x_test: https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_test.csv
x_label(평가용) : https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/y_test.csv
'''
import pandas as pd
xtr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_train.csv'
train = pd.read_csv(xtr_data)
#print(train)
#print(train.info())
#print(train.describe())
#print(train.isnull().sum())
ytr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/y_train.csv'
ytr = pd.read_csv(ytr_data)
#print(ytr)
#print(ytr.info())
#print(ytr.describe())
#print(ytr.isnull().sum())
xte_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_test.csv'
test = pd.read_csv(xte_data)
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

#전처리
#print(train.loc[train['Arrival Delay in Minutes'].isnull(),'Arrival Delay in Minutes'])
train.loc[train['Arrival Delay in Minutes'].isnull(),'Arrival Delay in Minutes'] = train['Arrival Delay in Minutes'].fillna(train['Arrival Delay in Minutes'].median())
test.loc[test['Arrival Delay in Minutes'].isnull(),'Arrival Delay in Minutes'] = test['Arrival Delay in Minutes'].fillna(test['Arrival Delay in Minutes'].median())

x = train.drop(columns = ['ID', 'id'])
xd = pd.get_dummies(x)
y = ytr['satisfaction']


#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc_score : ', roc_auc_score(y_test, pred[:, 1]))
acc_pred = rf.predict(x_test)
print('test accuracy score : ', acc(y_test, acc_pred))

test_preprocessing = pd.get_dummies(test.drop(columns = ['ID', 'id']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict(test_preprocessing)
submission = pd.DataFrame({'ID':test.ID, 'satisfaction':test_pred})

#출력&저장
print('submission file\n', submission.head(10))
submission.to_csv('sonyreal05_002_01.csv', index = False)
