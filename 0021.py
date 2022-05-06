'''
월드컵 출전선수 골기록 데이터
데이터 출처 :https://www.kaggle.com/darinhawley/fifa-world-cup-goalscorers-19302018(참고, 데이터 수정)
데이터 설명 : 1930 ~2018년도 월드컵 출전선수 골기록
data url = https://raw.githubusercontent.com/Datamanim/datarepo/main/worldcup/worldcupgoals.csv
'''
import pandas as pd

df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/worldcup/worldcupgoals.csv')
#print(df.head())

#01  주어진 전체 기간의 각 나라별 골득점수 상위 5개 국가와 그 득점수를 데이터프레임형태로 출력하라


from IPython.display import display
result = df.groupby('Country').sum().sort_values('Goals',ascending=False).head(5)
display(result)


#02  주어진 전체기간동안 골득점을 한 선수가 가장 많은 나라 상위 5개 국가와 그 선수 숫자를 데이터 프레임 형식으로 출력하라


result = df.groupby('Country').size().sort_values(ascending=False).head(5)
print(result)


#03  Years 컬럼은 년도 -년도 형식으로 구성되어있고, 각 년도는 4자리 숫자이다. 년도 표기가 4자리 숫자로 안된 케이스가 존재한다. 해당 건은 몇건인지 출력하라


df['yearLst'] = df.Years.str.split('-')

def checkFour(x):
    for value in x:
        if len(str(value)) != 4:
            return False
        
    return True
    
df['check'] = df['yearLst'].apply(checkFour)

result = len(df[df.check ==False])
print(result)


#04  03에서 발생한 예외 케이스를 제외한 데이터프레임을 df2라고 정의하고 데이터의 행의 숫자를 출력하라 (아래 문제부터는 df2로 풀이하겠습니다)


df2 = df[df.check ==True].reset_index(drop=True)
print(df2.shape[0])


#05  월드컵 출전횟수를 나타내는 ‘LenCup’ 컬럼을 추가하고 4회 출전한 선수의 숫자를 구하여라


df2['LenCup'] =df2['yearLst'].str.len()
result = df2['LenCup'].value_counts()[4]
print(result)


#06  Yugoslavia 국가의 월드컵 출전횟수가 2회인 선수들의 숫자를 구하여라


result = len(df2[(df2.LenCup==2) & (df2.Country =='Yugoslavia')])
print(result)


#07  2002년도에 출전한 전체 선수는 몇명인가?


result =len(df2[df2.Years.str.contains('2002')])
print(result)


#08  이름에 ‘carlos’ 단어가 들어가는 선수의 숫자는 몇 명인가? (대, 소문자 구분 x)


result = len(df2[df2.Player.str.lower().str.contains('carlos')])
print(result)


#07  월드컵 출전 횟수가 1회뿐인 선수들 중에서 가장 많은 득점을 올렸던 선수는 누구인가?


result = df2[df2.LenCup==1].sort_values('Goals',ascending=False).Player.values[0]
print(result)


#08  월드컵 출전횟수가 1회 뿐인 선수들이 가장 많은 국가는 어디인가?


result= df2[df2.LenCup==1].Country.value_counts().index[0]
print(result)




'''
서울시 따릉이 이용정보 데이터
데이터 출처 :https://www.data.go.kr/data/15051872/fileData.do(참고, 데이터 수정)
데이터 설명 : 서울특별시_공공자전거 시간대별 이용정보
data url = https://raw.githubusercontent.com/Datamanim/datarepo/main/bicycle/seoul_bi.csv'''

import pandas as pd
df =pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/bicycle/seoul_bi.csv')
print(df.head())


#01  대여일자별 데이터의 수를 데이터프레임으로 출력하고, 가장 많은 데이터가 있는 날짜를 출력하라


result = df['대여일자'].value_counts().sort_index().to_frame()
answer = result[result.대여일자  == result.대여일자.max()].index[0]

