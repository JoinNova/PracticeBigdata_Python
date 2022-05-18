'''
포켓몬 정보 데이터
데이터 출처 : https://www.kaggle.com/abcsds/pokemon (참고, 데이터 수정)
데이터 설명 : 포켓몬 정보
data url = https://raw.githubusercontent.com/Datamanim/datarepo/main/pok/Pokemon.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/pok/Pokemon.csv'
df = pd.read_csv(data)
print(type(df))
print(df.head())
print(df.columns)

#01 Legendary 컬럼은 전설포켓몬 유무를 나타낸다.전설포켓몬과 그렇지 않은 포켓몬들의 HP평균의 차이를 구하여라
ans = df.groupby('Legendary').mean()['HP']
print(ans.values[1]-ans.values[0])

#02 Type 1은 주속성 Type 2 는 부속성을 나타낸다. 가장 많은 부속성 종류는 무엇인가?
ans = df['Type 2'].value_counts().index[0]
print(ans)

#03 가장 많은 Type 1 의 종의 평균 Attack 을 평균 Defense로 나눈값은?
Max = df['Type 1'].value_counts().index[0]
ans = df[df['Type 1'] == Max].Attack.mean()/\
      df[df['Type 1'] == Max].Defense.mean()
print(ans)

#04 포켓몬 세대(Generation) 중 가장많은 Legendary를 보유한 세대는 몇세대인가?
ans = df[df.Legendary == True].Generation.value_counts().index[0]
print(ans)

#05 ‘HP’, ‘Attack’, ‘Defense’, ‘Sp. Atk’, ‘Sp. Def’, ‘Speed’ 간의 상관 계수중 가장 절댓값이 큰 두 변수와 그 값을 구하여라
target = df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].\
         corr().unstack().reset_index().rename(columns = {0: 'corr'})
ans = target[target['corr'] != 1].sort_values('corr', ascending = False).iloc[0]
print(ans)

#06 각 Generation의 Attack으로 오름차순 정렬시 상위 3개 데이터들(18개)의 Attack의 전체 평균을 구하여라
print(df.sort_values(['Generation', 'Attack']).\
      groupby('Generation').head(3).Attack.mean())

#07 각 Generation의 Attack으로 내림차순 정렬시 상위 5개 데이터들(30개)의 Attack의 전체 평균을 구하여라
print(df.sort_values(['Generation', 'Attack'], ascending = False).\
      groupby('Generation').head(5).Attack.mean())

#08 가장 흔하게 발견되는 (Type1 , Type2) 의 쌍은 무엇인가?
print(df[['Type 1', 'Type 2']].value_counts().head(1))

#09 한번씩만 존재하는 (Type1 , Type2)의 쌍의 갯수는 몇개인가?
target = df[['Type 1', 'Type 2']].value_counts()
ans = len(target[target == 1])
print(ans)

#10 한번씩만 존재하는 (Type1 , Type2)의 쌍을 각 세대(Generation)은 각각 몇개씩 가지고 있는가?
target = df[['Type 1', 'Type 2']].value_counts()
target2 = target[target == 1]
lst = []
for value in target2.reset_index().values:
    t1 = value[0]
    t2 = value[1]
    sp = df[(df['Type 1'] == t1) & (df['Type 2'] == t2)]
    lst.append(sp)
ans = pd.concat(lst).reset_index(drop = True).\
      Generation.value_counts().sort_index()
print(ans)
