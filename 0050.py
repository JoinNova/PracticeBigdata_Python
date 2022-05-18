'''
대한민국 체력장 데이터
데이터 출처 : 국민체육진흥공단 (문화 빅데이터플랫폼) (참고, 데이터 수정)
데이터 설명 : 대한민국 국민 체력장 평가
data url = https://raw.githubusercontent.com/Datamanim/datarepo/main/body/body.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/body/body.csv'
df= pd.read_csv(data)
print(type(df))
print(df.head())
print(df.columns)

#01 전체데이터의 수축기혈압(최고) - 이완기혈압(최저)의 평균을 구하여라
ans = (df['수축기혈압(최고) : mmHg'] - df['이완기혈압(최저) : mmHg']).mean()
print(ans)

#02 50~59세의 신장평균을 구하여라
ans = df[(df.측정나이 < 60) & (df.측정나이 >= 50)].iloc[:,2].mean()
print(ans)

#03 연령대 (20~29 : 20대 …) 별 인원수를 구하여라
df['연령대'] = df.측정나이 //10 *10
ans = df['연령대'].value_counts()
print(ans)

#04 연령대 (20~29 : 20대 …) 별 등급의 숫자를 데이터 프레임으로 표현하라
ans = df.groupby(['연령대', '등급'], as_index = False).size()
print(ans)

#05 남성 중 A등급과 D등급의 체지방률 평균의 차이(큰 값에서 작은 값의 차)를 구하여라
ans = abs(df[(df.측정회원성별 == 'M') & (df.등급 == 'A')].iloc[:, 4].mean() -\
          df[(df.측정회원성별 == 'M') & (df.등급 == 'D')].iloc[:, 4].mean())
print(ans)

#06 여성 중 A등급과 D등급의 체중의 평균의 차이(큰 값에서 작은 값의 차)를 구하여라
ans = abs(df[(df.측정회원성별 == 'F') & (df.등급 == 'A')].iloc[:, 3].mean()-\
          df[(df.측정회원성별 == 'F') & (df.등급 == 'D')].iloc[:, 3].mean())
print(ans)

#07 bmi는 자신의 몸무게(kg)를 키의 제곱(m)으로 나눈값이다. 데이터의 bmi 를 구한 새로운 컬럼을 만들고 남성의 bmi 평균을 구하여라
df['bmi'] = df['체중 : kg'] / (df['신장 : cm']/100)**2
ans = df[df.측정회원성별 == 'M'].bmi.mean()
print(ans)

#08 bmi보다 체지방율이 높은 사람들의 체중평균을 구하여라
print(df[df.bmi < df['체지방율 : %']]['체중 : kg'].mean())

#09 남성과 여성의 악력 평균의 차이를 구하여라
ans = df.groupby('측정회원성별')['악력D : kg'].mean()
print(ans.M - ans.F)

#10 남성과 여성의 교차윗몸일으키기 횟수의 평균의 차이를 구하여라
print(df.head())
print(df.columns)
ans = df.groupby('측정회원성별')['교차윗몸일으키기 : 회'].mean()
print(ans.M - ans.F)
