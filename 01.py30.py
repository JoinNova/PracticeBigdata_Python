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

#sub_data = 'submission.csv'
#submission = pd.read_csv(sub_data)

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

#전처리
#print(train.age.sort_values())
train['age'] = train.age.str.replace('*', '').astype('int')
#print(train.age.sort_values())
#print(train.loc[train.bmi.isnull(), 'bmi'])
#print(train.bmi.mean())
train[train.bmi.isnull()] = train.fillna(train.bmi.mean())
test[test.bmi.isnull()] = test.fillna(test.bmi.mean())
x = train.drop(columns = ['id', 'stroke'])
xd = pd.get_dummies(x)
y = train['stroke']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['id']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_preprocessing = test_preprocessing[x_train.columns]
test_pred = rf.predict_proba(test_preprocessing)


#출력
submission = pd.DataFrame({'id' : test.id, 'stroke' : test_pred[:, 1]})
print(submission.head())
submission.to_csv('sony02_002_08.csv', index = False)
