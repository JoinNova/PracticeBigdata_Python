import pandas as pd
data = 'BostonHousing.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())

'''
#01 다음은 BostonHousing 데이터세트이다.
crim항목의 상위에서 10번째 값(즉, 상위 10번째 값중에서 가장 적은 값)으로
상위 10개의 값을 변환하고, age 80이상인 값에 대하여 crim 평균을 구하시오.
'''
#print(df.CRIM.head(11))
chk = df.sort_values('CRIM', ascending = False)
#print(chk.CRIM.head(11))
#SRIM항목의 상위 10번째를 찾기 위한 내림차순정렬

ans = chk.CRIM.values[9]
#print(ans) #상위 10번째 CRIM 저장.

df.loc[df.CRIM >= ans, 'CRIM'] = ans
#print(df.CRIM.sort_values(ascending = False).head(11))
#원본 데이터에서 CRIM항목의 상위 10개의 값을 직전에 찾은 상위10번째 값으로 변환

result = df[df.AGE >= 80].CRIM.mean()
print(result)
#AGE가 80 이상인 값에 대하여 CRIM평균이 답.



import pandas as pd
data = 'housing.csv'
df = pd.read_csv(data)
#print(df['total_bedrooms'].sort_values(ascending = False))
#print(df)
#print(df.info())

'''
주어진 데이터 첫 번째 행부터 순서대로 80%까지의 데이터를 춘련 데이터로 추출 후
housing_office 항목에서
'total_bedrooms'변수의 결측값을
'total_bedrooms'변수의 중앙값으로 대체하고
대체 전의 'total_bedrooms'변수 표준편차값을 산출하려고 한다.
결측값을 중앙값으로 변환한후,
변환이전과 이후의 표준편차 차이를 구하시오.
'''
df_ = df.iloc[:int(len(df)*0.8)]
#원본데이터에서 순서대로 80%까지 추출
#print(df_.head())
#print(df_.info())

fir = df_['total_bedrooms'].var()**(1/2)
#print(fir)  #결측값 보정전 표준편차

df_.loc[df_['total_bedrooms'].isnull(),'total_bedrooms'] = df_['total_bedrooms'].fillna(df_['total_bedrooms'].median())
sec = df_['total_bedrooms'].var()**(1/2)
#print(sec) #결측값 중앙값으로 보정 후 표준편차

print(abs(fir - sec))
#변화 전과 후의 표준편차 차이


import pandas as pd
data = 'Insurance.csv'
df = pd.read_csv(data)
print(df)
print(df.info())

'''
다음은 Insurance 데이터 세트이다. Charges 항목에서 이상값의 합을 구하시오.
(이상값은 평균에서 1.5표준편차인 값)
'''
mid = df.charges.mean()
v = df.charges.var()
sq = v**(1/2)
print(mid, '\n', v, '\n', sq)
ans = df[(df.charges < (mid - 1.5*sq)) | (df.charges > (mid + 1.5*sq))].charges.sum()
print(ans)
