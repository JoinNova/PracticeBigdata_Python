import statsmodels
#help(statsmodels)
'''
statsmodels
│
├── 01 사후분석
│   │
│   └──stats
│       └── multicomp
│           ├── MultiComparison
│           │   └── allpairtest
│           └── pairwise_tukeyhsd
│
├── 02 시계열분석
│   │
│   ├── graphics.tsaplots
│   │   ├── plot_acf
│   │   └── plot_pacf
│   └── tsa
│       ├── arima_model
│       │   └── ARIMA
│       └── statesplace.sarimax
│           └── SARIMAX
│
├── 03 ANOVA (scipy모듈과 함께써야 모두 커버가능, 이분산 anova의 경우 pingouin모듈의 welch_anova를 사용)
│   │
│   ├── 다원분산분석 or 이원분산분석
│   └── 일원분산분석
│       └── stats.anova
│           └── anova_lm
│
└── 04 휘귀분석
    │
    └── formula.api
        └── ols

세 집단 이상 검정 (independent)
정규성(scipy.stats.shapiro), 등분산(scipy.stats.levene) 검정의 결과에 따라 시행하는 검정이 다르다
정규성 만족, 등분산 만족 : one-way anova
정규성 만족, 등분산 불만족 : welch’s anova
정규성 불만족 : kruskal-wallis H test
'''

#01 x1,x2,x3의 변수들의 평균의 차이가 존재하는지 검정하라., 차이가 존재한다면 사후 분석까지 진행하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/anova.csv')

data = df.x1
data2 = df.x2
data3 = df.x3

fig,ax = plt.subplots(1,2,figsize=(12,4))
ax[0].hist(data,alpha=0.3,bins=30,label='x1')
ax[0].hist(data2,alpha=0.3,bins=30,label='x2')
ax[0].hist(data3,alpha=0.3,bins=30,label='x3')
ax[0].legend()
labels = ['x1', 'x2', 'x3']
lst =[data,data2,data3]
ax[1].boxplot(lst, labels=labels) 
plt.show()


from scipy.stats import shapiro

# 정규성 검정 -> 모두 정규성을 가짐
print(shapiro(data))
print(shapiro(data2))
print(shapiro(data3))

from scipy.stats import levene

# 등분산 만족한다
print(levene(data,data2,data3))
print()

# anova 방법 1 
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
dfm =df.melt()
dfm.head()
model = ols('value ~ C(variable)', dfm).fit()
print(anova_lm(model))
print()

# anova 방법 2 (scipy.stats.f_oneway)
from scipy.stats import f_oneway 
print(f_oneway(data, data2, data3))


# p-value 는 4.9e-86이므로 3그룹중 어느 두 그룹은 평균이 동일하다고 볼수 없다

#사후검정 방법 1 투키의 HSD
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 유의수준 5%기준으로 도표상의 reject을 보면 group간에 모든 귀무가설(두 그룹의 평균은 같다)을 기각 하는 것을 볼수 있다
posthoc = pairwise_tukeyhsd(dfm.value, dfm.variable, alpha=0.05)
print(posthoc)

# 시각화 y축은 각 label이다. 겹치는 구간이 없으므로 차이가 존재함을 알수 있음
fig = posthoc.plot_simultaneous()
plt.show()


# 사후 검정 방법 2 봉페로니 교정
from statsmodels.sandbox.stats.multicomp import MultiComparison
import scipy.stats

comp = MultiComparison(dfm.value, dfm.variable)
result = comp.allpairtest(scipy.stats.ttest_ind, method='bonf')
print(result[0])


#02 x1,x2,x3의 변수들의 평균의 차이가 존재하는지 검정하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/anova2.csv')

data = df.x1
data2 = df.x2
data3 = df.x3

