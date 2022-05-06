#등분산 검정
#01 두개 학급의 시험성적에 대한 데이터이다 그룹간 등분산 검정을 시행하라
import pandas as pd 
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/scipy2.csv')
print(df.head())

from scipy.stats import bartlett
from scipy.stats import fligner
from scipy.stats import levene

a = df[df['class'] =='A'].score
b = df[df['class'] =='B'].score

print(bartlett(a,b))

print(fligner(a,b,center='median')) #default
print(fligner(a,b,center='mean')) 

print(levene(a,b, center='median')) #default
print(levene(a,b,center='mean'))


# 등분산검정의 방법은 3가지가 있다. pvalue값은 5% 유의수준이라면 0.05보다 작은 경우 "각 그룹은 등분산이다"라는 귀무가설을 기각한다

# 아래의 결과를 보면 모두 0.05보다 크므로 귀무가설을 기각할수 없음을 알 수 있다.

#02 두개 학급의 시험성적에 대한 데이터이다 그룹간 등분산 검정을 시행하라
import pandas as pd 
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/scipy3.csv')
print(df.head())

from scipy.stats import bartlett
from scipy.stats import fligner
from scipy.stats import levene

a = df[df['class'] =='A'].score
b = df[df['class'] =='B'].score

print(bartlett(a,b))
print()
print(fligner(a,b,center='median')) #default
print(fligner(a,b,center='mean')) 

print(levene(a,b, center='median')) #default
print(levene(a,b,center='mean'))


# bartlett 검정 결과 pvalue는 0.05보다 크고
# fligner, levene 검정 결과 pvalue는 0.05보다 작다. 
# fligner, levene는 bartlett보다 좀더 robust하다는 특징이 있다.
# 어떤 검정의 결과를 사용해야하는지는 정해지지 않았지만 상황에 따라 특징들을 서술할 수 있다면 문제 없지 않을까...

#03 두개 학급의 시험성적에 대한 데이터이다 그룹간 등분산 검정을 시행하라
import pandas as pd 
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/scipy6.csv')
print(df.head())

from scipy.stats import bartlett
from scipy.stats import fligner
from scipy.stats import levene


print(bartlett(df.A,df.B))
print(fligner(df.A,df.B))
print(levene(df.A,df.B))

# BartlettResult -> 등분산이다  // FlignerResult , LeveneResult -> 등분산이 아니다

#04 두개 학급의 시험성적에 대한 데이터이다 그룹간 등분산 검정을 시행하라
import pandas as pd 
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/scipy5.csv')
print(df.head())

from scipy.stats import bartlett
from scipy.stats import fligner
from scipy.stats import levene


print(bartlett(df.A,df.B))
print(bartlett(df.A,df.B.dropna()))
print()

print(fligner(df.A,df.B))
print(fligner(df.A,df.B.dropna()))
print()

print(levene(df.A,df.B))
print(levene(df.A,df.B.dropna()))

# bartlett ,fligner 두 검정은 nan값을 지우고 사용해야한다. LeveneResult의 경우 nan값이 포함된다면 연산이 제대로 안된다
