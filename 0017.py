#대응표본 t 검정 (paired)
#01 특정 질병 집단의 투약 전후의 혈류량 변화를 나타낸 데이터이다. 투약 전후의 변화가 있는지 검정하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/rel2.csv')

fig ,ax = plt.subplots(1,2)
ax[0].boxplot(df['before'])
ax[1].boxplot(df['after'])
ax[0].set_xticklabels(['before'])
ax[1].set_xticklabels(['after'])
ax[0].set_ylim(100,350)
ax[1].set_ylim(100,350)
ax[1].get_yaxis().set_visible(False)
ax[0].set_ylabel('value')
plt.show()

from scipy.stats import shapiro

before = df['before']
after = df['after']
print(shapiro(before))
print(shapiro(after))

from scipy.stats import levene
print()
print(levene(before,after))


from scipy.stats import ttest_rel
print(ttest_rel(before,after))


# 정규성 가짐 , 등분산성 가짐 -> 대응표본의 경우 등분산성이 파라미터에 영향을 주지않음, 
# 대응표본 t 검정 결과 pvalue는 0.01로 유의수준 5%내에서 귀무가설을 기각한다 (전 후 평균은 같지 않다)

#02 특정 질병 집단의 투약 전후의 혈류량 변화를 나타낸 데이터이다. 투약 전후의 변화가 있는지 검정하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/rel3.csv')

fig ,ax = plt.subplots(1,2)
ax[0].boxplot(df['before'])
ax[1].boxplot(df['after'])
ax[0].set_xticklabels(['before'])
ax[1].set_xticklabels(['after'])
ax[0].set_ylim(130,300)
ax[1].set_ylim(130,300)
ax[1].get_yaxis().set_visible(False)
ax[0].set_ylabel('value')
plt.show()

from scipy.stats import shapiro

before = df['before']
after = df['after']
print(shapiro(before))
print(shapiro(after))

from scipy.stats import levene
print()
print(levene(before,after))


from scipy.stats import ttest_rel
print(ttest_rel(before,after))
print()



# 정규성 가짐 , 등분산성 가짐 -> 대응표본의 경우 등분산성이 파라미터에 영향을 주지않음, 
# 대응표본 t 검정 결과 pvalue는 0.85로 유의수준 5%내에서 귀무가설을 기각할 수 없다 (전 후 평균은 같다)

#03 특정 집단의 학습 전후 시험 성적 변화를 나타낸 데이터이다. 시험 전과 후에 차이가 있는지 검정하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/rel1.csv')

fig ,ax = plt.subplots(1,2)
ax[0].boxplot(df['before'])
ax[1].boxplot(df['after'])
ax[0].set_xticklabels(['before'])
ax[1].set_xticklabels(['after'])
ax[0].set_ylim(145,170)
ax[1].set_ylim(145,170)
ax[1].get_yaxis().set_visible(False)
ax[0].set_ylabel('value')
plt.show()

from scipy.stats import shapiro

before = df['before']
after = df['after']
print(shapiro(before))
print(shapiro(after))

from scipy.stats import levene
print()
print(levene(before,after))


from scipy.stats import ttest_rel
print(ttest_rel(before,after))
print()


from scipy.stats import wilcoxon
print(wilcoxon(before,after))
# 정규성을 가지지 않음 , 등분산성 가짐 -> 대응표본의 경우 등분산성이 파라미터에 영향을 주지않음, 
# 정규성을 가지지 않으므로 대응 표본 검정중 비모수 검정인 윌콕슨 부호순위 검정을 진행해야한다 (scipy.stats.wilcoxon)

# t-test의 경우 전후 변화에 대한 귀무가설을 기각되지만 윌콕슨 부호순위 검정을 통해서 확인해봤을때 귀무가설을 기각할 수 없다


#04 한 기계 부품의 rpm 수치를 두가지 다른 상황에서 측정했다.(총 70세트) b 상황이 a 상황보다 rpm값이 높다고 말할 수 있는지 검정하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/rel4.csv')

fig ,ax = plt.subplots(1,2)
ax[0].boxplot(df[df['group']=='a'].rpm)
ax[1].boxplot(df[df['group']=='b'].rpm)
ax[0].set_xticklabels(['a'])
ax[1].set_xticklabels(['b'])
ax[0].set_ylim(430,600)
ax[1].set_ylim(430,600)
ax[1].get_yaxis().set_visible(False)
ax[0].set_ylabel('rpm')
plt.show()


from scipy.stats import shapiro

a = df[df['group']=='a'].rpm
b =  df[df['group']=='b'].rpm
print(shapiro(a))
print(shapiro(b))

from scipy.stats import levene
print()
print(levene(a,b))


from scipy.stats import ttest_rel
print(ttest_rel(a,b,alternative='greater'))
print()


# 정규성을 가짐 , 등분산성 가짐 -> 대응표본의 경우 등분산성이 파라미터에 영향을 주지않음, 
# a,b,alternative='greater' 의 의미는 a >b가 대립가설이 된다는 것이다. p-value는 0.96으로
# 귀무가설인 a<=b를 기각하지 못한다. 그러므로 b상황이 a 상황보다 rpm 값이 크다고 이야기 할수 있다.
