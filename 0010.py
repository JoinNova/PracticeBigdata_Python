#올림픽 메달리스트 정보 데이터: https://www.kaggle.com/the-guardian/olympic-games
#dataUrl =’https://raw.githubusercontent.com/Datamanim/pandas/main/winter.csv’

#01 데이터에서 한국 KOR 데이터만 추출하라
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/winter.csv')
kr = df[df.Country=='KOR']
Ans = kr
print(Ans.head())

#02 한국 올림픽 메달리스트 데이터에서 년도에 따른 medal 갯수를 데이터프레임화 하라
Ans = kr.pivot_table(index='Year',columns='Medal',aggfunc='size').fillna(0)
print(Ans)

#03 전체 데이터에서 sport종류에 따른 성별수를 구하여라
Ans = df.pivot_table(index='Sport',columns='Gender',aggfunc='size')
print(Ans)

#04 전체 데이터에서 Discipline종류에 따른 따른 Medal수를 구하여라
Ans = df.pivot_table(index='Discipline',columns='Medal',aggfunc='size')
print(Ans)
