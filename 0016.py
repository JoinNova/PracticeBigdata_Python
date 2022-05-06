#독립표본 검정 (Independent)

#독립 표본 t검정의 경우 집단의 정규성에 따라 접근방식이 다르다
#정규성 검정은 shapiro , anderson(샘플 5000개 이상) 을 통해 확인

#데이터가 정규성을 가지는 경우(모수적 검정)
#두 집단의 등분산 검정을 한 후

#from scipy.stats import ttest_ind

#데이터가 정규성을 가지지 않는 경우(비모수적 검정)

#01 개 학급의 시험성적에 대한 데이터이다. 두 학습의 시험 평균(비모수검정의 경우 중위값)은 동일하다 말할 수 있는지 확인 하라
import pandas as pd 
import matplotlib.pyplot as plt
df1 = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/ind1.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/ind2.csv')


plt.hist(df1,label='df1',alpha=0.4)
plt.hist(df2,label="df2",alpha=0.4)
plt.xlabel('Score bins')
plt.ylabel('Counts')
plt.legend()
plt.show()

from scipy.stats import shapiro
print(shapiro(df1))
print(shapiro(df2))

# 두 그룹 모두 Shapiro검정 결과 귀무가설(정규성을 가진다)을 기각 하지 못한다. 두 그룹은 정규성을 가진다.

from scipy.stats import levene
print()
print(levene(df1['data'],df2['data']))
# 두그룹은 levene 검정을 확인해 본결과 pvalue 는 0.11로 귀무가실을 기각히지 못한다. 그러므로 등분산은 가진다

from scipy.stats import ttest_ind
print()
print(ttest_ind(df1,df2,equal_var=True))

# 등분산이기 때문에 equal_var=True 파라미터를 주고 ttest_ind 모듈을 이용하여 t test를 진행한다
# pvalue는 0.006이므로 귀무가설(각 그룹의 평균값은 동일하다)를 기각하고 대립가설을 채택한다

#02 두개 학급의 시험성적에 대한 데이터이다. 두 학습의 시험 평균(비모수검정의 경우 중위값)은 동일하다 말할 수 있는지 확인 하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/scipy5.csv')

plt.hist(df['A'],alpha=0.5,label='A')
plt.hist(df['B'].dropna(),alpha=0.5,label="B")
plt.xlabel('Score bins')
plt.ylabel('Counts')
plt.legend()
plt.show()

# 데이터 분포를 확인해보니 정규성을 위해하는 것 처럼 보인다.
# 두그룹중 한 그룹만 정규성을 위배해도 독립표본 t-검정을 할 수 없다

print(shapiro(df['B'].dropna()))
print(shapiro(df['A']))

# 두 그룹 모두 Shapiro검정 결과 귀무가설(정규성을 가진다)을 기각한다. 정규성을 위배한다. 그러므로 비모수 검정을 실시해야한다.

from scipy.stats import mannwhitneyu , ranksums
print()
print(mannwhitneyu(df['A'],df['B'].dropna()))
print(ranksums(df['A'],df['B'].dropna()))

# Mann-Whitney U Test 검정 결과 pvalue는 0.49값으로 귀무가설(평균은같다)를 기각 할 수 없다. 두그룹의 평균은 동일하다 말할 수 있다. 
# 윌콕슨 순위합 검정(ranksums)으로 확인 해봐도 같은 결과가 나온다.

#03 두개 그룹에 대한 수치형 데이터이다. 두 그룹의 평균은 동일하다 말할 수 있는지 검정하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/ind3.csv')

plt.hist(df[df['group'] =='a'].data,label='A',alpha=0.5)
plt.hist(df[df['group'] =='b'].data,label="B",alpha=0.5)
plt.xlabel('Score bins')
plt.ylabel('Counts')
plt.legend()
plt.show()

a = df[df['group'] =='a'].data
b = df[df['group'] =='b'].data


from scipy.stats import shapiro
print(shapiro(a))
print(shapiro(b))

print("두 그룹 모두 Shapiro검정 결과 귀무가설(정규성을 가진다)을 기각 하지 못한다. 두 그룹은 정규성을 가진다.")

from scipy.stats import levene
print()
print(levene(a,b))
print("두그룹은 levene 검정을 확인해 본결과 pvalue 는 0.013로 귀무가실을 기각하고 대립가설을 채택한다. 두 그룹은 등분산이 아니다")

from scipy.stats import ttest_ind
print()
print(ttest_ind(a,b,equal_var=False))

print('''등분산이 아니기 때문에 equal_var=False 파라미터를 주고 ttest_ind 모듈을 이용하여 t test를 진행한다
pvalue는 0.02이므로 귀무가설(각 그룹의 평균값은 동일하다)를 기각하고 대립가설을 채택한다
결론적으로 두 그룹은 모두 정규성을 가지지만 등분산은 아니며 평균은 동일하다고 보기 어렵다
''')

#04 두개 그룹에 대한 수치형 데이터이다. 두 그룹의 평균은 동일하다 말할 수 있는지 검정하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/ind6.csv')

plt.hist(df['a'],alpha=0.5,label='A')
plt.hist(df['b'],alpha=0.5,label="B")
plt.xlabel('Score bins')
plt.ylabel('Counts')
plt.legend()
plt.show()

a = df['a'].dropna()
b = df['b'].dropna()


from scipy.stats import shapiro
print(shapiro(a))
print(shapiro(b))

print("두 그룹 모두 Shapiro검정 결과 귀무가설(정규성을 가진다)을 기각 하지 못한다. 두 그룹은 정규성을 가진다.")

from scipy.stats import levene
print()
print(levene(a,b))
print("두그룹은 levene 검정을 확인해 본결과 pvalue 는 0.047로 귀무가실을 기각하고 대립가설을 채택한다. 두 그룹은 등분산이 아니다")

from scipy.stats import ttest_ind
print()
print(ttest_ind(a,b,equal_var=False))

print('''등분산이 아니기 때문에 equal_var=False 파라미터를 주고 ttest_ind 모듈을 이용하여 t test를 진행한다
pvalue는 0.99이므로 귀무가설(각 그룹의 평균값은 동일하다)를 기각하기 어렵다
결론적으로 두 그룹은 모두 정규성을 가지지만 등분산은 아니며 평균은 동일하다고 볼 수 있다
''')
