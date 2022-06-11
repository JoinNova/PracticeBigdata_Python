'''
다음은 BostonHousing 데이터 세트이다.
본인 소유의 주택가격에서 상위 50개의 데이터에 대하여 최솟값으로 변환한 후
타운별 1인당 범죄율 값이 1이상인 데이터를 구하시오.
'''
import pandas as pd
data = 'BostonHousing.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

chk = df.MEDV.sort_values(ascending = False).head(50).values[-1]
print(chk)
df.loc[df.MEDV >= chk, 'MEDV'] = chk
print(df.MEDV.sort_values(ascending = False).head(50))
ans = df[df.CRIM >= 1].CRIM.mean()
print(ans)

'''
다음은 iris 데이터 세트이다. iris 데이터 세트에서 70% 데이터를 샘플링 후
꽃받침 길이의 표준편차를 구하시오.
'''
import pandas as pd
data = 'iris.csv'
df = pd.read_csv(data)
print(df)
print(df.info())
print(df.describe())

sp = df.head(int(len(df)*0.7))
ans = sp.SepalLengthCm.std()
print(ans)

'''
다음은 mtcars 데이터 세트이다.
wt 칼럼을 최소 최대 척도(min-max scale)로 변환한 후 큰 레코드 수를 구하시오.
'''
import pandas as pd
data = 'mtcars.csv'
df = pd.read_csv(data)
print(df)
print(df.info())
print(df.describe())

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
minmax = scaler.fit_transform(df.loc[:,['wt']])
print(minmax)
ans = minmax[minmax > 0.5]
print(len(ans))
