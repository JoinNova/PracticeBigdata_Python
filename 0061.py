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
for _ in df.select_dtypes(include = object).columns:
    if df[_].nunique() >= chk:
        chk = df[_].nunique()
        ans.append(_)
print(ans)

#05 balance 컬럼값들의 평균값 이상을 가지는 데이터를 ID값을 기준으로 내림차순 정렬했을때 상위 100개 데이터의 balance값의 평균은?
ans = df[df.balance >= df.balance.mean()]
print(ans.sort_values('ID', ascending = False).head(100).balance.mean())

#06 가장 많은 광고를 집행했던 날짜는 언제인가? (데이터 그대로 일(숫자),달(영문)으로 표기)
ans = df[['day','month']].value_counts().index[0]
print(ans)

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
pivotdf = chk.pivot_table(index = 'job', columns = 'marital')[0].fillna(0)
pivotdf['ratio'] = pivotdf['divorced'] / pivotdf['married']
print(pivotdf.ratio.max())
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
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import seaborn as sns

pd.set_option("display.max_columns", None)
df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv", sep = ",", skipinitialspace = True)
#print(df.head())
#print(df.tail())
#print(df.info())
rows = df.shape[0]
cols = df.shape[1]
#print("Before cleaning, there are " + str(rows) + " rows and " + str(cols) + " columns in this dataframe.")
dupRows = df.duplicated().sum()
#print("There are " + str(dupRows) + " duplicated rows in the dataframe.")
df = df.drop_duplicates()
dupRows = df.duplicated().sum()
#print("After pre-cleaning, there are " + str(dupRows) + " duplicated rows in the dataframe.")
#print(df.isnull().sum())
#print(df.nunique())
#print(df.memory_usage())
#print(df.describe())
plt.figure(figsize = (16, 16))
plt.title("Age Distribution", fontsize = 20)
plt.xlabel("Age", fontsize = 16)
plt.ylabel("Number of occurences", fontsize = 16)
sns.histplot(df["age"], color = "gold")
#plt.show()

plt.figure(figsize = (16, 16))
plt.title("Boxplot Age", fontsize = 20)
sns.boxplot(data = df["age"], color = "gold")
#plt.show()

#print(df.corr())

#cmap = sns.diverging_palette(100, 200, s = 40, l = 65, n = 9)
corrmat = df.corr()
plt.subplots(figsize = (22, 22))
sns.heatmap(corrmat,cmap = "cividis",annot = True, square = True, cbar_kws = {'label': 'Correlation Value', 'orientation': 'horizontal'});
#plt.show()

df = df.replace("no", 0)
df = df.replace("yes", 1)

ycorr = df.corr()["y"]
ycorr = pd.DataFrame(ycorr)
#print(ycorr)

#matplotlib inline

plt.figure(figsize = (16, 12))
plt.title("Correlations between input columns and target column 'y'", fontsize = 20)
plt.xlabel("Columns", fontsize = 16)
plt.ylabel("Correlation factor", fontsize = 16)
plt.plot(ycorr, color = "gold", linestyle = "", marker = "o")
#plt.show()

plt.figure(figsize = (26, 18))
plt.xlabel("Age", fontsize = 16)
plt.ylabel("Count", fontsize = 16)
age = sns.countplot(x = df["age"], hue = df["y"], palette = "YlOrBr")
age.set_title("Distribution Of Age regarding the campaign success", color = "black", fontsize = 20)
#plt.show()

plt.figure(figsize = (18, 12))
sns.kdeplot(x = df["age"], y = df["pdays"], hue = df["y"], palette = "YlOrBr")
#plt.show()

sns.pairplot(df, palette = "flag")
#plt.show()


#print(df.head())
#print(pd.crosstab(df["age"], df["y"]))

ct = pd.crosstab(df["age"], df["y"]) 

plt.figure(figsize = (18, 18))
plt.title("Crosstab showing how many successful campaigns were managed at what age levels", fontsize = 20)
sns.heatmap(ct, cmap = "YlOrBr", annot = True, cbar = True, fmt = "g")
#plt.show()

#print(pd.crosstab(df["marital"], df["y"]))

ct = pd.crosstab(df["age"], df["y"]) 

plt.figure(figsize = (18, 18))
plt.title("Crosstab showing how many successful campaigns were managed at what marital states", fontsize = 20)
sns.heatmap(ct, cmap = "cool", annot = True, cbar = True, fmt = "g")
#AxesSubplot:title={'center':'Crosstab showing how many successful campaigns were managed at what marital states'}, xlabel='y', ylabel='age'
#plt.show()

#print(pd.crosstab(df["education"], df["y"]))

ct = pd.crosstab(df["education"], df["y"]) 

plt.figure(figsize = (18, 18))
plt.title("Crosstab showing how many successful campaigns were managed at what education levels", fontsize = 20)
sns.heatmap(ct, cmap = "cubehelix", annot = True, cbar = True, fmt = "g")
#AxesSubplot:title={'center':'Crosstab showing how many successful campaigns were managed at what education levels'}, xlabel='y', ylabel='education'
#plt.show()


###
###
'''
import pandas_profiling
from pandas_profiling import ProfileReport

profile = ProfileReport(df, title = "Pandas Profiling Report", explorative = True)

profile.to_widgets()
'''

#print(df.columns)
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

from sklearn.model_selection import validation_curve
from sklearn.tree import DecisionTreeClassifier
import numpy as np

param_range = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

train_scores, test_scores = validation_curve(DecisionTreeClassifier(), X_train, y_train, param_name = "max_depth", param_range = param_range)

#matplotlib inline
import matplotlib.pyplot as plt

plt.figure(figsize = (16, 12))

plt.plot(param_range, np.mean(train_scores, axis = 1))
plt.plot(param_range, np.mean(test_scores, axis = 1))

plt.title("How does the tree depth influence the accuracy?", fontsize = 20)
plt.xlabel("depth levels of model", fontsize = 15)
plt.ylabel("model accuracy", fontsize = 15)

# Adding a legend
plt.legend(["train", "test"], loc = "upper left", fontsize = 12)

#plt.show()

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

from sklearn.model_selection import learning_curve
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import shuffle

X_train, y_train = shuffle(X_train, y_train)

import numpy as np

train_sizes_abs, train_scores, test_scores = learning_curve(KNeighborsClassifier(), X_train, y_train)

#matplotlib inline
import matplotlib.pyplot as plt

plt.figure(figsize = (16, 12))

plt.plot(train_sizes_abs, np.mean(train_scores, axis = 1))
plt.plot(train_sizes_abs, np.mean(test_scores, axis = 1))

plt.title("Learning Curve KNN", fontsize = 20)
plt.xlabel("Number of neighbors", fontsize = 15)
plt.ylabel("Model Accuracy", fontsize = 15)

# Adding a legend
plt.legend(["train", "test"], loc = "upper right", fontsize = 12)

plt.show()
