'''
다음은 BostonHousing데이터 세트이다.
CRIM 항목의 상위에서 10번째 값
(즉 상위 10배째 값 중에서 가장 적은 값)으로 상위 10개의 값을 변환하고,
AGE80 이상인 값에 대하여 CRIM평균을 구하시오..
'''
import pandas as pd
data = 'BostonHousing.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

chk = df.CRIM.sort_values(ascending = False).values[9]
print(chk)
df[df.CRIM >= chk] = chk
print(df.CRIM.sort_values(ascending = False).head(11))
ans = df[df.AGE >= 80].CRIM.mean()
print(ans)

'''
주어진 데이터 첫 번째 행부터 순서대로 80%까지의 데이터를 훈련 데이터로 추출 후
housing_office 항목에서 'total_bedrooms' 변수의 결측값(NA)을
'total_bedrooms'변수의 중앙값으로 대체하고
대체 전의 'total_bedrooms'변수 표준편차 값과
대체 후의 'total_bedrooms'변수 표준편차 값을 산출하려고 한다.
결측값을 중앙값으로 변환한 후, 변환 이전과 이후의 표준편차 차이를 구하시오.
'''
import pandas as pd
data = 'housing.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())
newdf = df.head(int(len(df)*0.8))
#print(newdf)
print(newdf.describe())
bef=newdf.total_bedrooms.std()
print(bef)
mid = newdf.total_bedrooms.median()
newdf.loc[newdf.total_bedrooms.isnull(), 'total_bedrooms'] = newdf.total_bedrooms.fillna(mid)
af = newdf.total_bedrooms.std()
print(af)
ans = abs(bef - af)
print(ans)


'''
다음은 insurance 데이터 세트이다. charges 항목에서 이상값의 합을 구하시오.
(이상 값은 평균에서 1.5 표준편차 이상인 값)
'''
import pandas as pd
data = 'insurance.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
print(df.describe())

ans = df.charges[abs(df.charges - df.charges.mean()) > df.charges.std()*1.5].sum()
print(ans)
