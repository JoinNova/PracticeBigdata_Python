'''
데이터 출처 : https://archive.ics.uci.edu/ml/datasets/Bank+Marketing (후처리 작업)
데이터 설명 : 은행의 전화 마케팅에 대해 고객의 반응 여부
dataurl : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv'
df = pd.read_csv(data)
#print(df.head())

#01 마케팅 응답 고객들의 나이를 10살 단위로 변환 했을 때, 가장 많은 인원을 가진 나이대는? (0~9 : 0 , 10~19 : 10)
ans = (df.age//10*10).value_counts().index[0]
#print(ans)

#02 마케팅 응답 고객들의 나이를 10살 단위로 변환 했을 때, 가장 많은 나이대 구간의 인원은 몇명인가?
ans = (df.age//10*10).value_counts().values[0]
#print(ans)

#03 나이가 25살 이상 29살 미만인 응답 고객들중 housing컬럼의 값이 yes인 고객의 수는?
ans = df[(df.age>=25) & (df.age < 29) &(df.housing == 'yes')]
#print(ans.sum())
#print(len(ans))

#04 numeric한 값을 가지지 않은 컬럼들중 unique한 값을 가장 많이 가지는 컬럼은?
chk = 0
from datetime import date
#df['month'] = df['month'].astype(int)
#df['month'] = df['month'].astype(date)
#df['month'] = df['month'].apply(lambda x: x.strftime('%m'))
#print(df['month'])
for _ in df.select_dtypes(include = object):
    if df[_].nunique() >= chk:
        ans = _
        chk = df[_].nunique()
#print(ans, chk)

#05 balance 컬럼값들의 평균값 이상을 가지는 데이터를 ID값을 기준으로 내림차순 정렬했을때 상위 100개 데이터의 balance값의 평균은?
ans = df[df['balance'] >= df.balance.mean()].sort_values('ID', ascending = False).head(100).balance.mean()
#print(ans)

#06 가장 많은 광고를 집행했던 날짜는 언제인가? (데이터 그대로 일(숫자),달(영문)으로 표기)
ans = df[['day', 'month']].value_counts().index[0]
#print(ans)

#07 데이터의 job이 unknown 상태인 고객들의 age 컬럼 값의 정규성을 검정하고자 한다. 샤피로 검정의 p-value값을 구하여라
from scipy.stats import shapiro
ans = shapiro(df[df.job =='unknown'].age)[1]
#print(ans)

#08 age와 balance의 상관계수를 구하여라
ans = df[['age', 'balance']].corr().iloc[0,1]
#print(ans)

#09 y 변수와 education 변수는 독립인지 카이제곱검정을 통해 확인하려한다. p-value값을 출력하라
from scipy.stats import chi2_contingency
ans = pd.crosstab(df.y, df.education)
#print(chi2_contingency(ans)[1])

#10 각 job에 따라 divorced/married 인원의 비율을 확인 했을 때 그 값이 가장 높은 값은?
chk = df.groupby(['job', 'marital']).size().reset_index()
pivotdf = chk.pivot_table(index = 'job', columns = 'marital')[0]
pivotdf = pivotdf.fillna(0)
#print(pivotdf)
pivotdf['ratio'] = pivotdf['divorced'] / pivotdf['married']
ans = pivotdf.sort_values('ratio').ratio.values[-1]
#print(ans)

'''

데이터 출처 : https://archive.ics.uci.edu/ml/datasets/Bank+Marketing (후처리 작업)
데이터 설명 : 은행의 전화 마케팅에 대해 고객의 반응 여부
train : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv
test : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/test.csv
submission : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/submission.csv
'''

import pandas as pd
train= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv')
test= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/test.csv')
submission= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/submission.csv')

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, classification_report

x = train.drop(columns = ['ID', 'y'])
xd = pd.get_dummies(x)
y = train['y']

x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)

rf = RandomForestClassifier()
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)

print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

test_pred = rf.predict_proba(pd.get_dummies(test.drop(columns = ['ID'])))
submission['predict'] = test_pred[:,1]

print('submisson file')
print(submission)
'''
from sklearn.model_selection import train_test_split

x = train.drop(columns =['ID','y'])
xd = pd.get_dummies(x)
y = train['y']

x_train,x_test,y_train,y_test = train_test_split(xd,y,stratify =y ,random_state=1)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(x_train,y_train)
pred = rf.predict_proba(x_test)

from sklearn.metrics import roc_auc_score,classification_report

print('test roc score : ',roc_auc_score(y_test,pred[:,1]))


test_pred = rf.predict_proba(pd.get_dummies(test.drop(columns=['ID'])))
submission['predict'] = test_pred[:,1]

print('submission file')
print(submission.head())
submission.to_csv('00000000000000.csv',index=False)
'''
