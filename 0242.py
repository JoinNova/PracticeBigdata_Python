'''
다음은 iris 데이터 세트이다. 주어진 데이터를 이용하여 Species rpart, svm 예측 모형을 만든 후
높은 Accuracy 값을 가지는 모델의 예측값을 csv 파일로 제출하시오.
'''
import pandas as pd
data = 'Train.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

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
x = df.drop(columns = ['ID', 'Reached.on.Time_Y.N'])
xd = pd.get_dummies(x)
y = df['Reached.on.Time_Y.N']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test rf_roc_score : ', roc_auc_score(y_test, pred[:, 1]))
ada.fit(x_train, y_train)
ada_pred = ada.predict_proba(x_test)
print('test ada_roc_score : ', roc_auc_score(y_test, ada_pred[:, 1]))

rf_submission = pd.DataFrame({'ID':x_test.index, 'predict':pred[:, 1]})
ada_submission = pd.DataFrame({'ID':x_test.index, 'predict':ada_pred[:, 1]})

#출력&저장
print('rf submission file\n', rf_submission.head(7))
rf_submission.to_csv('post02_002_01_rf.csv', index = False)
print('ada submission file\n', ada_submission.head(7))
ada_submission.to_csv('post02_002_01_ada.csv', index = False)
