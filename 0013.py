#6가지 대표 하위 메소드중 통계분석을 위한 stats를 위주로 학습
#scipy
#│
#├── 01 integrate 수치적분, 미분방정식
#│  
#├── 02 linalg (선형대수, 매트릭스 분해)
#│ 
#├── 03 optimize (방정식 해 구하는 알고리즘, 함수 최적화)
#│ 
#├── 04 signal (신호 관련)
#│
#├── 05 sparse (희소 행렬, 희소 선형 시스템)
#│
#└── 06 stats (통계 분석) 


#stats 하위 모듈

#248개
from scipy import stats
#print(len([x for x in dir(stats) if x[0] !='_'  ]))
#scipy.stats
#│
#├── 01 T-test
#│   │
#│   ├── ttest_1samp         (단일표본 t검정)
#│   ├── ttest_ind           (독립표본 t검정)
#│   └── ttest_rel           (대응표본 t검정) 
#│ 
#├── 02 비모수 검정
#│   │
#│   ├── mannwhitneyu        (맨-휘트니 U 검정 - 중위수 , 윌콕슨 순위합 검정과 동일하다 볼 수 있음)
#│   ├── ranksums            (윌콕슨 순위합 검정 - 중위수)
#│   └── wilcoxon            (윌콕슨 부호 순위합 검정)
#│ 
#├── 03 정규성검정
#│   │
#│   ├── anderson            (Anderson-Darling , 데이터수가 상대적으로 많을 때)
#│   ├── kstest              (Kolmogorov-Smirnov , 데이터수가 상대적으로 많을 때)
#│   ├── mstats.normaltest
#│   └── shapiro             (shapiro, 노말분포 가장 엄격하게 검정, 데이터수가 상대적으로 적을때)
#│   
#├── 04 등분산검정
#│   │
#│   ├── bartlett
#│   ├── fligner
#│   └── levene
#│
#├── 05 카이제곱검정
#│   │
#│   ├── chi2_contingency     (카이제곱독립검정, 독립성 검정)
#│   ├── chisquare            (카이제곱검정 , 적합도 검정)
#│   └── fisher_exact         (피셔 정확 검정 - 빈도수가 5개 이하 셀의 수가 전체 셀의 20%이상일 경우 사용 )
#│
#└── 06 ANOVA (일원분산분석)
#    │
#    └── f_oneway (분산 분석은  statmodels 모듈이 더 좋음! )
#dir , help를 이용해서 파라미터들 찾아가며 사용하기

#정규성 검정
#01 다음 데이터의 정규성을 검증하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/normal1.csv')
plt.hist(df)
plt.show()

from scipy.stats import shapiro
print(shapiro(df))

# 샤피로 검정시 p-value가 0.34이므로 유의수준 5%에서 귀무가설("데이터는 정규성을 가진다")을 기각할 수 없다

#02 다음 데이터의 정규성을 검증하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/normal3.csv')
plt.hist(df)
plt.show()

from scipy.stats import shapiro
print(shapiro(df))

# 샤피로 검정시 p-value가 2.3e-16 이므로 유의수준 5%에서 귀무가설인 "데이터는 정규성을 가진다"를 기각하고 대립가설을 채택한다
# 데이터는 정규성을 가지지 않는다

#03 위의 데이터를 log변환 한 후에 정규성을 가지는지 확인하라
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/normal3.csv')
log_y_data = np.log1p(df)

plt.hist(log_y_data)
plt.show()

from scipy.stats import shapiro
print(shapiro(log_y_data))

# 샤피로 검정시 p-value가 0.17이므로 유의수준 5%에서 귀무가설("데이터는 정규성을 가진다")을 기각할 수 없다

#04 다음 데이터의 정규성을 검증하라
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/scipy/normal6.csv')
plt.hist(df)
plt.show()

from scipy.stats import shapiro
print(shapiro(df))
# 샤피로 검정시 p-value가 0.15 이므로 유의수준 5%에서 귀무가설("데이터는 정규성을 가진다")을 기각할 수 없다.
# 하지만 경고 메세지에서도 보이듯이 5000개 초과의 샘플에 대해서는 샤피로 검정은 정확하지 않을 수 있다.


from scipy.stats import anderson
# anderson 검정을 실시한다
print(anderson(df['data'].values))


# anderson 검정 결과의 의미는 아래 링크에서 확인 가능
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anderson.html 
# significance_level는 유의 확률값을 나타내며 critical_values는 각 유의 확률값의 기준점이 된다.
# 5%유의 수준에서 검정을 진행하려면 statistic값인 0.82이 significance_level 이 5.에 위치한 인덱스를 
# critical_values값에서 비교하면 된다. 그 값은 0.786이므로 이보다 큰 0.82을 가지므로 
# 귀무가설을 기각하고 대립가설을 채택한다 -> 데이터는 정규성을 가지지 않는다고 판단한다. (p-value와 기각기준 부등호 개념이 반대)
