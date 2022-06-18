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
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder

#전처리
x = train.drop(columns = ['CustomerId', 'Surname'])
xd = pd.get_dummies(x)
y = ytr['Exited']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['CustomerId', 'Surname']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict_proba(test_preprocessing)
submission = pd.DataFrame({'CustomerId':test.CustomerId,'Exited_predict': test_pred[:, 1]})
exited_pred = rf.predict(test_preprocessing)
exited_submission = pd.DataFrame({'CustomerId':test.CustomerId,'Exited': exited_pred})

#출력&저장
print('submission file\n', submission.head())
submission.to_csv('sonyreal01_002_01.csv', index = False)

print('exited_submission file\n', exited_submission.head())
submission.to_csv('sonyreal01_002_01_exited.csv', index = False)
