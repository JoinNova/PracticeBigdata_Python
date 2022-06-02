'''
데이터 출처 : https://archive.ics.uci.edu/ml/datasets/Bank+Marketing (후처리 작업)
데이터 설명 : 은행의 전화 마케팅에 대해 고객의 반응 여부
dataurl : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv'
df = pd.read_csv(data)
#print(df.head())
#print(df.info())

#01 마케팅응답 고객들의 나이를 10살 단위로 변환 했을 때, 가장 많은 인원을 가진 나이대는? (0~9 : 0 , 10~19 : 10)
ans = (df.age//10*10).value_counts()
print(ans.index[0])

#02 마케팅 응답 고객들의 나이를 10살 단위로 변환 했을 때, 가장 많은 나이대 구간의 인원은 몇명인가?
print(ans.values[0])

#03 나이가 25살 이상 29살 미만인 응답 고객들중 housing컬럼의 값이 yes인 고객의 수는?
ans = df[(df.age >= 25) & (df.age < 29) & (df.housing == 'yes')]
print(len(ans))

#04 numeric한 값을 가지지 않은 컬럼들중 unique한 값을 가장 많이 가지는 컬럼은?
chk, ans = 0, []
for _ in df.select_dtypes(include = object):
    #print(_)
    if df[_].nunique() >= chk:
        chk = df[_].nunique()
        ans.append(_)
print(*ans)

#05 balance 컬럼값들의 평균값 이상을 가지는 데이터를 ID값을 기준으로 내림차순 정렬했을때 상위 100개 데이터의 balance값의 평균은?
ans = df[df.balance >= df.balance.mean()].sort_values('ID', ascending = False).head(100).balance.mean()
print(ans)

#06 가장 많은 광고를 집행했던 날짜는 언제인가? (데이터 그대로 일(숫자),달(영문)으로 표기)
ans = df[['day', 'month']].value_counts().index[0]
print(ans)

#07 데이터의 job이 unknown 상태인 고객들의 age 컬럼 값의 정규성을 검정하고자 한다. 샤피로 검정의 p-value값을 구하여라
from scipy.stats import shapiro
ans = shapiro(df[df.job == 'unknown'].age)[1]
print(ans)

#08 age와 balance의 상관계수를 구하여라
ans = df[['age', 'balance']].corr().values[0, 1]
print(ans)

#09 y 변수와 education 변수는 독립인지 카이제곱검정을 통해 확인하려한다. p-value값을 출력하라
from scipy.stats import chi2_contingency
chk = pd.crosstab(df.y, df.education)
print(chk)
ans = chi2_contingency(chk)[1]
print(ans)

#10 각 job에 따라 divorced/married 인원의 비율을 확인 했을 때 그 값이 가장 높은 값은?
chk = df.groupby(['job', 'marital']).size().reset_index()
print(chk)
pivotdf = chk.pivot_table(index = 'job', columns = 'marital')[0]
pivotdf['ratio'] = pivotdf.divorced / pivotdf.married
print(pivotdf)
ans = pivotdf.ratio.max()
print(ans)
