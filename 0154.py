'''
다음은 BostonHousing 데이터 세트이다.
CRIM항목의 상위에서 10번째 값(즉, 상위 10번째 값 중에서 가장 적은 값)으로
상위 10개 값을 변환 하고, age 80이상인 값에 대하여 CRIM평균을 구하시오.
'''
import pandas as pd
data = 'BostonHousing.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

chk = df.CRIM.sort_values(ascending = False).head(11)
pt = chk.values[9]
#print(pt)
df.loc[df.CRIM > pt,'CRIM'] = pt
#print(df.CRIM.sort_values(ascending = False).head(11))
ans = df[df.AGE >= 80].CRIM.mean()
print(ans)

'''
주어진 데이터의 첫번째 행부터 순서대로 80%까지의 데이터를 훈련 데이터로 추출후
'total_bedrooms'변수의 결측값(NA)을 'total_bedrooms'변수의 중앙값으로 대체하고
대체 전의 'total_bedrooms'변수 표준편차 값과
대체 후의 'total_bedrooms'변수 표준편차 값의 차이의 절대값을 구하시오.
'''
import pandas as pd
data = 'housing.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

semi = df.head(int(len(df)*0.8))
before = semi.total_bedrooms.std()
#print(before)
chk = semi.total_bedrooms.median()
semi['total_bedrooms'] = semi.total_bedrooms.fillna(chk)
after = semi.total_bedrooms.std()
ans = abs(before - after)
print(ans)

'''
다음은 Insurance 데이터 세트이다.
Charges 항목에서 이상 값의 합을 구하시오.
(이상값은 평균에서 1.5표준편차 이상인 값)
'''
import pandas as pd
data = 'Insurance.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())
chk = df.charges.std()
up = df[df.charges >= (df.charges.mean() + 1.5*chk)].charges.sum()
under = df[df.charges <= (df.charges.mean() - 1.5*chk)].charges.sum()
print(up+under)
