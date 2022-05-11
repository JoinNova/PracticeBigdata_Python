'''
02 Filtering & Sorting
식당데이터 : https://github.com/justmarkham/DAT8/blob/master/data/chipotle.tsv
DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv’
'''
import pandas as pd
data ='https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv' 

#01 데이터를 로드하라.
df = pd.read_csv(data)
print(type(df))
print(df.head())
#02 quantity컬럼 값이 3인 데이터를 추출하여 첫 5행을 출력하라
print(df[(df.quantity == 3)].head())
#03 quantity컬럼 값이 3인 데이터를 추출하여 index를 0부터 정렬하고 첫 5행을 출력하라
print(df[(df.quantity == 3)].reset_index(drop = True).head())
#04 quantity , item_price 두개의 컬럼으로 구성된 새로운 데이터 프레임을 정의하라
ans = df[['quantity', 'item_price']]
print(ans.head())
#05 item_price 컬럼의 달러표시 문자를 제거하고 float 타입으로 저장하여 new_price 컬럼에 저장하라
df['new_price'] = df.item_price.str[1:].astype('float')
ans = df['new_price']
print(ans.head())
#06 new_price 컬럼이 5이하의 값을 가지는 데이터프레임을 추출하고, 전체 갯수를 구하여라
ans = df.loc[df.new_price <= 5]
#print(ans.head())
print(len(ans))
#07 item_name명이 Chicken Salad Bowl 인 데이터 프레임을 추출하라고 index 값을 초기화 하여라
ans = df[df.item_name == 'Chicken Salad Bowl'].reset_index(drop = True)
print(ans.head())
#08 new_price값이 9 이하이고 item_name 값이 Chicken Salad Bowl 인 데이터 프레임을 추출하라
ans = df[(df.new_price <=9 ) & (df.item_name == 'Chicken Salad Bowl')]
print(ans.head())
#09 df의 new_price 컬럼 값에 따라 오름차순으로 정리하고 index를 초기화 하여라
ans = df.sort_values('new_price').reset_index(drop = True)
print(ans.head())
#10 df의 item_name 컬럼 값중 Chips 포함하는 경우의 데이터를 출력하라
ans = df.loc[df.item_name.str.contains('Chips')]
print(ans.head())
#11 df의 짝수번째 컬럼만을 포함하는 데이터프레임을 출력하라
ans = df.iloc[:,::2]
print(ans.head())
#12 df의 new_price 컬럼 값에 따라 내림차순으로 정리하고 index를 초기화 하여라
ans = df.sort_values('new_price',ascending = False).reset_index(drop = True)
print(ans)
#13 df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 인덱싱하라
ans = df[(df.item_name == 'Steak Salad') | (df.item_name == 'Bowl')]
print(ans)
#14 df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 첫번째 케이스만 남겨라
ans = df[(df.item_name == 'Steak Salad') | (df.item_name == 'Bowl')].drop_duplicates('item_name')
print(ans)
#15 df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 마지막 케이스만 남겨라
ans = df[(df.item_name == 'Steak Salad') | (df.item_name == 'Bowl')].drop_duplicates('item_name', keep = 'last')
print(ans)
#16 df의 데이터 중 new_price값이 new_price값의 평균값 이상을 가지는 데이터들을 인덱싱하라
ans = df.loc[df.new_price >= df.new_price.mean()]
print(ans.head())
#17 df의 데이터 중 item_name의 값이 Izze 데이터를 Fizzy Lizzy로 수정하라
df.loc[df.item_name =='Izze', 'item_name'] = 'Fizzy Lizzy'
ans = df.item_name
print(ans.head())
#18 df의 데이터 중 choice_description 값이 NaN 인 데이터의 갯수를 구하여라
ans = df.choice_description.isnull().sum()
print(ans)
#19 df의 데이터 중 choice_description 값이 NaN 인 데이터를 NoData 값으로 대체하라(loc 이용)
df.loc[df.choice_description.isnull(),'choice_description'] ='NoData'
print(df.choice_description.head())
#20 df의 데이터 중 choice_description 값에 Black이 들어가는 경우를 인덱싱하라
ans = df.loc[df.choice_description.str.contains('Black')]
print(ans.choice_description.head())
#21 df의 데이터 중 choice_description 값에 Vegetables 들어가지 않는 경우의 갯수를 출력하라
ans = df.loc[~df.choice_description.str.contains('Vegetables')]
print(len(ans))
#22 df의 데이터 중 item_name 값이 N으로 시작하는 데이터를 모두 추출하라
ans = df[df.item_name.str.startswith('N')]
print(ans.item_name.head())
#23 df의 데이터 중 item_name 값의 단어갯수가 15개 이상인 데이터를 인덱싱하라
ans = df.loc[df.item_name.str.len() >= 15]
print(ans.item_name.head())
#24 df의 데이터 중 new_price값이 lst에 해당하는 경우의 데이터 프레임을 구하고 그 갯수를 출력하라
lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
ans = df.loc[df.new_price.isin(lst)]
print(ans.new_price.head())
print(len(ans))
