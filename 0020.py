#유튜브 인기동영상 데이터
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv",index_col=0)
#print(df.head())

#01  인기동영상 제작횟수가 많은 채널 상위 10개명을 출력하라 (날짜기준, 중복포함)
answer =list(df.loc[df.channelId.isin(df.channelId.value_counts().head(10).index)].channelTitle.unique())
#print(answer)

#02  논란으로 인기동영상이 된 케이스를 확인하고 싶다. dislikes수가 like 수보다 높은 동영상을 제작한 채널을 모두 출력하라
answer =list(df.loc[df.likes < df.dislikes].channelTitle.unique())
#print(answer)

#03  채널명을 바꾼 케이스가 있는지 확인하고 싶다. channelId의 경우 고유값이므로 이를 통해 채널명을 한번이라도 바꾼 채널의 갯수를 구하여라
change = df[['channelTitle','channelId']].drop_duplicates().channelId.value_counts()
target = change[change>1]
#print(len(target))

#04  일요일에 인기있었던 영상들중 가장많은 영상 종류(categoryId)는 무엇인가
df['trending_date2'] = pd.to_datetime(df['trending_date2'])
answer =df.loc[df['trending_date2'].dt.day_name() =='Sunday'].categoryId.value_counts().index[0]
#print(answer)

#05  각 요일별 인기 영상들의 categoryId는 각각 몇개 씩인지 하나의 데이터 프레임으로 표현하라
from IPython.display import display
group = df.groupby([df['trending_date2'].dt.day_name(),'categoryId'],as_index=False).size()
answer= group.pivot(index='categoryId',columns='trending_date2')
#display(answer)

#06  댓글의 수로 (comment_count) 영상 반응에 대한 판단을 할 수 있다. viewcount대비 댓글수가 가장 높은 영상을 확인하라 (view_count값이 0인 경우는 제외한다)
target2= df.loc[df.view_count!=0]
t = target2.copy()
t['ratio'] = (target2['comment_count']/target2['view_count']).dropna()
result = t.sort_values(by='ratio', ascending=False).iloc[0].title
#print(result)

#07  댓글의 수로 (comment_count) 영상 반응에 대한 판단을 할 수 있다.viewcount대비 댓글수가 가장 낮은 영상을 확인하라 (view_counts, ratio값이 0인경우는 제외한다.)
ratio = (df['comment_count'] / df['view_count']).dropna().sort_values()
ratio[ratio!=0].index[0]

result= df.iloc[ratio[ratio!=0].index[0]].title
#print(result)

#08  like 대비 dislike의 수가 가장 적은 영상은 무엇인가? (like, dislike 값이 0인경우는 제외한다)
target = df.loc[(df.likes !=0) & (df.dislikes !=0)]
num = (target['dislikes']/target['likes']).sort_values().index[0]

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
answer = df.iloc[num].title
#print(answer.translate(non_bmp_map))

#09  가장많은 트렌드 영상을 제작한 채널의 이름은 무엇인가? (날짜기준, 중복포함)
answer = df.loc[df.channelId ==df.channelId.value_counts().index[0]].channelTitle.unique()[0]
#print(answer)

#10  20회(20일)이상 인기동영상 리스트에 포함된 동영상의 숫자는?
answer= (df[['title','channelId']].value_counts()>=20).sum()
#print(answer)


'''유튜브 공범컨텐츠 동영상 데이터
데이터 출처 :https://www.kaggle.com/kukuroo3/youtube-episodic-contents-kr(참고, 데이터 수정)
데이터 설명 : 유튜브 “공범” 컨텐츠 동영상 정보 ( 10분 간격 수집)
dataurl1 (비디오 정보) = https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/videoInfo.csv
dataurl2 (참가자 채널 정보)= https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/channelInfo.csv'''

import pandas as pd
from IPython.display import display
channel =pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/channelInfo.csv')
video =pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/videoInfo.csv')
#display(channel.head())
#display(video.head())

#01  각 데이터의 ‘ct’컬럼을 시간으로 인식할수 있게 datatype을 변경하고 video 데이터의 videoname의 각 value 마다 몇개의 데이터씩 가지고 있는지 확인하라  
video['ct'] = pd.to_datetime(video['ct'])
answer = video.videoname.value_counts()
#print(answer)

