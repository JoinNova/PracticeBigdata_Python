'''
오픈카톡_ADP빅분기_실기
by소니_실기 모의고사 1회차
작업1유형
데이터 출처 : https://archive.ics.uci.edu/ml/datasets/Bank+Marketing (후처리 작업)
데이터 설명 : 은행의 전화 마케팅에 대해 고객의 반응 여부
dataurl : https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv'
df = pd.read_csv(data)
print(type(df))
print(df.head())
print(df.columns)

#01 마케팅 응답 고객들의 나이를 10살 단위로 변환 했을 때, 가장 많은 인원을 가진 나이대는? (0~9 : 0 , 10~19 : 10)
df['Nage'] = df.age//10*10
ans = df['Nage'].value_counts()
print(ans.index[0])
#02 마케팅 응답 고객들의 나이를 10살 단위로 변환 했을 때, 가장 많은 나이대 구간의 인원은 몇명인가?
print(ans.max(0))
#03 나이가 25살 이상 29살 미만인 응답 고객들중 housing컬럼의 값이 yes인 고객의 수는?
ans = df[(df.age >= 25) &(df.age < 29) & (df.housing == 'yes')]
print(len(ans))
#04 numeric한 값을 가지지 않은 컬럼들중 unique한 값을 가장 많이 가지는 컬럼은?
target = 0
for _ in df.select_dtypes(include = object).columns:
    if df[_].nunique() > target:
        target = df[_].nunique()
        ans = _
print(ans)

#05 balance 컬럼값들의 평균값 이상을 가지는 데이터를 ID값을 기준으로 내림차순 정렬했을때 상위 100개 데이터의 balance값의 평균은?
ans = df[df['balance'] >= df.balance.mean()].\
      sort_values('ID', ascending = False)[0:100]
print(ans.balance.mean())

#06 가장 많은 광고를 집행했던 날짜는 언제인가? (데이터 그대로 일(숫자),달(영문)으로 표기)
ans = df.day.astype(str) +  df.month
print(ans.value_counts().index[0])

#07 데이터의 job이 unknown 상태인 고객들의 age 컬럼 값의 정규성을 검정하고자 한다. 샤피로 검정의 p-value값을 구하여라
from scipy.stats import shapiro
ans = df[df['job'] == 'unknown']
print(shapiro(ans.age)[1])

#08 age와 balance의 상관계수를 구하여라
import numpy as np
print(np.corrcoef(df.age, df.balance)[0, 1])

#09 y 변수와 education 변수는 독립인지 카이제곱검정을 통해 확인하려한다. p-value값을 출력하라
cdf = pd.crosstab(df['y'], df['education'])
print(cdf)
from scipy.stats import chi2_contingency
#print(chi2_contingency(cdf))
chi2, p, dof, expected = chi2_contingency(cdf)
print(p)

#10 각 job에 따라 divorced/married 인원의 비율을 확인 했을 때 그 값이 가장 높은
ans = df.groupby(['job', 'marital']).size().reset_index()
print(ans)
pivotdf = ans.pivot_table(index = 'job', columns = 'marital')[0]
pivotdf = pivotdf.fillna(0)
print(pivotdf)
pivotdf['ratio'] = pivotdf['divorced'] / pivotdf['married']
print(pivotdf.sort_values('ratio').ratio.values[-1])
