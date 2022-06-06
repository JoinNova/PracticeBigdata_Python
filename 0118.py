'''
데이터 출처 : https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset (후처리 작업)
데이터 설명 : 뇌졸증 발생여부 예측
dataurl : https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())

#01 성별이 Male인 환자들의 age의 평균값은 ?
print(df.age.sort_values())
df.age = df.age.str.replace('*', '').astype('int')
ans = df[df.gender == 'Male'].age.mean()
print(ans)

#02 bmi컬럼의 결측치를 bmi컬럼의 결측치를 제외한 나머지 값들의 중앙값으로 채웠을 경우 bmi 컬럼의 평균을 소숫점 이하 3자리 까지 구하여라
ans = df.bmi.fillna(df.bmi.median()).mean()
print(round(ans, 3))

#03 bmi컬럼의 각 결측치들을 직전의 행의 bmi값으로 채웠을 경우 bmi 컬럼의 평균을 소숫점 이하 3자리 까지 구하여라
ans = df.bmi.fillna(method = 'ffill').mean()
print(round(ans, 3))

#04 bmi컬럼의 각 결측치들을 결측치를 가진 환자 나이대(10단위)의 평균 bmi 값으로 대체한 후 대체된 bmi 컬럼의 평균을 소숫점 이하 3자리 까지 구하여라
df['sec'] = df.age//10*10
chk = df.groupby(['sec']).bmi.mean().reset_index()
print(chk)
dic = {}
for _ in chk.values:
    dic[_[0]] = _[1]
print(dic)
print(df[df.bmi.isnull()]['sec'])
print(df.loc[df.bmi.isnull(), 'sec'])
df.loc[df.bmi.isnull(), 'bmi'] = df[df.bmi.isnull()]['sec'].map(lambda _ : dic[_])
ans = df.bmi.mean()
print(round(ans, 3))

#05 avg_glucose_level 컬럼의 값이 200이상인 데이터를 모두 199로 변경하고 stroke값이 1인 데이터의 avg_glucose_level값의 평균을 소수점이하 3자리 까지 구하여라
df.loc[df.avg_glucose_level >= 200, 'avg_glucose_level'] = 199
ans = df[df.stroke == 1].avg_glucose_level.mean()
print(round(ans, 3))