#02  수집된 각 video의 가장 최신화 된 날짜의 viewcount값을 출력하라
answer = video.sort_values(['videoname','ct']).drop_duplicates('videoname',keep='last')[['viewcnt','videoname','ct']].reset_index(drop=True)
#display(answer)

#03  Channel 데이터중 2021-10-03일 이후 각 채널의 처음 기록 됐던 구독자 수(subcnt)를 출력하라
channel.ct = pd.to_datetime(channel.ct)
target = channel[channel.ct >= pd.to_datetime('2021-10-03')].sort_values(['ct','channelname']).drop_duplicates('channelname')
answer = target[['channelname','subcnt']].reset_index(drop=True)
#print(answer)

#04  각채널의 2021-10-03 03:00:00 ~ 2021-11-01 15:00:00 까지 구독자수 (subcnt) 의 증가량을 구하여라
end = channel.loc[channel.ct.dt.strftime('%Y-%m-%d %H') =='2021-11-01 15']
start = channel.loc[channel.ct.dt.strftime('%Y-%m-%d %H') =='2021-10-03 03']

end_df = end[['channelname','subcnt']].reset_index(drop=True)
start_df = start[['channelname','subcnt']].reset_index(drop=True)

end_df.columns = ['channelname','end_sub']
start_df.columns = ['channelname','start_sub']

tt = pd.merge(start_df,end_df)
tt['del'] = tt['end_sub'] - tt['start_sub']
result = tt[['channelname','del']]
#display(result)

#05  각 비디오는 10분 간격으로 구독자수, 좋아요, 싫어요수, 댓글수가 수집된것으로 알려졌다. 공범 EP1의 비디오정보 데이터중 수집간격이 5분 이하, 20분이상인 데이터 구간( 해당 시점 전,후) 의 시각을 모두 출력하라
import datetime

ep_one = video.loc[video.videoname.str.contains('1')].sort_values('ct').reset_index(drop=True)

ep_one[
        (ep_one.ct.diff(1) >=datetime.timedelta(minutes=20)) | \
        (ep_one.ct.diff(1) <=datetime.timedelta(minutes=5))
      
      ]

answer = ep_one[ep_one.index.isin([720,721,722,723,1635,1636,1637])]
#display(answer)

#06  각 에피소드의 시작날짜(년-월-일)를 에피소드 이름과 묶어 데이터 프레임으로 만들고 출력하라
start_date = video.sort_values(['ct','videoname']).drop_duplicates('videoname')[['ct','videoname']]
start_date['date'] = start_date.ct.dt.date
answer = start_date[['date','videoname']]
#display(answer)

#07 “공범” 컨텐츠의 경우 19:00시에 공개 되는것으로 알려져있다. 공개된 날의 21시의 viewcnt, ct, videoname 으로 구성된 데이터 프레임을 viewcnt를 내림차순으로 정렬하여 출력하라
video['time']= video.ct.dt.hour

answer = video.loc[video['time'] ==21] \
            .sort_values(['videoname','ct'])\
            .drop_duplicates('videoname') \
            .sort_values('viewcnt',ascending=False)[['videoname','viewcnt','ct']]\
            .reset_index(drop=True)

#display(answer)

#08  video 정보의 가장 최근 데이터들에서 각 에피소드의 싫어요/좋아요 비율을 ratio 컬럼으로 만들고 videoname, ratio로 구성된 데이터 프레임을 ratio를 오름차순으로 정렬하라
target = video.sort_values('ct').drop_duplicates('videoname',keep='last')
target['ratio'] =target['dislikecnt'] / target['likecnt']

answer = target.sort_values('ratio')[['videoname','ratio']].reset_index(drop=True)
#print(answer)

#09  2021-11-01 00:00:00 ~ 15:00:00까지 각 에피소드별 viewcnt의 증가량을 데이터 프레임으로 만드시오
start = pd.to_datetime("2021-11-01 00:00:00")
end = pd.to_datetime("2021-11-01 15:00:00")

target = video.loc[(video["ct"] >= start) & (video['ct'] <= end)].reset_index(drop=True)

def check(x):
    result = max(x) - min(x)
    return result

answer = target[['videoname','viewcnt']].groupby("videoname").agg(check)
#print(answer)

#10  video 데이터 중에서 중복되는 데이터가 존재한다. 중복되는 각 데이터의 시간대와 videoname 을 구하여라
answer  = video[video.index.isin(set(video.index) -  set(video.drop_duplicates().index))]
result = answer[['videoname','ct']]
display(result)