from IPython.display import display
display(result)
print(answer)


#02  각 일자의 요일을 표기하고 (‘Monday’ ~’Sunday’) ‘day_name’컬럼을 추가하고 이를 이용하여 각 요일별 이용 횟수의 총합을 데이터 프레임으로 출력하라
df['대여일자'] = pd.to_datetime(df['대여일자'])
df['day_name']  = df['대여일자'].dt.day_name()

result =  df.day_name.value_counts().to_frame()
print(result)


#03 각 요일별 가장 많이 이용한 대여소의 이용횟수와 대여소 번호를 데이터 프레임으로 출력하라


result = df.groupby(['day_name','대여소번호']).size().to_frame('size').sort_values(['day_name','size'],ascending=False).reset_index()
answer  = result.drop_duplicates('day_name',keep='first').reset_index(drop=True)
display(answer)


#04  나이대별 대여구분 코드의 (일일권/전체횟수) 비율을 구한 후 가장 높은 비율을 가지는 나이대를 확인하라. 일일권의 경우 일일권 과 일일권(비회원)을 모두 포함하라


daily = df[df.대여구분코드.isin(['일일권','일일권(비회원)'])].연령대코드.value_counts().sort_index()
total = df.연령대코드.value_counts().sort_index()

ratio = (daily /total).sort_values(ascending=False)
print(ratio)
print('max ratio age ',ratio.index[0])


#05  연령대별 평균 이동거리를 구하여라


result = df[['연령대코드','이동거리']].groupby(['연령대코드']).mean()
print(result)


#06  연령대 코드가 20대인 데이터를 추출하고,이동거리값이 추출한 데이터의 이동거리값의 평균 이상인 데이터를 추출한다.최종 추출된 데이터를 대여일자, 대여소 번호 순서로 내림차순 정렬 후 1행부터 200행까지의 탄소량의 평균을 소숫점 3째 자리까지 구하여라


tw = df[df.연령대코드 =='20대'].reset_index(drop=True)
tw_mean = tw[tw.이동거리 >= tw.이동거리.mean()].reset_index(drop=True)
tw_mean['탄소량'] =tw_mean['탄소량'].astype('float')
target =tw_mean.sort_values(['대여일자','대여소번호'], ascending=False).reset_index(drop=True).iloc[:200].탄소량
result = round(target.sum()/len(target),3)
print(result)


#07  6월 7일 ~10대의 “이용건수”의 중앙값은?


df['대여일자']  =pd.to_datetime(df['대여일자'])
result = df[(df.연령대코드 =='~10대') & (df.대여일자 ==pd.to_datetime('2021-06-07'))].이용건수.median()
print(result)


#08  평일 (월~금) 출근 시간대(오전 6,7,8시)의 대여소별 이용 횟수를 구해서 데이터 프레임 형태로 표현한 후 각 대여시간별 이용 횟수의 상위 3개 대여소와 이용횟수를 출력하라


target = df[(df.day_name.isin(['Tuesday', 'Wednesday', 'Thursday', 'Friday','Monday'])) & (df.대여시간.isin([6,7,8]))]
result = target.groupby(['대여시간','대여소번호']).size().to_frame('이용 횟수')

answer = result.sort_values(['대여시간','이용 횟수'],ascending=False).groupby('대여시간').head(3)
display(answer)


#09  이동거리의 평균 이상의 이동거리 값을 가지는 데이터를 추출하여 추출데이터의 이동거리의 표본표준편차 값을 구하여라


result  = df[df.이동거리 >= df.이동거리.mean()].reset_index(drop=True).이동거리.std()
print(result)


#10  남성(‘M’ or ‘m’)과 여성(‘F’ or ‘f’)의 이동거리값의 평균값을 구하여라


df['sex'] = df['성별'].map(lambda x: '남' if x in ['M','m'] else '여')
answer = df[['sex','이동거리']].groupby('sex').mean()
display(answer)
