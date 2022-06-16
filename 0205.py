'''
고객 3,500명에 대한 학습용 데이터(x_train.csv, y_train.csv)를 이용하여
성별 예측 모형을 만든후, 이를 평가용 데이터(x_test.csv)네 적용하여 얻은
2,482명 고객의 성별 예측 값(남자일 확률)을 다음과 같은 형식의 csv 파일로
생성하시오.(제출한 모델의 성능은 roc_auc 평가지표에 따라 채점)
'''
import pandas as pd
xtr_data = 'x_train002.csv'
train = pd.read_csv(xtr_data)
#print(train)
#print(train.info())
#print(train.describe())
#print(train.isnull().sum())
xte_data = 'x_test002.csv'
test = pd.read_csv(xte_data)
#print(test)
#print(test.info())
#print(test.describe())
#print(test.isnull().sum())
ytr_data = 'y_train002.csv'
ytr = pd.read_csv(ytr_data)
#print(ytr)
#print(ytr.info())
#print(ytr.describe())
#print(ytr.isnull().sum())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

#전처리
train.loc[train['환불금액'].isnull(), '환불금액'] = train['환불금액'].fillna(0)
test.loc[test['환불금액'].isnull(), '환불금액'] = test['환불금액'].fillna(0)

x = train.drop(columns = ['cust_id'])
xd = pd.get_dummies(x)
y = ytr['gender']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc_score : ', roc_auc_score(y_test, pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['cust_id']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict_proba(test_preprocessing)
submission = pd.DataFrame({'custid': test_preprocessing.index, 'gender': test_pred[:, 1]})

#출력&저장
print('submission file\n', submission.head())
submission.to_csv('realtest01_002_03.csv', index = False)
