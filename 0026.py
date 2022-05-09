'''
주가 데이터 : https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data
DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv’
'''
data = 'https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv'
import pandas as pd
df = pd.read_csv(data)

#01 데이터를 로드하고 각 열의 데이터 타입을 파악하라
print(df.info())

#02 Yr_Mo_Dy을 판다스에서 인식할 수 있는 datetime64타입으로 변경하라
df.Yr_Mo_Dy = pd.to_datetime(df.Yr_Mo_Dy)
print(df.Yr_Mo_Dy.head())

#03 Yr_Mo_Dy에 존재하는 년도의 유일값을 모두 출력하라
ans = df.Yr_Mo_Dy.dt.year.unique()
print(ans)

#04 Yr_Mo_Dy에 년도가 2061년 이상의 경우에는 모두 잘못된 데이터이다. 해당경우의 값은 100을 빼서 새롭게 날짜를 Yr_Mo_Dy 컬럼에 정의하라
df.Yr_Mo_Dy = pd.to_datetime(df.Yr_Mo_Dy)
def fix_century(x) :
    import datetime
    year = x.year - 100 if x.year > 2060 else x.year
    return pd.to_datetime(datetime.date(year, x.month, x.day))
df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix_century)
print(df.Yr_Mo_Dy.head())

#05 년도별 각 컬럼의 평균값을 구하여라
df.Yr_Mo_Dy = pd.to_datetime(df.Yr_Mo_Dy)
def fix_century(x) :
    import datetime
    year = x.year - 100 if x.year > 2060 else x.year
    return pd.to_datetime(datetime.date(year, x.month, x.day))
df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix_century)
ans = df.groupby(df.Yr_Mo_Dy.dt.year).mean()
print(ans.head())

#06 weekday컬럼을 만들고 요일별로 매핑하라 ( 월요일: 0 ~ 일요일 :6)
df.Yr_Mo_Dy = pd.to_datetime(df.Yr_Mo_Dy)
def fix_century(x) :
    import datetime
    year = x.year - 100 if x.year > 2060 else x.year
    return pd.to_datetime(datetime.date(year, x.month, x.day))
df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix_century)
df['weekday'] = df.Yr_Mo_Dy.dt.weekday
ans = df['weekday'].head().to_frame()
print(ans)

#07 weekday컬럼을 기준으로 주말이면 1 평일이면 0의 값을 가지는 WeekCheck 컬럼을 만들어라
df.Yr_Mo_Dy = pd.to_datetime(df.Yr_Mo_Dy)
def fix(x) :
    import datetime
    year = x.year - 100 if x.year > 2060 else x.year
    return pd.to_datetime(datetime.date(year, x.month, x.day))
df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix)
df['weekday'] = df.Yr_Mo_Dy.dt.weekday
df['check'] = df['weekday'].map(lambda x : 1 if x in[5, 6] else 0)
ans = df['check'].head().to_frame()
print(ans)

#08 년도, 일자 상관없이 모든 컬럼의 각 달의 평균을 구하여라
df.Yr_Mo_Dy = pd.to_datetime(df.Yr_Mo_Dy)
def fix(x) :
    import datetime
    year = x.year - 100 if x.year > 2060 else x.year
    return pd.to_datetime(datetime.date(year, x.month, x.day))
df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix)
ans = df.groupby(df.Yr_Mo_Dy.dt.month).mean()
print(ans.head())

#09 모든 결측치는 컬럼기준 직전의 값으로 대체하고 첫번째 행에 결측치가 있을경우 뒤에있는 값으로 대채하라
df = df.fillna(method = 'ffill').fillna(method = 'bfill')
print(df.isnull().sum())

#10 년도 - 월을 기준으로 모든 컬럼의 평균값을 구하여라
df.Yr_Mo_Dy = pd.to_datetime(df.Yr_Mo_Dy)
def fix(x) :
    import datetime
    year = x.year - 100 if x.year > 2060 else x.year
    return pd.to_datetime(datetime.date(year, x.month, x.day))
df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix)
df = df.fillna(method = 'ffill').fillna(method = 'bfill')
ans = df.groupby(df.Yr_Mo_Dy.dt.to_period('M')).mean()
print(ans.head())

#11 RPT 컬럼의 값을 일자별 기준으로 1차차분하라
ans = df['RPT'].diff()
print(ans.head())

#12 RPT와 VAL의 컬럼을 일주일 간격으로 각각 이동평균한값을 구하여라
ans = df[['RPT', 'VAL']].rolling(7).mean()
print(ans)
