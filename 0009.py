#국가별 5세이하 사망비율 통계 : https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete
#Dataurl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/under5MortalityRate.csv’

#01 Indicator을 삭제하고 First Tooltip 컬럼에서 신뢰구간에 해당하는 표현을 지워라
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/under5MortalityRate.csv')
df.drop('Indicator',axis=1,inplace=True)
df['First Tooltip'] = df['First Tooltip'].map(lambda x: float(x.split("[")[0]))
Ans = df
print(Ans.head())

#02 년도가 2015년 이상, Dim1이 Both sexes인 케이스만 추출하라
target = df[(df.Period >=2015) & (df.Dim1 =='Both sexes')]
Ans = target
print(Ans.head())

#03 직전 문제(02번)에서 추출한 데이터로 아래와 같이 나라에 따른 년도별 사망률을 데이터 프레임화 하라
Ans = target.pivot(index='Location',columns='Period',values='First Tooltip')
print(Ans.head())

#04 Dim1에 따른 년도별 사망비율의 평균을 구하라
Ans = df.pivot_table(index='Dim1',columns='Period',values='First Tooltip',aggfunc='mean')
print(Ans.iloc[:,:4])

