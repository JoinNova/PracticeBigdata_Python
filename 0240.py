'''
다음은 BostonHousing 데이터 세트이다. crim 항목의 상위에서 10번째 값
(즉, 상위 10번째 값 중에서 가장 적은 값)으로 상위 10개의 값을 변환하고,
age 80 이상인 값에 대하여 crim 평균을 구하시오.
'''
import pandas as pd
data = 'BostonHousing.csv'
df= pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

chk = df['CRIM'].sort_values(ascending = False).values[9]
df.loc[df.CRIM >= chk,'CRIM'] = chk
ans = df[df.AGE >= 80].CRIM.mean()
print(ans)

'''
주어진 테이터의 첫번째 행부터 순서대로 80%까지의 데이터를 훈련 데이터로
추출후 'total_bedrooms'변수의 결측값(NA)을 'total_bedrooms'변수의 중앙값으로
대체하고 대체전의 'total_bedrooms'변수 표준편차 값과 대체 후의
'total_bedrooms'변수 표준편차 값의 차이의 절대값을 구하시오.
'''
import pandas as pd
data = 'housing.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

before = df.total_bedrooms.std()
df.loc[df.total_bedrooms.isnull(), 'total_bedrooms'] = df.total_bedrooms.fillna(df.total_bedrooms.median())
after = df.total_bedrooms.std()

ans = abs(after - before)
print(ans)

'''
다음은 Insurance 데이터 세트이다. Charges 항목에서 이상값의 합을 구하시오.
(이상값은 평균에서 1.5 표준편차 이상인 값)
'''
import pandas as pd
data = 'Insurance.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

#print(df.charges.describe())
ans = df[(df.charges <= (df.charges.mean() - df.charges.std()*1.5)) | (df.charges >= (df.charges.mean() + df.charges.std()*1.5))].charges.sum()
print(ans)
