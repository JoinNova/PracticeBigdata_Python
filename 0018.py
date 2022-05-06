'''카이제곱 검정 (교차분석)
일원 카이제곱검정 (chisquare , 카이제곱 적합도 검정)
한 개의 요인에 의해 k개의 범주를 가질때 이론적 분포를 따르는지 검정
이원 카이제곱검정 (chi2_contingency ,fisher_exact(빈도수 5개 이하 셀이 20% 이상일때) , 카이제곱독립검정)
모집단이 두개의 변수에 의해 범주화 되었을 때, 두 변수들 사이의 관계가 독립인지 아닌지 검정'''

#01 144회 주사위를 던졌을때, 각 눈금별로 나온 횟수를 나타낸다. 이 데이터는 주사위의 분포에서 나올 가능성이 있는지 검정하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/dice.csv')

plt.bar(df.dice_number,df.counts)
plt.xlabel('dice value')
plt.ylabel('counts')
plt.show()

# 주사위 눈금의 발생확률은 1/6으로 모두 동일하다. 그러므로 각 눈금의 기댓값은 실제 발생한 모든값을 6으로 나눈 값이다.

from scipy.stats import chisquare
df['expected'] = (df['counts'].sum()/6).astype('int')
print(chisquare(df.counts,df.expected)) 

# p-value는 0.8로 귀무가설인 "각 주사위 눈금 발생비율은 동일함"을 기각 할 수 없다

#02 다음 데이터는 어떤 집단의 왼손잡이, 오른손 잡이의 숫자를 나타낸다. 인간의 왼손잡이와 오른손잡이의 비율을 0.2:0.8로 알려져있다.이 집단에서 왼손과 오른손 잡이의 비율이 적합한지 검정하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/hands2.csv')
print(df.head())


# 데이터에서 

from IPython.display import display
target = df.hands.value_counts().to_frame()
target['expected'] = [int(target.hands.sum()*0.8),int(target.hands.sum()*0.2)]
display(target)

from scipy.stats import chisquare
print(chisquare(target.hands,target.expected))

# 알려진 비율로 계산된 기댓값을 구하여 카이제곱검정을 시행한다.
# p-value는 0.02로 유의수준 5%이내에서 귀무가설을 기각하고 대립가설을 채택한다
# 즉 주어진 집단의 왼손, 오른손 비율은 0.2, 0.8으로 볼 수 없다

#03 다음 데이터는 국민 기초체력을 조사한 데이터이다. 성별과 등급이 독립적인지 검정하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/body/body.csv')
print(df.head())


cdf = pd.crosstab(df['측정회원성별'],df['등급'])
display(cdf)

from scipy.stats import chi2_contingency
print(chi2_contingency(cdf))
chi2 , p ,dof, expected = chi2_contingency(cdf)
print(p)

# p-value는 0에 근접하므로 측정회원성별 - 등급은 연관이 없다는 귀무가설을 기각하고, 성별관 체력 등급간에는 관련이 있다고 볼 수 있다.

#04 성별에 따른 동아리 활동 참석 비율을 나타낸 데이터이다. 성별과 참석간에 관련이 있는지 검정하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/fe2.csv',index_col=0)
print(df)

cdf = df.iloc[:-1,:-1]
display(cdf)

from scipy.stats import chi2_contingency,fisher_exact
print(chi2_contingency(cdf))
chi2 , p ,dof, expected = chi2_contingency(cdf)
print(p)

# 카이 제곱 검정시 p-value는 0.07로 귀무가설을 기각하지 못한다. 성별과 참석여부는 관련이 없다(독립이다).

# 하지만 5보다 작은 셀이 20%가 넘어가므로(75%) 피셔의 정확검정을 사용 해야한다.
# 피셔의 정확검정시 0.03의 값을 가지므로 귀무가설을 기각한다. 성별과 참석여부는 관련이 있다. (독립이 아니다)) 
print(fisher_exact(cdf))
