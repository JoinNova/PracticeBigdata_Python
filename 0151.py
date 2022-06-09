'''
다음은 음주, 흡연가 식도암의 관계를 분석하기 위한 환자와
대조군의 데이터인 R의 esoph데이터 세트이다.
환자 수(ncases)와 대조군 수(ncontrols)를 합한
새로운 칼럼인 관측자 수(nsums)를 생성하고,
음주량과 흡연량에 따른 관측자 수(nsums)의 이원 교차표(two-way table)를 생성하여 확인하고
음주량과 흡연량에 따른 관측자 수(nsums)의 카이제곱값을 구하시오.
'''
import pandas as pd
data = 'esoph.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

df['nsums'] = df.ncases + df.ncontrols
#print(df)

from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
model = ols('nsums ~ C(tobgp) * C(alcgp)', df).fit()
print(anova_lm(model))

'''
다음은 Mass패키지의 ChickWeight 데이터 세트이다.
weight를 최소-최대 척도(Min-Max Scaling)로 변환한
결과가 0.5 이상인 레코드 수를 구하시오.
'''
import pandas as pd
data = 'ChickWeight.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(df)
#print(scaler.transform(df.weight))


'''
다음은 mlbbench 패키지의 PimaIndiansDiabetes2 데이터세트이다.
glucose, pressure, mass 컬럼의 결측값이 있는 행을 제거하고
나이(age)를 조건에 맞게 그룹화 (1:10~40세, 2:41~60세, 3:60세이상)한 후
발병률이 가장 높은 나이 그룹의 발병률을 구하시오.
(발병률 = diabetes 중 pos의 수/ 인원 수)

import pandas as pd
data = 'diabetes.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

df['new'] = df.Age/20
idx = 0
for _ in df.new:
    if _ <= 2:
        df.new[idx] = 1
    elif _ <=3:
        df.new[idx] = 2
    else:
        df.new[idx] = 3
    idx+=1
#print(df.new)
chk = df[['new', 'Outcome']]
#print(chk)
ans2 = chk.groupby('new').Outcome.sum().reset_index()
ans1 = chk.groupby('new').size().reset_index()
#print(ans2)
result1 = {}
for _ in ans1.values:
    #print(_)
    result1[_[0]] = _[1]
#print(result1)

result2 = {}
for _ in ans2.values:
    #print(_)
    result2[_[0]] = _[1]
#print(result2)

ans = [166/574 , 95/167, 7/27]
result = 0
for _ in ans:
    if _ > result:
        result = _
print(result)
'''
