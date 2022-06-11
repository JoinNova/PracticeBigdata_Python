'''
다음은 ISLR패키지의 Carseats 데이터 세트이다.
매출(Sales)의 이상값을 제외한 데이터를 훈련 데이터로 선정할 때
Age 의 표준편차를 구하시오.
(이상값은 평균보다 1.5 표준편차 이하이거나 이상인 값으로 선정한다.)
'''
import pandas as pd
data = 'carseats.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

chk = df.Sales.std()
#print(chk)
#print(df.Sales.mean())
ans = df[abs(df.Sales - df.Sales.mean()) < chk*1.5].Sales.std()
#print(df.Sales.mean()-chk*1.5,' , ',df.Sales.mean()+chk*1.5 )
#print(df.Age.std())
print(ans)

'''
다음은 MASS 패키지의 Cars93 데이터 세트이다. Luggage.room의 결측값을 중앙값으로 변환한 후
변환 전,후 평균의 차이를 구하시오.
'''
import pandas as pd
data = 'Cars93.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

before = df['Luggage.room'].mean()
df.loc[df['Luggage.room'].isnull(), 'Luggage.room'] = df['Luggage.room'].fillna(df['Luggage.room'].median())
after = df['Luggage.room'].mean()
ans = abs(before - after)
print(ans)

'''
다음은 Covid19의 TimeAge 데이터 세트이다. 연령(age)이 20대(20s)인 확진자(confirmed)의 평균과
50대(50s)인 확진자(confirmed)평균의 차이를 구하시오.
'''
import pandas as pd
data = 'TimeAge.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

ans = abs(df[df.age == '20s'].confirmed.mean() - df[df.age == '50s'].confirmed.mean())
print(ans)
