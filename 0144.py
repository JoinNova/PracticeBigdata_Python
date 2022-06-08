'''
다음은 고객의 대출 정보인 Loan 데이터 세트이다.
전체 데이터를 7:3으로 훈련 데이터와 테스트 데이터로 분할하고,
테스트 데이터로 고객의 대출 상환(Loan_status)을 예측하고
csv 포맷으로 제출하시오.
'''
import pandas as pd
data = 'Loan_payments_data.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

from sklearn import preprocessing
le=preprocessing.LabelEncoder()
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()

#전처리
#print(df['loan_status'].unique())
df['loan_status']=le.fit_transform(df['loan_status'])
df['Gender']=le.fit_transform(df['Gender'])
df['education']=le.fit_transform(df['education'])
df['past_due_days']=le.fit_transform(df['past_due_days'])

#data2.drop('effective_date', axis=1, inplace=True)
#data2.drop('due_date', axis=1, inplace=True)
#data2.drop('paid_off_time', axis=1, inplace=True)

x = df.drop(columns = ['Loan_ID', 'effective_date', 'due_date', 'paid_off_time', 'loan_status'])
xd = pd.get_dummies(x)
y = df['loan_status']


#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, test_size = 0.3, random_state = 1)
rf.fit(x_train, y_train)
rfc.fit(x_train, y_train)

#pred = rf.predict_proba(x_test)
#print(pred)
#print('test roc score : ', roc_auc_score(y_test, pred['ovr':, 1]))


#출력
rfc_score_train = rfc.score(x_train, y_train)
print("Training score: ",rfc_score_train)
rfc_score_test = rfc.score(x_test, y_test)
print("Testing score: ",rfc_score_test)
