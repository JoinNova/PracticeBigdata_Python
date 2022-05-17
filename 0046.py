'''
서울시 따릉이 이용정보 데이터
데이터 출처 :https://www.data.go.kr/data/15051872/fileData.do(참고, 데이터 수정)
데이터 설명 : 서울특별시_공공자전거 시간대별 이용정보
data url = https://raw.githubusercontent.com/Datamanim/datarepo/main/bicycle/seoul_bi.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/bicycle/seoul_bi.csv'
df = pd.read_csv(data)
print(type(df))
print(df.head())
print(df.columns)

#01 대여일자별 데이터의 수를 데이터프레임으로 출력하고, 가장 많은 데이터가 있는 날짜를 출력하라
rentans = df['대여일자'].value_counts().sort_index().to_frame()
print(rentans)
ans = rentans[rentans.대여일자 == rentans.대여일자.max()].index[0]
print(ans)

#02 각 일자의 요일을 표기하고 (‘Monday’ ~’Sunday’) ‘day_name’컬럼을 추가하고 이를 이용하여 각 요일별 이용 횟수의 총합을 데이터 프레임으로 출력하라
df['대여일자'] = pd.to_datetime(df['대여일자'])
df['day_name'] = df['대여일자'].dt.day_name()
ans = df.day_name.value_counts().to_frame()
print(ans)

#03 각 요일별 가장 많이 이용한 대여소의 이용횟수와 대여소 번호를 데이터 프레임으로 출력하라
ans = df.groupby(['day_name', '대여소번호']).size().to_frame('size').\
      sort_values(['day_name', 'size'], ascending = False).reset_index().\
      drop_duplicates('day_name', keep = 'first').reset_index(drop = True)
print(ans)

#04 나이대별 대여구분 코드의 (일일권/전체횟수) 비율을 구한 후 가장 높은 비율을 가지는 나이대를 확인하라. 일일권의 경우 일일권 과 일일권(비회원)을 모두 포함하라
daily = df[df.대여구분코드.isin(['일일권','일일권(비회원)'])].연령대코드.value_counts().sort_index()
total = df.연령대코드.value_counts().sort_index()
ratio = (daily / total).sort_values(ascending = False)
print(ratio)
print('max ratio age', ratio.index[0])

#05 연령대별 평균 이동거리를 구하여라
ans = df[['연령대코드', '이동거리']].groupby(['연령대코드']).mean()
print(ans)

#06 연령대 코드가 20대인 데이터를 추출하고,이동거리값이 추출한 데이터의 이동거리값의 평균 이상인 데이터를 추출한다.최종 추출된 데이터를 대여일자, 대여소 번호 순서로 내림차순 정렬 후 1행부터 200행까지의 탄소량의 평균을 소숫점 3째 자리까지 구하여라
tw = df[df.연령대코드 == '20대'].reset_index(drop = True)
tw_mean = tw[tw.이동거리 >= tw.이동거리.mean()].reset_index(drop = True)
tw_mean['탄소량'] = tw_mean['탄소량'].astype('float')
target = tw_mean.sort_values(['대여일자', '대여소번호'], ascending = False).\
         reset_index(drop = True).iloc[:200].탄소량
ans = round(target.sum()/len(target), 3)
print(ans)

#07 6월 7일 ~10대의 “이용건수”의 중앙값은?
df['대여일자'] = pd.to_datetime(df['대여일자'])
ans = df[(df.연령대코드 == '~10대') & (df.대여일자 == pd.to_datetime('2021-06-07'))].이용건수.median()
print(ans)


#08 평일 (월~금) 출근 시간대(오전 6,7,8시)의 대여소별 이용 횟수를 구해서 데이터 프레임 형태로 표현한 후 각 대여시간별 이용 횟수의 상위 3개 대여소와 이용횟수를 출력하라
target = df[(df.day_name.isin(['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Monday'])) & (df.대여시간.isin([6, 7, 8]))]
ans = target. groupby(['대여시간', '대여소번호']).size().to_frame('이용 횟수').\
      sort_values(['대여시간', '이용 횟수'], ascending = False).groupby('대여시간').head(3)
print(ans)

#09 이동거리의 평균 이상의 이동거리 값을 가지는 데이터를 추출하여 추출데이터의 이동거리의 표본표준편차 값을 구하여라
ans = df[df.이동거리 >= df.이동거리.mean()].reset_index(drop = True).이동거리.std()
print(ans)

#10 남성(‘M’ or ‘m’)과 여성(‘F’ or ‘f’)의 이동거리값의 평균값을 구하여라
df['sex'] = df['성별'].map(lambda x : '남' if x in ['M', 'm'] else '여')
ans = df[['sex', '이동거리']].groupby('sex').mean()
print(ans)
