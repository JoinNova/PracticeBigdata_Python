'''
데이터 설명 : 자동차 보험 가입 예측 (종속변수 Response: 1 : 가입 , 0 :미가입)
x_train: https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/x_train.csv
y_train: https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/y_train.csv
x_test: https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/x_test.csv
x_label(평가용) : https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/y_test.csv
데이터 출처 :https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction(참고, 데이터 수정)
'''
import pandas as pd
xtr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/x_train.csv'
train = pd.read_csv(xtr_data)
#print(train)
#print(train.info())
#print(train.describe())
#print(train.isnull().sum())
ytr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/y_train.csv'
ytr = pd.read_csv(ytr_data)
#print(ytr)
#print(ytr.info())
#print(ytr.describe())
#print(ytr.isnull().sum())
te_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/x_test.csv'
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

#전처리
x = train.drop(columns = ['ID', 'id'])
xd = pd.get_dummies(x)
y = ytr['Response']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
accpred = rf.predict(x_test)
print('test roc_score : ', roc_auc_score(y_test, pred[:, 1]))
print('test accuracy_score : ', acc(y_test, accpred))

test_preprocessing = pd.get_dummies(test.drop(columns = ['ID', 'id']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict(test_preprocessing)
submission = pd.DataFrame({'ID':test.ID, '흡연상태':test_pred})

#출력&저장
print('submission file\n', submission.head())
submission.to_csv('sonyreal04_002_01_rf.csv', index = False)
