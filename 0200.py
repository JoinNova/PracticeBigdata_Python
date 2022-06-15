'''
<대락적인 데이터 처리 과정>
1. 결측치, 이상치 제거
2. 텍스트형 자료 더미변수화
3. 데이터 정규화
4. train, test data split
5. (자료가 불균형할 때) 오버, 언더샘플링
6. 차원축소
7. 모델링
8. Fit 학습
9. test data set으로 Accuracy score 확인(R^2, mse, auroc 등등)을 통해 모델 평가
10. 배깅
11. 배깅 모형 평가
12. 최종 모델을 사용해 새로운 데이터셋의 결과 확인
'''
'''
고객 3,500명에 대한 학습용 데이터(x_train.csv, y_train.csv)를 이용하여
성별 예측 모형을 만든후, 이를 평가용 데이터(x_test.csv)네 적용하여 얻은
2,482명 고객의 성별 예측 값(남자일 확률)을 다음과 같은 형식의 csv 파일로
생성하시오.(제출한 모델의 성능은 roc_auc 평가지표에 따라 채점)
'''
import pandas as pd
x_tr = 'x_train002.csv'
train = pd.read_csv(x_tr)
#print(train)
#print(train.info())
#print(train.describe())
x_te = 'x_test002.csv'
test = pd.read_csv(x_te)
#print(test)
#print(test.info())
#print(test.describe())
y_tr = 'y_train002.csv'
y_tra = pd.read_csv(y_tr)
#print(y_tra)
#print(y_tra.info())
#print(y_tra.describe())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

#전처리
#print(train.isnull().sum())
train.loc[train['환불금액'].isnull(), '환불금액'] = train['최대구매액'].fillna(0)
#print(train.isnull().sum())
#print(test.isnull().sum())
test.loc[test['환불금액'].isnull(), '환불금액'] = test['최대구매액'].fillna(0)
#print(test.isnull().sum())
x = train.drop(columns = ['cust_id'])
xd = pd.get_dummies(x)
y = y_tra['gender']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)
'''
test_size: 테스트 데이터셋의 비율
train_size: 학습 데이터셋의 비율, 1 - test_size의 값을 가짐
random_state: 데이터 분할시 셔플이 이뤄지는데 이를 위한 시드값. int형이나 RandomState를 입력한다.
shuffle: 셔플 여부 결정 (기본값 = False)
stratify: 지정한 data의 비율을 유지한다. stratify에 지정된 데이터셋의 라벨의 비율이 0 : 1 = 25 :75 일경우, 분할된 데이터셋 역시 이와 같은 비율로 분할된다. 참고로 stratify는 계층화하다는 의미
'''
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc_score : ', roc_auc_score(y_test, pred[:, 1]))

test_preprocessing = pd.get_dummies(test.drop(columns = ['cust_id']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict_proba(test_preprocessing)
submission = pd.DataFrame({'cust_id': test.cust_id, 'gender':test_pred[:, 1]})

#출력&저장
print(submission.head())
submission.to_csv('realtest01_002_02.csv', index = False)

