'''
데이터 출처 : https://www.kaggle.com/abcsds/pokemon (참고, 데이터 수정)
데이터 설명 : 포켓몬 정보
data url = https://raw.githubusercontent.com/Datamanim/datarepo/main/pok/Pokemon.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/pok/Pokemon.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

#01 Attack컬럼의 값을 기준으로 내림차순정렬 했을때 상위 400위까지 포켓몬들과 401~800위까지의 포켓몬들에서 전설포켓몬(Legendary컬럼)의 숫자 차이는?
chk = df.sort_values('Attack', ascending = False)
ans = chk.head(400).Legendary.sum() - chk.iloc[400:800].Legendary.sum()
print(ans)

#02 Type 1 컬럼의 종류에 따른 Total 컬럼의 평균값을 내림차순 정렬했을때 상위 3번째 Type 1은 무엇인가?
ans = df.groupby('Type 1').Total.mean().sort_values(ascending = False).index[2]
print(ans)

#03 결측치가 존재하는 행을 모두 지운 후 처음부터 순서대로 60% 데이터를 추출하여 Defense컬럼의 1분위수를 구하여라
chk = df.dropna()
ans = chk.head(int(len(chk)*0.6)).Defense.quantile(0.25)
print(ans)

#04 Type 1 컬럼의 속성이 Fire인 포켓몬들의 Attack의 평균이상인 Water속성의 포켓몬 수를 구하여라
chk = df[df['Type 1'] == 'Fire'].Attack.mean()
ans = df[(df.Attack >= chk) & (df['Type 1'] == 'Water')]
print(len(ans))

#05 각 세대 중(Generation 컬럼)의 Speed와 Defense 컬럼의 차이(절댓값)이 가장 큰 세대는?
df['gap'] = abs(df.Speed - df.Defense)
ans = df.groupby('Generation').gap.mean().sort_values(ascending = False).index[0]
print(ans)
