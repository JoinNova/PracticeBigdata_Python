'''
다음은 고객의 대출 정보인 Loan 데이터 세트이다.
전체 데이터를 7:3으로 훈련 데이터와 테스트 데이터로 분할하고,
테스트 데이터로 고객의 대출상환(loan_status)을 예측하고 csv포맷으로 제출하시오.
'''
import pandas as pd
data = 'Loan_payments_data.csv'
df = pd.read_csv(data)
print(df)
print(df.info())
print(df.describe())

#모듈
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.preprocessing import LabelEncoder
from sklearn.utils.multiclass import type_of_target
encoder = LabelEncoder()
#roc = {label: [] for label in multi_class_series.unique()}
#for label in multi_class_series.unique():
#    selected_classifier.fit(train_set_dataframe, train_class == label)
#    predictions_proba = selected_classifier.predict_proba(test_set_dataframe)
#    roc[label] += roc_auc_score(test_class, predictions_proba[:,1])

#전처리
df['loan_status'] = encoder.fit_transform(df['loan_status'])
df['education'] = encoder.fit_transform(df['education'])
df['Gender'] = encoder.fit_transform(df['Gender'])
df['effective_date'] = encoder.fit_transform(df['effective_date'])
df['due_date'] = encoder.fit_transform(df['due_date'])
df['paid_off_time'] = encoder.fit_transform(df['paid_off_time'])
df['Principal'] = df['Principal'].astype('int')
df['terms'] = df['terms'].astype('int')
#df['past_due_days'] = df['past_due_days'].astype('int')
df['age'] = df['age'].astype('int')

x = df.drop(columns = ['Loan_ID', 'paid_off_time', 'past_due_days', 'loan_status'])
xd = pd.get_dummies(x)
y = df['loan_status']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, test_size = 0.3, random_state = 1)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
#print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))
submission = pd.DataFrame({'Loan_ID': x_test.index, 'loan_status': pred[:, 1]})

#출력&저장
print(submission.head())
submission.to_csv('new02_002_03.csv', index = False)
