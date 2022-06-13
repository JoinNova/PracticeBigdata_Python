'''
데이터 설명 : 이직여부 판단 데이터
train: https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/X_train.csv
test : https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/y_train.csv
'''
import pandas as pd
xtr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/X_train.csv'
x_tr = pd.read_csv(xtr_data)
#print(x_tr)
#print(x_tr.info())
#print(x_tr.describe())
ytr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/y_train.csv'
y_tr = pd.read_csv(ytr_data)
#print(y_tr)
#print(y_tr.info())
#print(y_tr.describe())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

#전처리
x = x_tr.drop(columns = ['enrollee_id'])
xd = pd.get_dummies(x)
y = y_tr['target']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

submission = pd.DataFrame({'enrollee_id': x_test.index,'predict': pred[:, 1]})

#출력&저장
print('submision file\n', submission.head())
submission.to_csv('sony_sklearn_001.csv', index = False)
