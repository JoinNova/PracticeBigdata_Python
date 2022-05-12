'''
04_Apply , Map
카드이용데이터 : https://www.kaggle.com/sakshigoyal7/credit-card-customers
DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/BankChurnersUp.csv’
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/pandas/main/BankChurnersUp.csv'

#01 데이터를 로드하고 데이터 행과 열의 갯수를 출력하라
df = pd.read_csv(data)
print(type(df))
print('(행 , 열)',df.shape)
#02 Income_Category의 카테고리를 map 함수를 이용하여 다음과 같이 변경하여 newIncome 컬럼에 매핑하라
#Unknown : N Less than 40K:a40K - 60K:b60K - 80K:c80K - 120K:d120K +’ : e
dic = {
    'Unknown' : 'N',
    'Less than $40K' : 'a',
    '$40K - $60K' : 'b',
    '$60K - $80K' : 'c',
    '$80K - $120K' : 'd',
    '$120K +' : 'e'
    }
df['newIncome'] = df.Income_Category.map(lambda x: dic[x])
print(df['newIncome'].head())
#03 Income_Category의 카테고리를 apply 함수를 이용하여 다음과 같이 변경하여 newIncome 컬럼에 매핑하라
#Unknown : N Less than 40K:a40K - 60K:b60K - 80K:c80K - 120K:d120K +’ : e
def change(x):
    if x == 'Unknown':
        return 'N'
    elif x == 'Less than $40K':
        return 'a'
    elif x == '$40K - $60K':
        return 'b'
    elif x == '$60K - $80K':
        return 'c'
    elif x == '$80K - $120K':
        return 'd'
    elif x == '$120K +':
        return 'e'
df['newIncome'] = df.Income_Category.apply(change)
print(df['newIncome'].head())
#04 Customer_Age의 값을 이용하여 나이 구간을 AgeState 컬럼으로 정의하라. (0~9 : 0 , 10~19 :10 , 20~29 :20 … 각 구간의 빈도수를 출력하라
df['AgeState'] = df.Customer_Age.map(lambda x: x//10 * 10)
print(df['AgeState'].value_counts().sort_index())
#05 Education_Level의 값중 Graduate단어가 포함되는 값은 1 그렇지 않은 경우에는 0으로 변경하여 newEduLevel 컬럼을 정의하고 빈도수를 출력하라
df['newEduLevel'] = df.Education_Level.map(lambda x : 1 if 'Graduate' in x else 0)
print(df['newEduLevel'].value_counts())
#06 Credit_Limit 컬럼값이 4500 이상인 경우 1 그외의 경우에는 모두 0으로 하는 newLimit 정의하라. newLimit 각 값들의 빈도수를 출력하라
df['newLimit'] = df.Credit_Limit.map(lambda x :1 if x>=4500 else 0)
print(df['newLimit'].value_counts())
#07 Marital_Status 컬럼값이 Married 이고 Card_Category 컬럼의 값이 Platinum인 경우 1 그외의 경우에는 모두 0으로 하는 newState컬럼을 정의하라. newState의 각 값들의 빈도수를 출력하라
def check(x):
    if x.Marital_Status =='Married' and x.Card_Category == 'Platinum':
        return 1
    else:
        return 0
df['newState'] = df.apply(check, axis = 1)
print(df['newState'].value_counts())
#08 Gender 컬럼값 M인 경우 male F인 경우 female로 값을 변경하여 Gender 컬럼에 새롭게 정의하라. 각 value의 빈도를 출력하라
def change(x):
    if x =='M':
        return 'male'
    else:
        return 'female'
df['Gender'] = df.Gender.apply(change)
print(df['Gender'].value_counts())
