'''
고객의 3,500명에 대한 학습용 데이터를 이용하여 성별예측 모형을 만든 후,
이를 평가용데이터에 적용하여 얻은 2482명 고객의 성별 예측값(남자일 확률)을
다음과 같은 형식의 CSV파일로 생성하시오.
(제출한 모델의 성능은 ROC-AUC 평가지표에 따라 채점)
'''
import pandas as pd
xtr_data = 'X_train_2.csv'
train = pd.read_csv(xtr_data)
#print(train)
#print(train.info())
#print(train.describe())
#print(train.isnull().sum())
ytr_data = 'y_train_2.csv'
ytr = pd.read_csv(ytr_data)
#print(ytr)
#print(ytr.info())
#print(ytr.describe())
#print(ytr.isnull().sum())
xte_data = 'X_test_2.csv'
test = pd.read_csv(xte_data)
#print(test)
#print(test.info())
#print(test.describe())
#print(test.isnull().sum())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
acc = accuracy_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier()
from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()

#전처리
train['환불금액'] = train['환불금액'].fillna(0)
test['환불금액'] = test['환불금액'].fillna(0)

x = train.drop(columns = ['cust_id'])
xd = pd.get_dummies(x)
y = ytr['gender']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test rf_roc_score : ', roc_auc_score(y_test, pred[:, 1]))

ada.fit(x_train, y_train)
pred = ada.predict_proba(x_test)
print('test ada_roc_score : ', roc_auc_score(y_test, pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['cust_id']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict_proba(test_preprocessing)
rf_submission = pd.DataFrame({'custid':test.cust_id, 'gender':test_pred[:, 1]})

ada_test_pred = ada.predict_proba(test_preprocessing)
ada_submission = pd.DataFrame({'cudtid':test.cust_id, 'gender':ada_test_pred[:, 1]})

#출력&저장
print('rf submission file\n', rf_submission.head(7))
rf_submission.to_csv('realtest02_002_22_rf.csv', index = False)
print('ada submission file\n', ada_submission.head(7))
ada_submission.to_csv('realtest02_002_22_ada.csv', index = False)
