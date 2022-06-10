'''
데이터 출처 : link (후처리 작업)
데이터 설명 : 2010-2019 스포티파이 TOP100 노래
dataurl : https://raw.githubusercontent.com/Datamanim/datarepo/main/spotify/spotify.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/spotify/spotify.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

#01 데이터는 현재 년도별 100곡이 인기순으로 정렬되어 있다. 각 년도별 1~100위의 랭킹을 나타내는 rank컬럼을 만들고 매년도 1위의 bpm컬럼의 평균값을 구하여라
df = df.dropna()
df['rank'] = list(range(1, 101))*10
#print(df)
ans = df[df['rank'] == 1].bpm.mean()
print(ans)

#02 2015년도에 가장많은 top100곡을 올린 artist는 누구인가?
chk = df[df['top year'] == 2015].value_counts('artist').sort_values(ascending = False).reset_index()
chk2, ans = 0, []
for _ in chk.values:
    if _[1] >= chk2:
        ans.append(_[0])
        chk2 = _[1]
print(*ans, sep = ',')

#03 년도별 rank값이 1~10위 까지의 곡들 중 두번째로 많은 top genre는 무엇인가?
ans = df[df['rank'] < 11].value_counts('top genre').sort_values(ascending = False).index[1]
print(ans)

#04 피처링의 경우 title에 표시된다. 피처링을 가장 많이 해준 가수는 누구인가?
ans = df.title.str.split('\(feat.').str[1].dropna().str[:-1].str.strip().value_counts().index[0]
print(ans)

#05 top year 년도를 기준으로 발매일(year released)과 top100에 진입한 일자 (top year)가 다른 곡의 숫자를 count 했을때 가장 많은 년도는?
ans = df[df['top year'] != df['year released']].value_counts('top year').sort_values(ascending = False).index[0]
print(int(ans))

#06 artist 컬럼의 값에 대소문자 상관없이 q 단어가 들어가는 아티스트는 몇명인가?
ans = df[df.artist.str.lower().str.contains('q')].artist.nunique()
print(ans)

#07 년도 상관없이 전체데이터에서 1~50위와 51~100위간의 dur 컬럼의 평균값의 차이는?
ans = abs(df[df['rank'] < 51].dur.mean() - df[df['rank'] > 50].dur.mean())
print(ans)

#08 title을 띄어쓰기 단어로 구분 했을때 가장 많이 나온 단어는 무엇인가? (대소문자 구분 x)
#ans = df.title.str.split(' ').dropna().explode().str.lower().value_counts().index[1]
ans = df.title.str.split('\(feat').str[0].str.split().explode().str.lower().value_counts().index[0]
print(ans)

#09 년도별 nrgy값의 평균값을 구할때 최대 평균값과 최소 평균값의 차이를 구하여라
chk = df.groupby('top year').nrgy.mean().sort_values(ascending = False)
#print(chk)
ans = chk.values[0] - chk.values[-1]
print(ans)

#10 artist중 artist type 타입을 여러개 가지고 있는 artist는 누구인가
chk = df[['artist', 'artist type']].value_counts().reset_index().artist.value_counts().index[0]
print(chk)
