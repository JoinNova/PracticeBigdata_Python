'''
데이터 출처 : https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset (후처리 작업)
데이터 설명 : 뇌졸증 발생여부 예측
train : https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv
test : https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/test.csv
'''
import pandas as pd
tr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv'
train = pd.read_csv(tr_data)
#print(train.head())
#print(train.info())
te_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/test.csv'
test = pd.read_csv(te_data)
#print(test.head())
#print(test.info())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.metrics import roc_auc_score

#전처리
train.age.str.replace('*', '').astype('int64')
train['bmi'] = train['bmi'].fillna(train.bmi.mean())
test['bmi'] = test['bmi'].fillna(test.bmi.mean())
x = train.drop(columns = ['id', 'stroke'])
xd = pd.get_dummies(x)
y = train['stroke']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

# one-hot encoding시 train셋에만 존재하는 컬럼이 존재

test_preprocessing = pd.get_dummies(test.drop(columns = ['id']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_preprocessing = test_preprocessing[x_train.columns]
test_pred = rf.predict_proba(test_preprocessing)

# 아래 코드 예측변수와 수험번호를 개인별로 변경하여 활용
pd.DataFrame({'id' : test.id, 'stroke' : test_pred[:, 1]}).to_csv('sony02_002_03.csv', index = False)
