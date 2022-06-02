'''
데이터 설명 : 센서데이터로 동작 유형 분류 (종속변수 pose : 0 ,1 구분)
x_train: https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/x_train.csv
y_train: https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/y_train.csv
x_test: https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/x_test.csv
'''
import pandas as pd
xtr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/x_train.csv'
x_train = pd.read_csv(xtr_data)
#print(x_train.head())
#print(x_train.info())
ytr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/y_train.csv'
y_train = pd.read_csv(ytr_data)
#print(y_train.head())
#print(y_train.info())
xte_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/x_test.csv'
test = pd.read_csv(xte_data)
#print(x_test.head())
#print(x_test.info())

#모듈
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
from sklearn.metrics import roc_auc_score

#전처리
x = x_train.drop(columns = ['ID'])
test_drop = test.drop(columns = ['ID'])
sc.fit(x)
xs = sc.transform(x)
x_test_scaler = sc.transform(test_drop)



#학습
x_train, x_test, y_train, y_test = train_test_split(xs, y_train['pose'], test_size = 0.33, random_state = 42) 
lr.fit(x_train, y_train)

pred = lr.predict_proba(x_test)
print('validation_auc : ', roc_auc_score(y_test, pred[:, 1]))

# # 아래 코드 예측변수와 수험번호를 개인별로 변경하여 활용
pd.DataFrame({'id': test.ID, 'pose': lr.predict_proba(x_test_scaler)[:, 1]}).to_csv('sony03_002_01.csv', index = False)
