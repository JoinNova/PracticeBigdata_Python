import pandas as pd

#01 데이터를 로드하라. 데이터는 \t을 기준으로 구분되어있다.
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
df = pd.read_csv(DataUrl,sep='\t')
print(type(df))

#02 데이터의 상위 5개 행을 출력하라
Ans = df.head(5)
print(Ans)

#03 데이터의 행과 열의 갯수를 파악하라
print(df.shape)
print('행:',df.shape[0])
print('열:',df.shape[1])


#04 전체 컬럼을 출력하라
Ans = df.columns
print(Ans)

#05 6번째 컬럼명을 출력하라
Ans = df.columns[5]
print(Ans)

#06 6번째 컬럼의 데이터 타입을 확인하라
Ans = df.iloc[:,5].dtype
print(Ans)

#07 데이터셋의 인덱스 구성은 어떤가
Ans = df.index
print(Ans)

#08 6번째 컬럼의 3번째 값은 무엇인가?
Ans = df.iloc[2,5]
print(Ans)
