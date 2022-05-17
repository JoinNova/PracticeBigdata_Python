'''
전세계 행복도 지표 데이터
데이터 출처 :https://www.kaggle.com/unsdsn/world-happiness(참고, 데이터 수정)
데이터 설명 : 전세계 행복도 지표 조사
data url = https://raw.githubusercontent.com/Datamanim/datarepo/main/happy2/happiness.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/happy2/happiness.csv'
df = pd.read_csv(data)
print(type(df))
print(df.head())
print(df.columns)

#01 데이터는 2018년도와 2019년도의 전세계 행복 지수를 표현한다. 각년도의 행복랭킹 10위를 차지한 나라의 행복점수의 평균을 구하여라
print(df[df.행복랭킹 == 10]['점수'].mean())

#02 데이터는 2018년도와 2019년도의 전세계 행복 지수를 표현한다. 각년도의 행복랭킹 50위이내의 나라들의 각각의 행복점수 평균을 데이터프레임으로 표시하라
print(df[df.행복랭킹 <= 50][['년도', '점수']].groupby('년도').mean())

#03 2018년도 데이터들만 추출하여 행복점수와 부패에 대한 인식에 대한 상관계수를 구하여라
print(df[df.년도 == 2018][['점수', '부패에 대한인식']].corr().iloc[0, 1])

#04 2018년도와 2019년도의 행복랭킹이 변화하지 않은 나라명의 수를 구하여라
print(len(df[['행복랭킹', '나라명']]) - len(df[['행복랭킹', '나라명']].drop_duplicates()))

#05 2019년도 데이터들만 추출하여 각변수간 상관계수를 구하고 내림차순으로 정렬한 후 상위 5개를 데이터 프레임으로 출력하라. 컬럼명은 v1,v2,corr으로 표시하라
zz = df[df.년도 == 2019].corr().unstack().to_frame().reset_index().dropna()
ans = zz[zz[0] != 1].sort_values(0, ascending = False).drop_duplicates(0).\
      head().reset_index(drop = True)
ans.columns = ['v1', 'v2', 'corr']
print(ans)

#06 각 년도별 하위 행복점수의 하위 5개 국가의 평균 행복점수를 구하여라
print(df.groupby('년도').tail().groupby('년도').mean()[['점수']])

#07 2019년 데이터를 추출하고 해당데이터의 상대 GDP 평균 이상의 나라들과 평균 이하의 나라들의 행복점수 평균을 각각 구하고 그 차이값을 출력하라
over = df[df.상대GDP >= df.상대GDP.mean()]['점수'].mean()
under = df[df.상대GDP <= df.상대GDP.mean()]['점수'].mean()
print(over - under)

#08 각년도의 부패에 대한인식을 내림차순 정렬했을때 상위 20개 국가의 부패에 대한인식의 평균을 구하여라
print(df.sort_values(['년도','부패에 대한인식'], ascending = False).groupby('년도').head(20).\
      groupby(['년도']).mean()[['부패에 대한인식']])

#09 2018년도 행복랭킹 50위 이내에 포함됐다가 2019년 50위 밖으로 밀려난 국가의 숫자를 구하여라
print(len(set(df[(df.년도 == 2018) & (df.행복랭킹 <= 50)].나라명)\
          -set(df[(df.년도 == 2019) & (df.행복랭킹 <= 50)].나라명)))

#10 2018년,2019년 모두 기록이 있는 나라들 중 년도별 행복점수가 가장 증가한 나라와 그 증가 수치는?
count = df.나라명.value_counts()
target = count[count >= 2 ].index
df2 = df.copy()
multiple = df2[df2.나라명.isin(target)].reset_index(drop = True)
multiple.loc[multiple['년도'] == 2018, '점수'] = multiple[multiple.년도 == 2018]['점수'].values * (-1)
print(multiple.groupby('나라명').sum()['점수'].sort_values().to_frame().iloc[-1])
