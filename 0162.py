'''
데이터 설명 : 센서데이터로 동작 유형 분류 (종속변수 pose : 0 ,1 구분)
x_train: https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/x_train.csv
y_train: https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/y_train.csv
x_test: https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/x_test.csv
'''
import pandas as pd
xtr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/x_train.csv'
x_tr = pd.read_csv(xtr_data)
#print(x_tr)
#print(x_tr.info())
#print(x_tr.describe())
ytr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/y_train.csv'
y_tr = pd.read_csv(ytr_data)
#print(y_tr)
#print(y_tr.info())
#print(y_tr.describe())
xte_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/x_test.csv'
x_te = pd.read_csv(xte_data)
#print(x_te)
#print(x_te.info())
#print(x_te.describe())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

#전처리
x = x_tr.drop(columns = ['ID'])
xd = pd.get_dummies(x)
y = y_tr['pose']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

test_preprocessing = pd.get_dummies(x_te.drop(columns = ['ID']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict_proba(test_preprocessing)
submission = pd.DataFrame({'ID':x_te.ID, 'pose' : test_pred[:, 1] })

#출력&저장
print('submission file\n', submission.head())
submission.to_csv('sony03_002_04.csv', index = False)
