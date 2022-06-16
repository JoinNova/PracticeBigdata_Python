'''
빅데이터분석기사_2회_작업형_제2유형
https://www.kaggle.com/datasets/prachi13/customer-analytics

'''
import pandas as pd
tr_data = 'train001.csv'
train = pd.read_csv(tr_data)
#print(train)
#print(train.info())
#print(train.describe())
#print(train.isnull().sum())

##모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

#전처리
x = train.drop(columns = ['ID', 'Reached.on.Time_Y.N'])
xd = pd.get_dummies(x)
y = train['Reached.on.Time_Y.N']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

submission = pd.DataFrame({'ID':x_test.index, 'predict': pred[:, 1]})

#출력&저장
print('submission file\n', submission.head())
submission.to_csv('post02_002_04.csv', index = False)
