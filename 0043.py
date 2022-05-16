'''
유튜브 인기동영상 데이터
데이터 출처 :https://www.kaggle.com/rsrishav/youtube-trending-video-dataset?select=KR_youtube_trending_data.csv
데이터 설명 : 유튜브 데일리 인기동영상 (한국)
dataurl : https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv
'''
import pandas as pd
data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv'
df = pd.read_csv(data, index_col = 0)
print(type(df))
print(df.head())
print(df.columns)

#01 인기동영상 제작횟수가 많은 채널 상위 10개명을 출력하라 (날짜기준, 중복포함)
ans = list(df.loc[df.channelId.isin(df.channelId.value_counts().head(10).index)].channelTitle.unique())
print(ans)

#02 논란으로 인기동영상이 된 케이스를 확인하고 싶다. dislikes수가 like 수보다 높은 동영상을 제작한 채널을 모두 출력하라
ans = list(df.loc[df.likes < df.dislikes].channelTitle.unique())
print(ans)

#03 채널명을 바꾼 케이스가 있는지 확인하고 싶다. channelId의 경우 고유값이므로 이를 통해 채널명을 한번이라도 바꾼 채널의 갯수를 구하여라
change = df[['channelTitle', 'channelId']].drop_duplicates().channelId.value_counts()
target = change[change>1]
print(len(target))

#04 일요일에 인기있었던 영상들중 가장많은 영상 종류(categoryId)는 무엇인가?
df['trending_date2'] = pd.to_datetime(df['trending_date2'])
ans = df.loc[df['trending_date2'].dt.day_name() == 'Sunday'].categoryId.value_counts().index[0]
print(ans)

#05 각 요일별 인기 영상들의 categoryId는 각각 몇개 씩인지 하나의 데이터 프레임으로 표현하라
group = df.groupby([df['trending_date2'].dt.day_name(), 'categoryId'], as_index = False).size()
ans = group.pivot(index = 'categoryId', columns = 'trending_date2')
print(ans)

#06 댓글의 수로 (comment_count) 영상 반응에 대한 판단을 할 수 있다. viewcount대비 댓글수가 가장 높은 영상을 확인하라 (view_count값이 0인 경우는 제외한다)
target2 = df.loc[df.view_count != 0]
t = target2.copy()
t['ratio'] = (target2['comment_count']/target2['view_count']).dropna()
ans = t.sort_values(by = 'ratio', ascending = False).iloc[0].title
print(ans)

#07 댓글의 수로 (comment_count) 영상 반응에 대한 판단을 할 수 있다.viewcount대비 댓글수가 가장 낮은 영상을 확인하라 (view_counts, ratio값이 0인경우는 제외한다.)
ratio = (df['comment_count']/ df['view_count']).dropna().sort_values()
ratio[ratio != 0].index[0]
ans = df.iloc[ratio[ratio != 0].index[0]].title
print(ans)

#08 like 대비 dislike의 수가 가장 적은 영상은 무엇인가? (like, dislike 값이 0인경우는 제외한다)
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

target = df.loc[(df.likes != 0) & (df.dislikes != 0)]
num = (target['dislikes']/ target['likes']).sort_values().index[0]
ans = df.iloc[num].title
print(ans.translate(non_bmp_map))

#09 가장많은 트렌드 영상을 제작한 채널의 이름은 무엇인가? (날짜기준, 중복포함)
ans = df.loc[df.channelId == df.channelId.value_counts().index[0]].channelTitle.unique()[0]
print(ans)

#10 20회(20일)이상 인기동영상 리스트에 포함된 동영상의 숫자는?
ans = (df[['title', 'channelId']].value_counts() >= 20).sum()
print(ans)
