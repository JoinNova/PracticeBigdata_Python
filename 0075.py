'''
데이터 출처 : https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset (후처리 작업)
데이터 설명 : 뇌졸증 발생여부 예측
dataurl : https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv'
df = pd.read_csv(data)
#print(df.head())
#print(df.info())

#01 성별이 Male인 환자들의 age의 평균값은 ?
df['age'] = df.age.str.replace('*', '').astype('int64')
#print(df.age.sort_values())
ans = df[df.gender == 'Male'].age.mean()
print(ans)

#02 bmi컬럼의 결측치를 bmi컬럼의 결측치를 제외한 나머지 값들의 중앙값으로 채웠을 경우 bmi 컬럼의 평균을 소숫점 이하 3자리 까지 구하여라
print(df.bmi.isnull().sum())
df['bmi'] = df['bmi'].fillna(df.bmi.median())
print(df.bmi.isnull().sum())
ans = round(df.bmi.mean(), 3)
print(ans)

#03 bmi컬럼의 각 결측치들을 직전의 행의 bmi값으로 채웠을 경우 bmi 컬럼의 평균을 소숫점 이하 3자리 까지 구하여라
df = pd.read_csv(data)
df['bmi'] = df.bmi.fillna(method = 'ffill')
ans = round(df.bmi.mean(), 3)
print(ans)

#04 bmi컬럼의 각 결측치들을 결측치를 가진 환자 나이대(10단위)의 평균 bmi 값으로 대체한 후 대체된 bmi 컬럼의 평균을 소숫점 이하 3자리 까지 구하여라
df = pd.read_csv(data)
df['age'] = df.age.str.replace('*', '').astype('int64')
df['age2'] = df['age']//10*10
chk = df[df.bmi.isnull()]
#print(len(chk))
#print(df.age2)
dic = {}
for _ in df.groupby('age2')[['bmi']].mean().reset_index().values:
    dic[int(_[0])] = _[1]
#print(df[df.bmi.isnull()][['age', 'age2', 'bmi']].head())
#print(df.bmi.isnull().sum())
df.loc[df.bmi.isnull(), 'bmi'] = df[df.bmi.isnull()]['age2'].map(lambda x : dic[x])
#print(df['bmi'])
#print(df.bmi.isnull().sum())
ans = round(df.bmi.mean(), 3)
print(ans)

'''
chk = df[df.bmi.isnull()]
#print(chk)

section = df.groupby('age').bmi.mean().reset_index().values
#print(section)
dic = {}
for _ in section:
    #print(_)
    dic[int(_[0])] = _[1]
#print(dic)
#print(chk['age'])
df.loc[df.bmi,'bmi'] = df['age'].map(lambda x: dic(x))
#ans = round(df.bmi.mean(), 3)
#print(ans)
'''

#05 **avg_glucose_level 컬럼의 값이 200이상인 데이터를 모두 199로 변경하고 stroke값이 1인 데이터의 avg_glucose_level값의 평균을 소수점이하 3자리 까지 구하여라 **
df.loc[df.avg_glucose_level >= 200,'avg_glucose_level'] = 199
ans = round(df[df.stroke == 1].avg_glucose_level.mean(), 3)
print(ans)
