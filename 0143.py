'''
다음은 ISLR패키지의 Carseats 데이터 세트이다.
매출(Sales)의 이상값을 제외한 데이를 훈련 데이터로 선정할 때
Age의 표준편차를 구하시오.
(이상 값은 평균보다 1.5표준편차이하이거나 이상인 값으로 선정한다.
'''
import pandas as pd
data = 'Carseats.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

chk = df.Sales.std()
#print(chk)
train = df[(df.Sales < (df.Sales.mean() + chk*1.5)) & (df.Sales > (df.Sales.mean() - chk*1.5))]
ans = train.Age.std()
print(ans)


'''
다음은 MASS 패키지의 Cars93 데이터 세트이다.
Luggage.room의 결측값을 중앙값으로 변환한 후
변환 전, 후 평균의 차이를 구하시오.
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
다음은 Covid19의 TimeAge데이터 세트이다.
연령(age)이 20대(20s)인 확진자(confirmed)의 평균과
50대(50s)인 확진자(confirmed) 평균의 차이를 구하시오.
'''
import pandas as pd
data = 'TimeAge.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

chk = df.groupby('age').mean().reset_index()
#print(chk)
ans = chk[chk.age == '20s'].confirmed.values[0] - chk[chk.age == '50s'].confirmed.values[0]
print(ans)
