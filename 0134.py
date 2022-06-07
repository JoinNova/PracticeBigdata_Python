'''
주어진 데이터는 각 고객이 가입한 서비스와 계정 정보,
인구에 대한 통계 정보들이다. 주어진 훈련데이터를 이용하여
모델을 훈련한 후
테스트 데이터로 고객의 이탈 여부를 예측하고 csv포맷으로 제출하시오.
(단, 이탈:'Yes', 유지 : 'No')
'''
import pandas as pd
data = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
df = pd.read_csv(data)
print(df)
print(df.info())
print(df.describe())

#모델
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

#전처리
x = df.drop(columns = ['customerID', 'Churn'])
xd = pd.get_dummies(x)
y = df['Churn']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

test_preprocessing = pd.get_dummies(x_test)
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_preprocessing = test_preprocessing[x_test.columns]
test_pred = rf.predict_proba(test_preprocessing)

submission = pd.DataFrame({'ID': x_test.index, 'predict' : test_pred[:, 1]})

#출력
print(submission.head())
submission.to_csv('new03_002_01.csv', index = False)
