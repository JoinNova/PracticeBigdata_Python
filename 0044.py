'''
유튜브 공범컨텐츠 동영상 데이터
데이터 출처 :https://www.kaggle.com/kukuroo3/youtube-episodic-contents-kr(참고, 데이터 수정)
데이터 설명 : 유튜브 “공범” 컨텐츠 동영상 정보 ( 10분 간격 수집)
dataurl1 (비디오 정보) = https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/videoInfo.csv
dataurl2 (참가자 채널 정보)= https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/channelInfo.csv
'''

import pandas as pd
data1 = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/videoInfo.csv'
data2 = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/channelInfo.csv'
video = pd.read_csv(data1)
channel = pd.read_csv(data2)

print(video)
print(video.columns)
print(channel)
print(channel.columns)

#01 각 데이터의 ‘ct’컬럼을 시간으로 인식할수 있게 datatype을 변경하고 video 데이터의 videoname의 각 value 마다 몇개의 데이터씩 가지고 있는지 확인하라
video['ct'] = pd.to_datetime(video['ct'])
ans = video.videoname.value_counts()
print(ans)

#02 수집된 각 video의 가장 최신화 된 날짜의 viewcount값을 출력하라
ans = video.sort_values(['videoname', 'ct']).drop_duplicates('videoname', keep = 'last')\
                        [['viewcnt', 'videoname', 'ct']].reset_index(drop = True)
print(ans)

#03 Channel 데이터중 2021-10-03일 이후 각 채널의 처음 기록 됐던 구독자 수(subcnt)를 출력하라
channel.ct = pd.to_datetime(channel.ct)
target = channel[channel.ct >= pd.to_datetime('2021-10-03')].\
         sort_values(['ct', 'channelname']).drop_duplicates('channelname')
ans = target[['channelname', 'subcnt']].reset_index(drop = True)
print(ans)

#04 각채널의 2021-10-03 03:00:00 ~ 2021-11-01 15:00:00 까지 구독자수 (subcnt) 의 증가량을 구하여라
start = channel.loc[channel.ct.dt.strftime('%Y-%m-%d %H') == '2021-10-03 03']
end = channel.loc[channel.ct.dt.strftime('%Y-%m-%d %H') == '2021-11-01 15']

start_df = start[['channelname', 'subcnt']].reset_index(drop = True)
end_df = end[['channelname', 'subcnt']].reset_index(drop = True)

start_df.columns = ['channelname', 'start_sub']
end_df.columns = ['channelname', 'end_sub']

tt = pd.merge(start_df,end_df)
tt['del'] = tt['end_sub'] - tt['start_sub']
ans = tt[['channelname', 'del']]
print(ans)

#05 각 비디오는 10분 간격으로 구독자수, 좋아요, 싫어요수, 댓글수가 수집된것으로 알려졌다. 공범 EP1의 비디오정보 데이터중 수집간격이 5분 이하, 20분이상인 데이터 구간( 해당 시점 전,후) 의 시각을 모두 출력하라
import datetime
ep_one = video.loc[video.videoname.str.contains('1')].\
         sort_values('ct').reset_index(drop = True)
ep_one[(ep_one.ct.diff(1) >= datetime.timedelta(minutes = 20)) |\
       (ep_one.ct.diff(1) <= datetime.timedelta(minutes = 5))]
ans = ep_one[ep_one.index.isin([720.721,722,723,1635,1636,1637])]
print(ans)

#06 각 에피소드의 시작날짜(년-월-일)를 에피소드 이름과 묶어 데이터 프레임으로 만들고 출력하라
start_date = video.sort_values(['ct', 'videoname']).drop_duplicates('videoname')[['ct', 'videoname']]
start_date['date'] = start_date.ct.dt.date
ans = start_date[['date', 'videoname']]
print(ans)

#07 “공범” 컨텐츠의 경우 19:00시에 공개 되는것으로 알려져있다. 공개된 날의 21시의 viewcnt, ct, videoname 으로 구성된 데이터 프레임을 viewcnt를 내림차순으로 정렬하여 출력하라
video['time'] = video.ct.dt.hour
ans = video.loc[video['time'] == 21].\
      sort_values(['videoname', 'ct']).\
      drop_duplicates('videoname').\
      sort_values('viewcnt', ascending = False)[['videoname', 'viewcnt', 'ct']].\
      reset_index(drop = True)
print(ans)

#08 video 정보의 가장 최근 데이터들에서 각 에피소드의 싫어요/좋아요 비율을 ratio 컬럼으로 만들고 videoname, ratio로 구성된 데이터 프레임을 ratio를 오름차순으로 정렬하라
target = video.sort_values('ct').drop_duplicates('videoname', keep = 'last')
target['ratio'] = target['dislikecnt'] / target['likecnt']
ans =target.sort_values('ratio')[['videoname', 'ratio']].reset_index(drop = True)
print(ans)

#09 2021-11-01 00:00:00 ~ 15:00:00까지 각 에피소드별 viewcnt의 증가량을 데이터 프레임으로 만드시오
start = pd.to_datetime('2021-11-01 00:00:00')
end = pd.to_datetime('2021-11-01 15:00:00')
target = video.loc[(video['ct'] >= start) & (video['ct'] <= end)].\
         reset_index(drop = True)
def chk(x):
    result = max(x) - min(x)
    return result
ans = target[['videoname', 'viewcnt']].groupby('videoname').agg(chk)
print(ans)

#10 video 데이터 중에서 중복되는 데이터가 존재한다. 중복되는 각 데이터의 시간대와 videoname 을 구하여라
ans = video[video.index.isin(set(video.index) - set(video.drop_duplicates().index))]
print(ans[['videoname', 'ct']])
