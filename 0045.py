'''
월드컵 출전선수 골기록 데이터
데이터 출처 :https://www.kaggle.com/darinhawley/fifa-world-cup-goalscorers-19302018(참고, 데이터 수정)
데이터 설명 : 1930 ~2018년도 월드컵 출전선수 골기록
data url = https://raw.githubusercontent.com/Datamanim/datarepo/main/worldcup/worldcupgoals.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/worldcup/worldcupgoals.csv'
df = pd.read_csv(data)
print(type(df))
print(df.head())
print(df.columns)

#01 주어진 전체 기간의 각 나라별 골득점수 상위 5개 국가와 그 득점수를 데이터프레임형태로 출력하라
ans = df.groupby('Country').sum().sort_values('Goals', ascending = False).head()
print(ans)

#02 주어진 전체기간동안 골득점을 한 선수가 가장 많은 나라 상위 5개 국가와 그 선수 숫자를 데이터 프레임 형식으로 출력하라
ans = df.groupby('Country').size().sort_values(ascending = False).head()
print(ans)

#03 Years 컬럼은 년도 -년도 형식으로 구성되어있고, 각 년도는 4자리 숫자이다. 년도 표기가 4자리 숫자로 안된 케이스가 존재한다. 해당 건은 몇건인지 출력하라
df['yearLst'] = df.Years.str.split('-')
def chkFour(x):
    for value in x:
        if len(str(value)) != 4:
            return False
    return True
df['check'] = df['yearLst'].apply(chkFour)
ans = len(df[df.check == False])
print(ans)

#04 **Q3에서 발생한 예외 케이스를 제외한 데이터프레임을 df2라고 정의하고 데이터의 행의 숫자를 출력하라 (아래 문제부터는 df2로 풀이하겠습니다) **
df2 = df[df.check == True].reset_index(drop = True)
print(df2.shape[0])

#05 월드컵 출전횟수를 나타내는 ‘LenCup’ 컬럼을 추가하고 4회 출전한 선수의 숫자를 구하여라
df2['LenCup'] = df2['yearLst'].str.len()
ans = df2['LenCup'].value_counts()[4]
print(ans)

#06 Yugoslavia 국가의 월드컵 출전횟수가 2회인 선수들의 숫자를 구하여라
ans = len(df2[(df2.LenCup == 2) & (df2.Country == 'Yugoslavia')])
print(ans)

#07 2002년도에 출전한 전체 선수는 몇명인가?
ans = len(df2[df2.Years.str.contains('2002')])
print(ans)

#08 이름에 ‘carlos’ 단어가 들어가는 선수의 숫자는 몇 명인가? (대, 소문자 구분 x)
ans = len(df2[df2.Player.str.lower().str.contains('carlos')])
print(ans)

#09 월드컵 출전 횟수가 1회뿐인 선수들 중에서 가장 많은 득점을 올렸던 선수는 누구인가?
ans = df2[df2.LenCup == 1].sort_values('Goals', ascending = False).Player.values[0]
print(ans)

#10 월드컵 출전횟수가 1회 뿐인 선수들이 가장 많은 국가는 어디인가?
ans = df2[df2.LenCup == 1].Country.value_counts().index[0]
print(ans)
