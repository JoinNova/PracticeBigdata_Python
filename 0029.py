'''
01 Getting & Knowing Data
롤 랭킹 데이터 : https://www.kaggle.com/datasnaek/league-of-legends
DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv’
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
#01 데이터를 로드하라. 데이터는 \t을 기준으로 구분되어있다.
df = pd.read_csv(data, sep = '\t')
print(type(df))
#02 데이터의 상위 5개 행을 출력하라
print(df.head())
#03 데이터의 행과 열의 갯수를 파악하라
print('(행, 열) ',df.shape)
#04 전체 컬럼을 출력하라
print(df.columns)
#05 6번째 컬럼명을 출력하라
print(df.columns[5])
#06 6번째 컬럼의 데이터 타입을 확인하라
print(df.iloc[:,5].dtype)
#07 데이터셋의 인덱스 구성은 어떤가
print(df.index)
#08 6번째 컬럼의 3번째 값은 무엇인가?
print(df.iloc[:3,:6])
print(df.iloc[2:3,5:6])
print(df.iloc[2,5])
