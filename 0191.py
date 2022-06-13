'''
데이터 설명 : 비행탑승 경험 만족도
x_train: https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_train.csv
x_test: https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_test.csv
'''
import pandas as pd
tr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_train.csv'
train = pd.read_csv(tr_data)
#print(train)
#print(train.info())
#print(train.describe())
te_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_test.csv'
test = pd.read_csv(te_data)
#print(test)
#print(test.info())
#print(test.describe())

#01 train 데이터의 Flight Distance 컬럼을 사이킷런 모듈을 이용하여
#최솟값을 0 최댓값을 1값로 하는 데이터로 변환하고 scaling을 이름으로 하는 컬럼으로 데이터프레임에 추가하라
from sklearn.preprocessing import MinMaxScaler

mm = MinMaxScaler()
mm.fit(train['Flight Distance'].values.reshape(-1,1))

scalingdata = mm.transform(train['Flight Distance'].values.reshape(-1,1))
train['scaling'] = scalingdata

##결과 시각화
import matplotlib.pyplot as plt
fig , ax = plt.subplots(1,2)
ax[0].boxplot(train['Flight Distance'])
ax[0].set_xticks([1])
ax[0].set_xticklabels(['Raw'])
ax[1].boxplot(scalingdata)
ax[1].set_xticks([1])
ax[1].set_xticklabels(['Scaling data'])
#plt.show()

# 분포는 바뀌지 않는다

#02 train 데이터의 Flight Distance 컬럼을 pandas의 내장함수만을 이용하여
#최솟값을 0 최댓값을 1값로 하는 데이터로 변환하고
#scaling을 이름으로 하는 컬럼으로 데이터프레임에 추가하라
scaling = (train['Flight Distance'] - train['Flight Distance'].min()) /(train['Flight Distance'].max() - train['Flight Distance'].min())
train['scaling'] = scaling


##결과 시각화
import matplotlib.pyplot as plt
fig , ax = plt.subplots(1,2)
ax[0].boxplot(train['Flight Distance'])
ax[0].set_xticks([1])
ax[0].set_xticklabels(['Raw'])
ax[1].boxplot(scalingdata)
ax[1].set_xticks([1])
ax[1].set_xticklabels(['Scaling data'])
plt.show()

# 분포는 바뀌지 않는다

#03 train 데이터의 Age컬럼을 MinMax 스케일링 진행 하고
#age_scaling컬럼에 추가하고 train셋과 같은 기준으로
#test데이터의 Age를 스케일링하여 age_scaling에 추가하라
from sklearn.preprocessing import MinMaxScaler

mm = MinMaxScaler()
mm.fit(train['Age'].values.reshape(-1,1))

train['age_scaling'] = mm.transform(train['Age'].values.reshape(-1,1))
test['age_scaling'] = mm.transform(test['Age'].values.reshape(-1,1))

print(test[['ID','age_scaling']].head(3))

## 짧게 쓴다면 아래와 같이 쓸수도 있다
# mm = MinMaxScaler()
# train['age_scaling'] = mm.fit_transform(train['Age'].values.reshape(-1,1))
# test['age_scaling'] = mm.transform(test['Age'].values.reshape(-1,1))
