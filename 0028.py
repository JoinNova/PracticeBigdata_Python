'''
국가별 5세이하 사망비율 통계 : https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete
Dataurl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/under5MortalityRate.csv’
'''
data = 'https://raw.githubusercontent.com/Datamanim/pandas/main/under5MortalityRate.csv'
import pandas as pd
'''
#01 Indicator을 삭제하고 First Tooltip 컬럼에서 신뢰구간에 해당하는 표현을 지워라
df = pd.read_csv(data)
df.drop('Indicator', axis = 1, inplace = True)
df['First Tooltip'] = df['First Tooltip'].map(lambda x: float(x.split('[')[0]))
print(df.head())

#02 년도가 2015년 이상, Dim1이 Both sexes인 케이스만 추출하라
df = pd.read_csv(data)
df.drop('Indicator', axis = 1, inplace = True)
df['First Tooltip'] = df['First Tooltip'].map(lambda x: float(x.split('[')[0]))
ans = df[(df.Period >= 2015) & (df.Dim1 == 'Both sexes')]
print(ans)

#03 02번 문제에서 추출한 데이터로 아래와 같이 나라에 따른 년도별 사망률을 데이터 프레임화 하라
df = pd.read_csv(data)
df.drop('Indicator', axis = 1, inplace = True)
df['First Tooltip'] = df['First Tooltip'].map(lambda x : float(x.split('[')[0]))
ans = df[(df.Period >= 2015) & (df.Dim1 == 'Both sexes')]
ans = ans.pivot(index = 'Location', columns = 'Period', values = 'First Tooltip')
print(ans)

#04 Dim1에 따른 년도별 사망비율의 평균을 구하라
df = pd.read_csv(data)
df.drop('Indicator', axis = 1,inplace = True)
df['First Tooltip'] = df['First Tooltip'].map(lambda x : float(x.split('[')[0]))
ans = df[(df.Period >= 2015) & (df.Dim1 == 'Both sexes')]
ans = df.pivot_table(index = 'Dim1', columns = 'Period', values = 'First Tooltip', aggfunc = 'mean')
print(ans.iloc[:,:4])
'''
'''
올림픽 메달리스트 정보 데이터: https://www.kaggle.com/the-guardian/olympic-games
dataUrl =’https://raw.githubusercontent.com/Datamanim/pandas/main/winter.csv’
'''
data = 'https://raw.githubusercontent.com/Datamanim/pandas/main/winter.csv'
df = pd.read_csv(data)
'''
#01 데이터에서 한국 KOR 데이터만 추출하라
kor = df[df.Country == 'KOR']
print(kor)

#02 한국 올림픽 메달리스트 데이터에서 년도에 따른 medal 갯수를 데이터프레임화 하라
kor = df[df.Country == 'KOR']
ans = kor.pivot_table(index = 'Year', columns = 'Medal', aggfunc = 'size').fillna(0)
print(ans)

#03 전체 데이터에서 sport종류에 따른 성별수를 구하여라
ans = df.pivot_table(index = 'Sport', columns = 'Gender', aggfunc = 'size')
print(ans)

#04 전체 데이터에서 Discipline종류에 따른 따른 Medal수를 구하여라
ans = df.pivot_table(index = 'Discipline', columns = 'Medal', aggfunc = 'size')
print(ans)
'''
'''
국가별 5세이하 사망비율 통계 : https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete
데이터 변형
Dataurl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv’
'''

data = 'https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv'
df = pd.read_csv(data)

df1 = df.iloc[:4,:]
df2 = df.iloc[4:,:]
df3 = df.iloc[:2,:5]
df4 = df.iloc[5:,4:]
df5 = df.T.iloc[:8,:3]
df6 = df.T.iloc[7:,2:5]
#df6.columns = ['Afghanistan','Albania','Algeria']
from IPython.display import display
#display(df1)
#display(df2)
#display(df3)
#display(df4)
#display(df5)
#display(df6)


#01 df1과 df2 데이터를 하나의 데이터 프레임으로 합쳐라
totala = pd.concat([df1,df2])
print(totala)

#02 df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 둘다 포함하고 있는 년도에 대해서만 고려한다
totalb = pd.concat([df3,df4], join = 'inner')
print(totalb)

#03 df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 모든 컬럼을 포함하고, 결측치는 0으로 대체한다
totalb = pd.concat([df3,df4], join = 'outer').fillna(0)
print(totalb)

#04 df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 두 데이터 모두 포함하는 데이터만 출력하라
ans = pd.merge(df5, df6, on = 2, how = 'inner')
ans.columns = ['Afghanistan','Albania','Algeria','Andorra','Angola']
print(ans)

#05 df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 합집합으로 합쳐라
ans =pd.merge(df5,df6,on=2,how='outer')
ans.columns = ['Afghanistan','Albania','Algeria','Andorra','Angola']
ans = ans.drop(ans.index[[0]])
print(ans)
