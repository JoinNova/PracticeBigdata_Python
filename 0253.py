'''
Churn model data set ( competition form)
Classfication training
source = https://www.kaggle.com/kukuroo3/churn-model-data-set-competition-form
'''
import pandas as pd
tr_data = '001/001_x_train.csv'
train = pd.read_csv(tr_data)
#print(train)
#print(train.info())
#print(train.describe())
#print(train.isnull().sum())
ytr_data = '001/001_y_train.csv'
ytr = pd.read_csv(ytr_data)
#print(ytr)
#print(ytr.info())
#print(ytr.describe())
#print(ytr.isnull().sum())
te_data = '001/001_x_test.csv'
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

#전처리

x = train.drop(columns = ['CustomerId', 'Surname'])
xd = pd.get_dummies(x)
y = ytr['Exited']


#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test rf roc score : ', roc_auc_score(y_test, pred[:, 1]))

ada.fit(x_train, y_train)
ada_pred = ada.predict_proba(x_test)
print('test ada roc score : ', roc_auc_score(y_test, ada_pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['CustomerId', 'Surname']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
rf_test_pred = rf.predict_proba(test_preprocessing)
rf_submission = pd.DataFrame({'CustomerId':test.CustomerId, 'Exited':rf_test_pred[:, 1]})

ada_test_pred = ada.predict_proba(test_preprocessing)
ada_submission = pd.DataFrame({'CustomerId':test.CustomerId, 'Exited':ada_test_pred[:, 1]})

#출력&저장
print('rf submission file \n', rf_submission.head(7))
rf_submission.to_csv('kaggle001_rf.csv', index = False)
print('ada submission file \n', ada_submission.head(7))
ada_submission.to_csv('kaggle001_ada.csv', index = False)
