'''
데이터 출처 : https://archive.ics.uci.edu/ml/datasets/Bank+Marketing (후처리 작업)
데이터 설명 : 은행의 전화 마케팅에 대해 고객의 반응 여부
dataurl : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv
'''
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv'
df = pd.read_csv(data)
#print(df.head())
#print(df.info())
#01 마케팅 응답 고객들의 나이를 10살 단위로 변환 했을 때, 가장 많은 인원을 가진 나이대는? (0~9 : 0 , 10~19 : 10)
ans = df.age//10*10
print(ans.value_counts().index[0])

#02 마케팅 응답 고객들의 나이를 10살 단위로 변환 했을 때, 가장 많은 나이대 구간의 인원은 몇명인가?
print(ans.value_counts().values[0])

#03 나이가 25살 이상 29살 미만인 응답 고객들중 housing컬럼의 값이 yes인 고객의 수는?
ans = df[(df.age >= 25) & (df.age < 29) & (df.housing == 'yes')]
print(len(ans))

#04 numeric한 값을 가지지 않은 컬럼들중 unique한 값을 가장 많이 가지는 컬럼은?
chk, ans = 0, []
for _ in df.select_dtypes(include = object):
    if chk <= df[_].nunique():
        chk = df[_].nunique()
        ans.append(_)
print(ans)

#05 balance 컬럼값들의 평균값 이상을 가지는 데이터를 ID값을 기준으로 내림차순 정렬했을때 상위 100개 데이터의 balance값의 평균은?
ans = df[(df.balance >= df.balance.mean())].sort_values('ID', ascending = False)
print(ans.head(100).balance.mean())

#06 가장 많은 광고를 집행했던 날짜는 언제인가? (데이터 그대로 일(숫자),달(영문)으로 표기)
ans = df[['day', 'month']].value_counts()
print(ans.index[0])

#07 데이터의 job이 unknown 상태인 고객들의 age 컬럼 값의 정규성을 검정하고자 한다. 샤피로 검정의 p-value값을 구하여라
from scipy.stats import shapiro
ans = shapiro(df[df.job == 'unknown'].age)
print(ans[1])

#08 age와 balance의 상관계수를 구하여라
ans = df[['age', 'balance']].corr()
print(ans.iloc[0,1])

#09 y 변수와 education 변수는 독립인지 카이제곱검정을 통해 확인하려한다. p-value값을 출력하라
from scipy.stats import chi2_contingency
chk = pd.crosstab(df.y, df.education)
ans = chi2_contingency(chk)
print(ans[1])

#10 각 job에 따라 divorced/married 인원의 비율을 확인 했을 때 그 값이 가장 높은 값은?
chk = df.groupby(['job', 'marital']).size().reset_index()
pivotdf = chk.pivot_table(index = 'job', columns = 'marital')[0]
pivotdf['ratio'] = pivotdf.divorced/pivotdf.married
print(pivotdf['ratio'].max())
'''
'''
데이터 출처 : https://archive.ics.uci.edu/ml/datasets/Bank+Marketing (후처리 작업)
데이터 설명 : 은행의 전화 마케팅에 대해 고객의 반응 여부
train : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv
test : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/test.csv
submission : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/submission.csv
'''
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
#import seaborn as sns

train = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv')
test = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/test.csv')
submission = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/submission.csv')
pd.set_option("display.max_columns", None)
#print(train.head(3))
rows = train.shape[0]
cols = train.shape[1]
dupRows = train.duplicated().sum()
#print(dupRows)
train = train.replace("no", 0)
train = train.replace("yes", 1)

ycorr = train.corr()["y"]
ycorr = pd.DataFrame(ycorr)
#print(ycorr)
df = train

df["job"] = df["job"].astype(str)
df["marital"] = df["marital"].astype(str)
df["education"] = df["education"].astype(str)
df["default"] = df["default"].astype(str)
df["contact"] = df["contact"].astype(str)
df["month"] = df["month"].astype(str)
df["day"] = df["day"].astype(str)
df["poutcome"] = df["poutcome"].astype(str)
df["housing"] = df["housing"].astype(str)
df["loan"] = df["loan"].astype(str)
#print(df.head())

from sklearn import preprocessing

number = preprocessing.LabelEncoder()

df["job"] = number.fit_transform(df["job"])
df["marital"] = number.fit_transform(df["marital"])
df["education"] = number.fit_transform(df["education"])
df["default"] = number.fit_transform(df["default"])
df["contact"] = number.fit_transform(df["contact"])
df["month"] = number.fit_transform(df["month"])
df["day"] = number.fit_transform(df["day"])
df["poutcome"] = number.fit_transform(df["poutcome"])
df["housing"] = number.fit_transform(df["housing"])
df["loan"] = number.fit_transform(df["loan"])

#print(df.head())

#LOGISTIC REGRESSION
from sklearn.model_selection import train_test_split

X = df.drop(["y"], axis = 1)
y = df["y"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.15)
#print(X_train, X_test, y_train, y_test)
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver = "saga", max_iter = 10000)
model.fit(X_train, y_train)

print('LOGISTIC REGRESSION : ', model.score(X_test, y_test))

#RANDOM FOREST
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(criterion = "entropy")
model.fit(X_train, y_train)

print('RANDOM FOREST : ', model.score(X_test, y_test))

#DECISION TREE
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(criterion = "entropy")
model.fit(X_train, y_train)

print('DECISION TREE : ', model.score(X_test, y_test))

#SVM WITH RBF-KERNEL
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.svm import SVC

model = SVC(kernel = "rbf", gamma = 0.01, C = 5)
model.fit(X_train, y_train)

print('SVM WITH RBF-KERNEL : ', model.score(X_test, y_test))

#GAUSSIAN NAIVE BAYES
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X_train, y_train)

print('GAUSSIAN NAIVE BAYES : ', model.score(X_test, y_test))

#KNN
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors = 18)
model.fit(X_train, y_train)

print('KNN : ', model.score(X_test, y_test))
