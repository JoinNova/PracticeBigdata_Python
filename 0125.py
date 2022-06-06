'''
기업에서 생성된 주문데이터이다. 80009건의 데이터에 대하여
정시도착 가능여부 예측 모델을 만들고, 평가 데이터에 대하여
정시도착 가능여부 예측확률을 기록한csv를 생성하시오.
'''
import pandas as pd
data = 'Train.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())
sub_data = 'submission.csv'
submission = pd.read_csv(sub_data)

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

#전처리
x = df.drop(columns = ['ID', 'Reached.on.Time_Y.N'])
xd = pd.get_dummies(x)
y = df['Reached.on.Time_Y.N']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

test_preprocessing = pd.get_dummies(x_test)
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_predict = rf.predict_proba(test_preprocessing)
submission['presict'] = test_predict[:, 1]

#출력
print('submision file\n', submission.head())
submission.to_csv('New02_002_01.csv', index = False)
