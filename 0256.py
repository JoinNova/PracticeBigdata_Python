'''
Bank marketing response predict
binary classification practice
soource = https://www.kaggle.com/datasets/kukuroo3/bank-marketing-response-predict
'''
import pandas as pd
tr_data = '004/train.csv'
train = pd.read_csv(tr_data)
#print(train)
#print(train.info())
#print(train.describe())
#print(train.isnull().sum())
te_data = '004/test.csv'
test = pd.read_csv(te_data)
#print(test)
#print(test.info())
#print(test.describe())
#print(test.isnull().sum())
sub_data = '004/submission.csv'
submission = pd.read_csv(sub_data)
#print(submission)
#print(submission.info())
#print(submission.describe())
#print(submission.isnull().sum())

#모델
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier()

#전처리
rf_submission = submission
ada_submission = submission

ytr = train['y']
train = train.drop(columns = ['ID', 'y'])
test_id = test.ID
test = test.drop(columns = ['ID'])

dummies = pd.get_dummies(pd.concat([train, test]))
xd = dummies[:train.shape[0]]
td = dummies[train.shape[0]:]

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, ytr, stratify = ytr, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test rf roc score : ', roc_auc_score(y_test, pred[:, 1]))

ada.fit(x_train, y_train)
ada_pred = ada.predict_proba(x_test)
print('test ada roc_score : ', roc_auc_score(y_test, ada_pred[:, 1]))

test_rf_pred = rf.predict_proba(td)
rf_submission['predict'] = test_rf_pred[:, 1]

test_ada_pred = ada.predict_proba(td)
ada_submission['predict'] = test_ada_pred[:, 1]

#출력&저장
print('rf submission file \n', rf_submission.head(7))
rf_submission.to_csv('kaggle004_rf.csv', index = False)
print('ada submission file \n', ada_submission.head(7))
ada_submission.to_csv('kaggle004_ada.csv', index = False)