fig,ax = plt.subplots(1,2,figsize=(12,4))
ax[0].hist(data,alpha=0.3,bins=30,label='x1')
ax[0].hist(data2,alpha=0.3,bins=30,label='x2')
ax[0].hist(data3,alpha=0.3,bins=30,label='x3')
ax[0].legend()
labels = ['x1', 'x2', 'x3']
lst =[data,data2,data3]
ax[1].boxplot(lst, labels=labels) 
plt.show()


from scipy.stats import shapiro

# 정규성 검정 -> 모두 정규성을 가짐
print(shapiro(data))
print(shapiro(data2))
print(shapiro(data3))

from scipy.stats import levene

# 등분산 만족한다
print(levene(data,data2,data3))
print()

# anova 방법 1 
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
dfm =df.melt()
dfm.head()
model = ols('value ~ C(variable)', dfm).fit()
print(anova_lm(model))
print()

# anova 방법 2 (scipy.stats.f_oneway)
from scipy.stats import f_oneway 
print(f_oneway(data, data2, data3))

# p-value 는 0.09이므로 귀무가설을 기각할 수 없다. 3그룹은 평균이 동일하다고 볼 수 있다.

#03 target 변수들에 의해 value값들의 평균의 차이가 존재하는지 검정하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/anova8.csv')

data = df[df.target=='a'].value
data2 = df[df.target=='b'].value
data3 = df[df.target=='c'].value

fig,ax = plt.subplots(1,2,figsize=(12,4))
ax[0].hist(data,alpha=0.3,bins=30,label='a')
ax[0].hist(data2,alpha=0.3,bins=30,label='b')
ax[0].hist(data3,alpha=0.3,bins=30,label='c')
ax[0].legend()
labels = ['a', 'b', 'c']
lst =[data,data2,data3]
ax[1].boxplot(lst, labels=labels) 
plt.show()

from scipy.stats import shapiro

# 정규성 검정 -> 하나의 변수가 정규성을 가지지 않는다. -> 비모수 검정인 kruskal 검정을 사용해야한다
print(shapiro(data))
print(shapiro(data2))
print(shapiro(data3))

from scipy.stats import levene

# 등분산 만족한다
print(levene(data,data2,data3))
print()

# anova
from scipy.stats import f_oneway  ,kruskal
print(f_oneway(data, data2, data3))
print(kruskal(data, data2, data3))

# 비교를 위해 f_oneway 와 kruskal 모두 시행했다.
# kruskal의 경우 평균의 차이가 존재, f_oneway의 경우 차이가 존재하지 않는다


#04 target 변수들에 의해 value값들의 평균의 차이가 존재하는지 검정하라

import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/anova10.csv')

data = df[df.target=='a'].value
data2 = df[df.target=='b'].value
data3 = df[df.target=='c'].value

fig,ax = plt.subplots(1,2,figsize=(12,4))
ax[0].hist(data,alpha=0.3,bins=30,label='a')
ax[0].hist(data2,alpha=0.3,bins=30,label='b')
ax[0].hist(data3,alpha=0.3,bins=30,label='c')
ax[0].legend()
labels = ['a', 'b', 'c']
lst =[data,data2,data3]
ax[1].boxplot(lst, labels=labels) 
plt.show()


from scipy.stats import shapiro

# 정규성 검정 -> 정규성 가짐
print(shapiro(data))
print(shapiro(data2))
print(shapiro(data3))

from scipy.stats import levene

# 등분산 만족하지 않음 -> welch test를 진행해야한다 (pingouin.welch_anova)
print(levene(data,data2,data3))
print()

# anova
from scipy.stats import f_oneway  ,kruskal
print(f_oneway(data, data2, data3))
print(kruskal(data, data2, data3))

from IPython.display import display
import pingouin as pg
display(pg.welch_anova(dv='value', between='target', data=df))


# 비교를 위해 f_oneway 와 kruskal 모두 시행했다.
# kruskal의 경우 평균의 차이가 존재, f_oneway, welch(p-unc값)의 경우 차이가 존재하지 않는다
