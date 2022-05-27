'''
데이터 출처 : https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset (후처리 작업)
데이터 설명 : 뇌졸증 발생여부 예측
dataurl : https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke/train.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv'
df = pd.read_csv(data)#.sort_values('age')
df = df.drop([586])
#print(df.head(587))
#print(df.info())

#01 성별이 Male인 환자들의 age의 평균값은 ?'
df.age = df.age.astype('float')
ans = df[df.gender == 'Male']
print(ans.age.mean())

#02 bmi컬럼의 결측치를 bmi컬럼의 결측치를 제외한 나머지 값들의 중앙값으로 채웠을 경우 bmi 컬럼의 평균을 소숫점 이하 3자리 까지 구하여라
#df2 = df.sort_values('bmi')
df2 = df
print(df2['bmi'].isnull().value_counts())
df2 = df2.sort_values('bmi')
#print(df2['bmi'])
#print(df2['bmi'].median())

df2['bmi'] = df2['bmi'].fillna(df2['bmi'].median())
#print(df2['bmi'])
ans = round(df2['bmi'].mean(),3)
print(ans)
'''
#03 bmi컬럼의 각 결측치들을 직전의 행의 bmi값으로 채웠을 경우 bmi 컬럼의 평균을 소숫점 이하 3자리 까지 구하여라
df2 = df
#df2 = df2.sort_values('bmi')
#print(df2['bmi'])
print(df2['bmi'].isnull().value_counts())

#print(df2['bmi'].median())

df2['bmi'] = df2['bmi'].fillna(method = 'pad')
#print(df2['bmi'])
#print(df2['bmi'].isnull().value_counts())
ans = round(df2['bmi'].mean(),3)
print(ans)
'''
#04 bmi컬럼의 각 결측치들을 결측치를 가진 환자 나이대(10단위)의 평균 bmi 값으로 대체한 후 대체된 bmi 컬럼의 평균을 소숫점 이하 3자리 까지 구하여라
df3 = df
#df2 = df2.sort_values('bmi')
#print(df2['bmi'])
print(df3['bmi'].isnull().value_counts())
df3['newage'] = df3.age//10*10
#print(df2)
chk = df3.groupby(['newage', 'bmi']).size()
#print(chk)
#df2['bmi'] = df2['bmi'].fillna()
df3['bmi'] = df3['bmi'].interpolate(method = 'linear' , limit_direction = 'forward')
#print(df2['bmi'])
#print(df2['bmi'].isnull().value_counts())
ans = round(df3['bmi'].mean(),3)
print(ans)
