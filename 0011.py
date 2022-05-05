#국가별 5세이하 사망비율 통계 : https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete
#데이터 변형 Dataurl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv’

import pandas as pd
from IPython.display import display
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv',index_col= 0)
df1 = df.iloc[:4,:]
df2 = df.iloc[4:,:]
display(df1)
display(df2)
df3 = df.iloc[:2,:4]
df4 = df.iloc[5:,3:]
display(df3)
display(df4)
df5 = df.T.iloc[:7,:3]
df6 = df.T.iloc[6:,2:5]
display(df5)
display(df6)

#01 df1과 df2 데이터를 하나의 데이터 프레임으로 합쳐라
total = pd.concat([df1,df2])
Ans = total
print(Ans)

#02 df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 둘다 포함하고 있는 년도에 대해서만 고려한다
Ans = pd.concat([df3,df4],join='inner')
print(Ans)

#03 df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 모든 컬럼을 포함하고, 결측치는 0으로 대체한다
Ans = pd.concat([df3,df4],join='outer').fillna(0)
print(Ans)

#04 df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 두 데이터 모두 포함하는 데이터만 출력하라
Ans = pd.merge(df5,df6,on='Algeria',how='inner')
print(Ans)

#05 df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 합집합으로 합쳐라
Ans =pd.merge(df5,df6,on='Algeria',how='outer')
print(Ans)
