import  pandas as pd
x_tra = 'x_train002.csv'
x_tr = pd.read_csv(x_tra)
#print(x_train)
#print(x_tr.info())
#print(x_train.describe())
y_tra = 'y_train002.csv'
y_tr = pd.read_csv(y_tra)
#print(y_train)
#print(y_train.info())
#print(y_train.describe())
x_tes = 'x_test002.csv'
x_te = pd.read_csv(x_tes)
#print(x_te)
#print(x_te.info())
#print(x_te.describe())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

#전처리
# 결측치 처리 및 이상치 변환, 파생변수 생성
x_tr.loc[x_tr['환불금액'].isnull(), '환불금액'] = x_tr['환불금액'].fillna(0)
x_te.loc[x_te['환불금액'].isnull(), '환불금액'] = x_te['환불금액'].fillna(0)
#train$환불금액 <- ifelse(is.na(train$환불금액) == 'TRUE', 0, train$환불금액)
x_tr.loc[x_tr['총구매액'] < 0, '총구매액'] = 0
#train$총구매액 <- ifelse(train$총구매액 <0, 0, train$총구매액)
x_tr.loc[x_tr['최대구매액'] < 0, '최대구매액'] = 0
#train$최대구매액 <- ifelse(train$최대구매액 <0, 0, train$최대구매액)
x_tr['최대구매액'] = x_tr['총구매액'] +  x_tr['환불금액']
#train$최초구매액 <- train$총구매액 + train$환불금액
#x_tr['최대구매액비율'] = x_tr['최대구매액'] / x_tr['최초구매액']
#train$최대구매액비율 <- train$최대구매액/train$최초구매액 
#train$환불금액비율 <- train$환불금액/train$최초구매액 

x = x_tr.drop(columns = ['cust_id'])
xd = pd.get_dummies(x)
y = y_tr['gender']



#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)
rf.fit(x_train, y_train)
pred = rf.predict_proba(x_test)
print('test roc_score : ', roc_auc_score(y_test, pred[:, 1]))

test_preprocessing = pd.get_dummies(x_te.drop(columns = ['cust_id']))
test_preprocessing[list(set(x_train.columns) - set(test_preprocessing))] = 0
test_pred = rf.predict_proba(test_preprocessing)
submission = pd.DataFrame({'custid': x_te.cust_id, 'gender': test_pred[:, 1]})

#출력&저장
print('submission file\n', submission.head())
submission.to_csv('realtest01_002_01.csv', index = False)
