'''
제주 날씨,인구에 따른 교통량데이터 : 출처 제주 데이터 허브
DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv’
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv'

#01 데이터를 로드하라. 컬럼이 한글이기에 적절한 처리해줘야함
df = pd.read_csv(data, encoding = 'euc-kr')
print(df.head())
#02 데이터 마지막 3개행을 출력하라
print(df.tail(3))
#03 수치형 변수를 가진 컬럼을 출력하라
print(df.select_dtypes(exclude = object).columns)
#04 범주형 변수를 가진 컬럼을 출력하라
print(df.select_dtypes(include = object).columns)
#05 각 컬럼의 결측치 숫자를 파악하라
print(df.isnull().sum())
#06 각 컬럼의 데이터수, 데이터타입을 한번에 확인하라
print(df.info())
#07 각 수치형 변수의 분포(사분위, 평균, 표준편차, 최대 , 최소)를 확인하라
print(df.describe())
#08 거주인구 컬럼의 값들을 출력하라
print(df['거주인구'])
#09 평균 속도 컬럼의 4분위 범위(IQR) 값을 구하여라
print(df['평균 속도'].quantile(0.75)-df['평균 속도'].quantile(0.25))
#10 읍면동명 컬럼의 유일값 갯수를 출력하라
print(df.읍면동명.nunique())
print(df['읍면동명'].nunique())
#11 읍면동명 컬럼의 유일값을 모두 출력하라
print(df.읍면동명.unique())
print(df['읍면동명'].unique())
