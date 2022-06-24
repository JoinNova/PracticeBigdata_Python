'''
HR data, Predict changing jobs (competition form)
Classification problem
source = https://www.kaggle.com/datasets/kukuroo3/hr-data-predict-change-jobscompetition-form
'''
import pandas as pd
tr_data = '002/002_x_train.csv'
train = pd.read_csv(tr_data)
#print(train)
#print(train.info())
#print(train.describe())
#print(train.isnull().sum())
ytr_data = '002/002_y_train.csv'
ytr = pd.read_csv(ytr_data)
#print(ytr)
#print(ytr.info())
#print(ytr.describe())
#print(ytr.isnull().sum())
te_data = '002/002_x_test.csv'
test = pd.read_csv(te_data)
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
le = LabelEncoder()

#전처리
train = train.drop(columns = ['enrollee_id'])
test_id = test.enrollee_id
test = test.drop(columns = ['enrollee_id'])

train = train.fillna('missing')
tst = test.fillna('missing')

x_dummies = pd.get_dummies(pd.concat([train, test]))
xd = x_dummies[:train.shape[0]]
test_dummies = x_dummies[train.shape[0]:]

y = ytr['target']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test rf roc score : ', roc_auc_score(y_test, pred[:, 1]))

ada.fit(x_train, y_train)
ada_pred = ada.predict_proba(x_test)
print('test ada roc score : ', roc_auc_score(y_test, ada_pred[:, 1]))

#test_preprocessing = pd.get_dummies(test_dummies)
#test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict_proba(test_dummies)
rf_submission = pd.DataFrame({'enrollee_id':test_id, 'target':test_pred[:, 1]})

ada_test_pred = ada.predict_proba(test_dummies)
ada_submission = pd.DataFrame({'enrollee_id':test_id, 'target':ada_test_pred[:, 1]})

#출력&저장
print('rf.submission file \n', rf_submission.head(7))
rf_submission.to_csv('kaggle002_rf.csv', index = False)
print('ada submission file \n', ada_submission.head(7))
ada_submission.to_csv('kaggle002_ada.csv', index = False)
