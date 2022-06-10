'''
다음은 iris 데이터 세트이다.
주어진 데이터를 이용하여 Species rpart, svm 예측 모형을
만든 후 높은 Accuracy 값을 가지는 모델의 예측값을 csv 파일로 제출하시오.
'''
import pandas as pd
data = 'iris.csv'
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
print(len(df))
train = df.head(int(len(df)*0.8))
print(len(train))
test = df.iloc[int(len(df)*0.8):]
print(len(test))
x = train.drop(columns = ['ID', 'Reached.on.Time_Y.N'])
xd = pd.get_dummies(x)
y = train['Reached.on.Time_Y.N']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['ID', 'Reached.on.Time_Y.N']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 1
test_pred = rf.predict_proba(test_preprocessing)
submission = pd.DataFrame({'ID':test.ID, 'predict': test_pred[:, 1]})


#출력&저장
print(submission.head())
submission.to_csv('post02_002_02.csv', index = False)
