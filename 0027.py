'''
서울시 미세먼지 데이터 : https://www.airkorea.or.kr/web/realSearch?pMENU_NO=97
DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/seoul_pm.csv’
'''
data = 'https://raw.githubusercontent.com/Datamanim/pandas/main/seoul_pm.csv'
import pandas as pd
df = pd.read_csv(data)

#01 년-월-일:시 컬럼을 pandas에서 인식할 수 있는 datetime 형태로 변경하라. 서울시의 제공데이터의 경우 0시가 24시로 표현된다
import datetime
def change(x) :
    hour = x.split(':')[1]
    date = x.split(':')[0]
    if hour == '24':
        hour = '00:00:00'
        result = pd.to_datetime(date + ' ' + hour) + datetime.timedelta(days = 1)
    else :
        hour = hour + ':00:00'
        result = pd.to_datetime(date + ' ' + hour)
    return result
df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change)
print(df.head())

#02 일자별 영어요일 이름을 dayName 컬럼에 저장하라
df = pd.read_csv(data)
import datetime
def change(x) :
    hour = x.split(':')[1]
    date = x.split(':')[0]
    if hour == '24' :
        hour = '00:00:00'
        result = pd.to_datetime(date + ' ' + hour) + datetime.timedelta(days = 1)
    else :
        hour = hour + ':00:00'
        result = pd.to_datetime(date + ' ' + hour)
    return result
df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change)
df['dayName'] = df['(년-월-일:시)'].dt.day_name()
ans = df['dayName']
print(ans)

#03 일자별 각 PM10등급의 빈도수를 파악하라
df = pd.read_csv(data)
import datetime
def change(x) :
    hour = x.split(':')[1]
    date = x.split(':')[0]
    if hour == '24' :
        hour = '00:00:00'
        result = pd.to_datetime(date + ' ' + hour) + datetime.timedelta(days = 1)
    else :
        hour = hour + ':00:00'
        result = pd.to_datetime(date + ' ' + hour)
    return result
df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change)
df['dayName'] = df['(년-월-일:시)'].dt.day_name()

ans = df.groupby(['dayName', 'PM10등급'], as_index = False).size()
ans = ans.pivot(index = 'dayName', columns = 'PM10등급', values = 'size').fillna(0)
print(ans)

#04 시간이 연속적으로 존재하며 결측치가 없는지 확인하라
df = pd.read_csv(data)
import datetime
def change(x) :
    hour = x.split(':')[1]
    date = x.split(':')[0]
    if hour == '24' :
        hour = '00:00:00'
        result = pd.to_datetime(date + ' ' + hour) + datetime.timedelta(days = 1)
    else :
        hour = hour + ':00:00'
        result = pd.to_datetime(date + ' '+ hour)
    return result
df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change)
df['dayName'] = df['(년-월-일:시)'].dt.day_name()
check = len(df['(년-월-일:시)'].diff().unique())
if check == 2:
    ans = True
else :
    ans = False
print(ans)

#05 오전 10시와 오후 10시(22시)의 PM10의 평균값을 각각 구하여라
df = pd.read_csv(data)
import datetime
def change(x) :
    hour = x.split(':')[1]
    date = x.split(':')[0]
    if hour == '24' :
        hour = '00:00:00'
        result = pd.to_datetime(date + ' ' + hour) + datetime.timedelta(days = 1)
    else :
        hour =hour + ':00:00'
        result = pd.to_datetime(date + ' ' + hour)
    return result
df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change)
df['dayName'] = df['(년-월-일:시)'].dt.day_name()
ans = df.groupby(df['(년-월-일:시)'].dt.hour).mean().iloc[[10,22],[0]]
print(ans)

#06 날짜 컬럼을 index로 만들어라
df = pd.read_csv(data)
import datetime
def change(x) :
    hour = x.split(':')[1]
    date = x.split(':')[0]
    if hour == '24':
        hour = '00:00:00'
        result = pd.to_datetime(date + ' ' + hour) + datetime.timedelta(days = 1)
    else :
        hour = hour + ':00:00'
        result = pd.to_datetime(date + ' ' + hour)
    return result
df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change)
df['dayName'] = df['(년-월-일:시)'].dt.day_name()
df.set_index('(년-월-일:시)', inplace = True, drop = True)
print(df.head())

#07 데이터를 주단위로 뽑아서 최소,최대 평균, 표준표차를 구하여라
df = pd.read_csv(data)
import datetime
def change(x) :
    hour = x.split(':')[1]
    date = x.split(':')[0]
    if hour == '24':
        hour = '00:00:00'
        result = pd.to_datetime(date + ' ' + hour) + datetime.timedelta(days = 1)
    else :
        hour = hour + ':00:00'
        result = pd.to_datetime(date + ' ' + hour)
    return result
df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change)
df['dayName'] = df['(년-월-일:시)'].dt.day_name()
df.set_index('(년-월-일:시)', inplace = True, drop = True)
ans = df.resample('W').agg(['min','max','mean','std'])
print(ans)
