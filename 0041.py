'''
01 Getting & Knowing Data
롤 랭킹 데이터 : https://www.kaggle.com/datasnaek/league-of-legends
DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv’
'''

import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'

#01 데이터를 로드하라. 데이터는 \t을 기준으로 구분되어있다.
df = pd.read_csv(data, sep = '\t')
print(type(df))
#02 데이터의 상위 5개 행을 출력하라
print(df.head())
#03 데이터의 행과 열의 갯수를 파악하라
print('( 행 , 열 )', df.shape)
#04 전체 컬럼을 출력하라
print(df.columns)
#05 6번째 컬럼명을 출력하라
print(df.columns[5])
#06 6번째 컬럼의 데이터 타입을 확인하라
print(df.iloc[:,5].dtype)
#07 데이터셋의 인덱스 구성은 어떤가
print(df.index)
#08 6번째 컬럼의 3번째 값은 무엇인가?
print(df.iloc[2,5])

'''
제주 날씨,인구에 따른 교통량데이터 : 출처 제주 데이터 허브
DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv’
'''

import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv'

#01 데이터를 로드하라. 컬럼이 한글이기에 적절한 처리해줘야함
df = pd.read_csv(data, encoding = 'euc-kr')
print(type(df))
#02 데이터 마지막 3개행을 출력하라
print(df.tail(3))
#03 수치형 변수를 가진 컬럼을 출력하라
print(df.select_dtypes(exclude = object).columns)
#04 범주형 변수를 가진 컬럼을 출력하라
print(df.select_dtypes(include = object).columns)
#05 각 컬럼의 결측치 숫자를 파악하라
print(df.isnull().sum())
#06 각 컬럼의 데이터수, 데이터타입을 한번에 확인하라
print(df.info())
#07 각 수치형 변수의 분포(사분위, 평균, 표준편차, 최대 , 최소)를 확인하라
print(df.describe())
#08 거주인구 컬럼의 값들을 출력하라
print(df['거주인구'])
#09 평균 속도 컬럼의 4분위 범위(IQR) 값을 구하여라
print((df['평균 속도'].quantile(0.75)) - (df['평균 속도'].quantile(0.25)))
#10 읍면동명 컬럼의 유일값 갯수를 출력하라
print(df.읍면동명.nunique())
#11 읍면동명 컬럼의 유일값을 모두 출력하라
print(df.읍면동명.unique())

'''
02 Filtering & Sorting
식당데이터 : https://github.com/justmarkham/DAT8/blob/master/data/chipotle.tsv
DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv’
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv'

#01 데이터를 로드하라.
df = pd.read_csv(data)
print(type(df))
#02 quantity컬럼 값이 3인 데이터를 추출하여 첫 5행을 출력하라
print(df[df.quantity == 3].head())
#03 quantity컬럼 값이 3인 데이터를 추출하여 index를 0부터 정렬하고 첫 5행을 출력하라
print(df[df.quantity == 3].reset_index(drop = True).head())
#04 quantity , item_price 두개의 컬럼으로 구성된 새로운 데이터 프레임을 정의하라
print(df[['quantity', 'item_price']].head())
#05 item_price 컬럼의 달러표시 문자를 제거하고 float 타입으로 저장하여 new_price 컬럼에 저장하라
df['new_price'] = df['item_price'].str[1:].astype(float)
print(df['new_price'].head())
#06 new_price 컬럼이 5이하의 값을 가지는 데이터프레임을 추출하고, 전체 갯수를 구하여라
print(len(df[df.new_price<=5]))
#07 item_name명이 Chicken Salad Bowl 인 데이터 프레임을 추출하라고 index 값을 초기화 하여라
print(df[df.item_name == 'Chicken Salad Bowl'].reset_index(drop = True))
#08 new_price값이 9 이하이고 item_name 값이 Chicken Salad Bowl 인 데이터 프레임을 추출하라
print(df[(df.new_price <= 9) & (df.item_name == 'Chicken Salad Bowl')])
#09 df의 new_price 컬럼 값에 따라 오름차순으로 정리하고 index를 초기화 하여라
print(df.sort_values('new_price').reset_index(drop = True))
#10 df의 item_name 컬럼 값중 Chips 포함하는 경우의 데이터를 출력하라
print(df[df.item_name.str.contains('Chips')])
#11 df의 짝수번째 컬럼만을 포함하는 데이터프레임을 출력하라
print(df.iloc[:,::2])
#12 df의 new_price 컬럼 값에 따라 내림차순으로 정리하고 index를 초기화 하여라
print(df.sort_values('new_price', ascending = False).reset_index(drop = True))
#13 df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 인덱싱하라
print(df[(df.item_name == 'Steak Salad') | (df.item_name == 'Bowl')])
#14 df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 첫번째 케이스만 남겨라
print(df[(df.item_name == 'Steak Salad') | (df.item_name == 'Bowl')].drop_duplicates('item_name'))
#15 df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 마지막 케이스만 남겨라
print(df[(df.item_name == 'Steak Salad') | (df.item_name == 'Bowl')].drop_duplicates('item_name', keep = 'last'))
#16 df의 데이터 중 new_price값이 new_price값의 평균값 이상을 가지는 데이터들을 인덱싱하라
print(df[df.new_price >= df.new_price.mean()])
#17 df의 데이터 중 item_name의 값이 Izze 데이터를 Fizzy Lizzy로 수정하라
df[df.item_name == 'Izze'] = 'Fizzy Lizzy'
print(df['item_name'])
#18 df의 데이터 중 choice_description 값이 NaN 인 데이터의 갯수를 구하여라
print(df.choice_description.isnull().sum())
#19 df의 데이터 중 choice_description 값이 NaN 인 데이터를 NoData 값으로 대체하라(loc 이용)
df.loc[df.choice_description.isnull(), 'choice_description'] = 'NoData'
print(df['choice_description'].head())
#20 df의 데이터 중 choice_description 값에 Black이 들어가는 경우를 인덱싱하라
print(df[df.choice_description.str.contains('Black')]['choice_description'].head())
#21 df의 데이터 중 choice_description 값에 Vegetables 들어가지 않는 경우의 갯수를 출력하라
print(len(df[~df.choice_description.str.contains('Vegetables')]['choice_description']))
#22 df의 데이터 중 item_name 값이 N으로 시작하는 데이터를 모두 추출하라
print(df[df.item_name.str.startswith('N')]['item_name'])
#23 df의 데이터 중 item_name 값의 단어갯수가 15개 이상인 데이터를 인덱싱하라
print(df[df.item_name.str.len() >= 15 ]['item_name'])
#24 df의 데이터 중 new_price값이 lst에 해당하는 경우의 데이터 프레임을 구하고 그 갯수를 출력하라
lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
print(len(df.loc[df.new_price.isin(lst)]))
