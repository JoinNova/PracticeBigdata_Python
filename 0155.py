'''
다음은 iris 데이터 세트이다.
주어진 데이터를 이용하여 Species rpart, svm 예측 모형을 만든 후
높은 Accuracy 값을 가지는 모델을 예측 값을 csv파일로 제출하시오.
'''
import pandas as pd
data = 'Iris.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())


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
#print(x_test.head())
print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

submission = pd.DataFrame({'ID':x_test.index, 'predict':pred[:, 1]})

#출력저장
print(submission.head())
submission.to_csv('post02_002_01.csv', index = False)
