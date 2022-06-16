'''
빅데이터분석기사_2회_작업형_제2유형
https://www.kaggle.com/datasets/tejashvi14/travel-insurance-prediction-data
'''
import pandas as pd
tr_data = 'train003.csv'
train = pd.read_csv(tr_data)
#print(train)
#print(train.info())
#print(train.describe())
#print(train.isnull().sum())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier()
from sklearn.metrics import accuracy_score
#ac = accuracy_score()
from sklearn.metrics import classification_report
#cr = classification_report()

#전처리
x = train.drop(columns = ['Unnamed: 0', 'TravelInsurance'])
xd = pd.get_dummies(x)
y = train['TravelInsurance']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred_rf = rf.predict_proba(x_test)
print('test rf_roc score : ', roc_auc_score(y_test, pred_rf[:, 1]))
submission_rf = pd.DataFrame({'index': x_test.index,'predict': pred_rf[:, 1]})
#print('test rf_accuracy_score : ', accuracy_score(y_test, pred_rf))


ada.fit(x_train, y_train)
pred_ada = ada.predict_proba(x_test)
print('test ada_roc score : ', roc_auc_score(y_test, pred_ada[:, 1]))
submission_ada = pd.DataFrame({'index':x_test.index, 'predict': pred_ada[:, 1]})
#print('test ada_accuracy_score : ', accuracy_score(y_test, pred_ada))

#출력&저장
print('rf_submission file\n', submission_rf.head())
submission_rf.to_csv('post03_002_01_rf.csv', index = False)

print('ada_submission file\n', submission_ada.head())
submission_ada.to_csv('post03_002_01_ada.csv', index = False)
