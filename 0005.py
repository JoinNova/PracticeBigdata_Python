#뉴욕 airBnB : https://www.kaggle.com/ptoscano230382/air-bnb-ny-2019
#DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv’

#01 데이터를 로드하고 상위 5개 컬럼을 출력하라
import pandas as pd
df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv')
Ans =df.head(5)
print(Ans)

#02 데이터의 각 host_name의 빈도수를 구하고 host_name으로 정렬하여 상위 5개를 출력하라
#Ans = df.groupby('host_name').size()
# or
Ans = df.host_name.value_counts().sort_index()
print(Ans.head(5))

#03 데이터의 각 host_name의 빈도수를 구하고 빈도수 기준 내림차순 정렬한 데이터 프레임을 만들어라. 빈도수 컬럼은 counts로 명명하라
Ans = df.groupby('host_name').size().\
                to_frame().rename(columns={0:'counts'}).\
                sort_values('counts',ascending=False)
print(Ans)

#04 neighbourhood_group의 값에 따른 neighbourhood컬럼 값의 갯수를 구하여라
Ans = df.groupby(['neighbourhood_group','neighbourhood'], as_index=False).size()
print(Ans.head(4))

#05 neighbourhood_group의 값에 따른 neighbourhood컬럼 값 중 neighbourhood_group그룹의 최댓값들을 출력하라
Ans= df.groupby(['neighbourhood_group','neighbourhood'], as_index=False).size()\
                  .groupby(['neighbourhood_group'], as_index=False).max()
print(Ans)

#06 neighbourhood_group 값에 따른 price값의 평균, 분산, 최대, 최소 값을 구하여라
Ans = df[['neighbourhood_group','price']].groupby('neighbourhood_group').agg(['mean','var','max','min'])
print(Ans)

#07 neighbourhood_group 값에 따른 reviews_per_month 평균, 분산, 최대, 최소 값을 구하여라
Ans = df[['neighbourhood_group','reviews_per_month']].groupby('neighbourhood_group').agg(['mean','var','max','min'])
print(Ans)

#08 neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 구하라
Ans = df.groupby(['neighbourhood','neighbourhood_group']).price.mean()
print(Ans)

#09 neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하라
Ans = df.groupby(['neighbourhood','neighbourhood_group']).price.mean().unstack()
print(Ans)

#10 neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하고 nan 값은 -999값으로 채워라
Ans = df.groupby(['neighbourhood','neighbourhood_group']).price.mean().unstack().fillna(-999)
print(Ans.head())

#11 데이터중 neighbourhood_group 값이 Queens값을 가지는 데이터들 중 neighbourhood 그룹별로 price값의 평균, 분산, 최대, 최소값을 구하라
Ans = df[df.neighbourhood_group=='Queens'].groupby(['neighbourhood']).price.agg(['mean','var','max','min'])
print(Ans.head())

#12 데이터중 neighbourhood_group 값에 따른 room_type 컬럼의 숫자를 구하고 neighbourhood_group 값을 기준으로 각 값의 비율을 구하여라
Ans = df[['neighbourhood_group','room_type']].groupby(['neighbourhood_group','room_type']).size().unstack()
Ans.loc[:,:] = (Ans.values /Ans.sum(axis=1).values.reshape(-1,1))
print(Ans)
