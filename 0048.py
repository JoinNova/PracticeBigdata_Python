'''
지역구 에너지 소비량 데이터
데이터 출처 : https://archive.ics.uci.edu/ml/datasets/Power+consumption+of+Tetouan+city (참고, 데이터 수정)
데이터 설명 : 기온, 습도,바람풍속에 따른 도시의 3개 지역구의 에너지 소비량
data url = https://raw.githubusercontent.com/Datamanim/datarepo/main/consum/Tetuan City power consumption.csv
'''

import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/consum/Tetuan%20City%20power%20consumption.csv'
df = pd.read_csv(data)
print(type(df))
print(df.head())
print(df.columns)

#01 DateTime컬럼을 통해 각 월별로 몇개의 데이터가 있는지 데이터 프레임으로 구하여라
df['DateTime'] = pd.to_datetime(df['DateTime'])
ans = df['DateTime'].dt.month.value_counts().sort_index().to_frame()
print(ans)

#02 3월달의 각 시간대별 온도의 평균들 중 가장 낮은 시간대의 온도를 출력하라
target = df[df.DateTime.dt.month == 3]
ans = target.groupby(target.DateTime.dt.hour)\
      ['Temperature'].mean().sort_values().values[0]
print(ans)

#03 3월달의 각 시간대별 온도의 평균들 중 가장 높은 시간대의 온도를 출력하라
target = df[df.DateTime.dt.month == 3]
ans = target.groupby(target.DateTime.dt.hour)\
      ['Temperature'].mean().sort_values().values[-1]
print(ans)

#04 Zone 1 Power Consumption 컬럼의 value값의 크기가 Zone 2 Power Consumption 컬럼의 value값의 크기보다 큰 데이터들의 Humidity의 평균을 구하여라
ans = df[df['Zone 1 Power Consumption'] > df['Zone 2  Power Consumption']].\
      Humidity.mean()
print(ans)

#05 각 zone의 에너지 소비량의 상관관계를 구해서 데이터 프레임으로 표기하라
ans = df.iloc[:, -3:].corr()
print(ans)

#06 Temperature의 값이 10미만의 경우 A, 10이상 20미만의 경우 B,20이상 30미만의 경우 C, 그 외의 경우 D라고 할때 각 단계의 데이터 숫자를 구하여라
def split_data(x):
    if x < 10:
        return 'A'
    elif x < 20:
        return 'B'
    elif x < 30:
        return 'C'
    else:
        return 'D'
df['sp'] = df.Temperature.map(split_data)
ans = df['sp'].value_counts()
print(ans)

#07 6월 데이터중 12시의 Temperature의 표준편차를 구하여라
ans = df[(df.DateTime.dt.month == 6) & (df.DateTime.dt.hour == 12)].\
      Temperature.std()
print(ans)

#08 6월 데이터중 12시의 Temperature의 분산을 구하여라
ans = df[(df.DateTime.dt.month == 6) & (df.DateTime.dt.hour == 12)].\
      Temperature.var()
print(ans)

#09 Temperature의 평균이상의 Temperature의 값을 가지는 데이터를 Temperature를 기준으로 정렬 했을때 4번째 행의 Humidity 값은?
ans = df[df.Temperature >= df.Temperature.mean()].\
      sort_values('Temperature').Humidity.values[3]
print(ans)

#10 Temperature의 중간값 이상의 Temperature의 값을 가지는 데이터를Temperature를 기준으로 정렬 했을때 4번째 행의 Humidity 값은?
ans = df[df.Temperature >= df.Temperature.median()].\
      sort_values('Temperature').Humidity.values[3]
print(ans)
