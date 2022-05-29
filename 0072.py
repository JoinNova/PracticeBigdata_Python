'''
데이터 출처 : https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset (후처리 작업)
데이터 설명 : 뇌졸증 발생여부 예측
dataurl : https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke/train.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv'
df = pd.read_csv(data)
#print(df.head())

#01 성별이 Male인 환자들의 age의 평균값은 ?
ans = df[df.gender == 'Male'].age.str.replace('*', '').astype('int64').mean()
print(ans)
#02 bmi컬럼의 결측치를 bmi컬럼의 결측치를 제외한 나머지 값들의 중앙값으로 채웠을 경우 bmi 컬럼의 평균을 소숫점 이하 3자리 까지 구하여라
ans = df.bmi.fillna(df.bmi.median()).mean()
print(round(ans, 3))
#03 bmi컬럼의 각 결측치들을 직전의 행의 bmi값으로 채웠을 경우 bmi 컬럼의 평균을 소숫점 이하 3자리 까지 구하여라
ans = df.bmi.fillna(method = 'ffill').mean()
#ans = df.bmi.fillna(method = 'bfill').mean()
print(round(ans, 3))
#04 bmi컬럼의 각 결측치들을 결측치를 가진 환자 나이대(10단위)의 평균 bmi 값으로 대체한 후 대체된 bmi 컬럼의 평균을 소숫점 이하 3자리 까지 구하여라
df['age'] = df.age.str.replace('*', '').astype('int64')
chk = df[df.bmi.notnull()].groupby(df.age//10*10).bmi.mean()
print(chk)
dic = {x:y for x,y in chk.items()}
print(dic)
##idx = df.loc[df.bmi.isnull(), ['age', 'bmi']].index
##print(idx)
df.loc[df.bmi.isnull(), 'bmi'] = (df[df.bmi.isnull()].age//10*10).map(lambda x: dic[x])
ans = df.bmi.mean()
print(round(ans, 3))

#05 **avg_glucose_level 컬럼의 값이 200이상인 데이터를 모두 199로 변경하고 stroke값이 1인 데이터의 avg_glucose_level값의 평균을 소수점이하 3자리 까지 구하여라 **
df.loc[df.avg_glucose_level >= 200, 'avg_glucose_level'] = 199
ans = df[df.stroke == 1].avg_glucose_level.mean()
print(round(ans, 3))

'''
데이터 출처 : https://www.kaggle.com/abcsds/pokemon (참고, 데이터 수정)
데이터 설명 : 포켓몬 정보
data url = https://raw.githubusercontent.com/Datamanim/datarepo/main/pok/Pokemon.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/pok/Pokemon.csv'
df = pd.read_csv(data)
#print(df.head())
#print(df.info())

#01 Attack컬럼의 값을 기준으로 내림차순정렬 했을때 상위 400위까지 포켓몬들과 401~800위까지의 포켓몬들에서 전설포켓몬(Legendary컬럼)의 숫자 차이는?
chk = df.sort_values('Attack', ascending = False)
#print(chk['Attack'])
ans = chk.head(400).Legendary.sum() - chk[400:800].Legendary.sum()
print(ans)

#02 Type 1 컬럼의 종류에 따른 Total 컬럼의 평균값을 내림차순 정렬했을때 상위 3번째 Type 1은 무엇인가?
chk = df.groupby(['Type 1']).Total.mean().sort_values(ascending = False)
print(chk.index[2])

#03 결측치가 존재하는 행을 모두 지운 후 처음부터 순서대로 60% 데이터를 추출하여 Defense컬럼의 1분위수를 구하여라
print(df.isnull().sum())
chk = df.dropna()
print(chk.isnull().sum())
ans = chk.head(int(len(chk)*0.6))
print(ans.Defense.quantile(0.25))

#04 Type 1 컬럼의 속성이 Fire인 포켓몬들의 Attack의 평균이상인 Water속성의 포켓몬 수를 구하여라
chk = df[df['Type 1'] == 'Fire'].Attack.mean()
ans = df[(df.Attack >= chk) & (df['Type 1'] == 'Water')]
print(len(ans))

target = df[df.Attack >= df[df['Type 1'] =='Fire'].Attack.mean()]
result = target[target['Type 1']=='Water'].shape[0]
print(result)

#05 각 세대 중(Generation 컬럼)의 Speed와 Defense 컬럼의 차이(절댓값)이 가장 큰 세대는?
df['gap'] = abs(df.Speed - df.Defense)
print(df.head())
ans = df.groupby('Generation').gap.mean().sort_values(ascending = False)
print(ans.index[0])
