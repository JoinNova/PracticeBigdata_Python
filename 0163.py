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
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor(n_estimators = 1000, criterion = 'mse', random_state = 100)
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
#from sklearn.metrics import confusion_metrix



#전처리
x = x_tr.drop(columns = ['ID'])
xd = pd.get_dummies(x)
y = y_tr['pose']

#학습
x_train, x_test, y_train, y_test =train_test_split(xd, y, test_size = 0.3, random_state = 100)
rfr.fit(x_train, y_train)
y_train_pred = rfr.predict(x_train)
#print(y_train_pred)
y_test_pred = rfr.predict(x_test)
#print(y_test_pred)
r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)

print('R2 - Train: %.2f, Test: %.2f'%(r2_train, r2_test))

testSet = x_test
testSet2 = y_test

prediction = y_test_pred
df_prediction = pd.DataFrame(prediction)
df_prediction = df_prediction.rename(columns = {0:'what_is_this'})

testSet = testSet.reset_index(drop = True)
dataSet2 = testSet2.reset_index(drop = True)
df_prediction = df_prediction.reset_index(drop = True)
df_prediction = pd.concat([testSet, df_prediction], 1)
df_prediction = df_prediction.reset_index(drop = True)
df_prediction = pd.concat([df_prediction, testSet2], 1)
df_prediction = df_prediction.reset_index(drop = True)

print(df_prediction.head())
#출력&저장
