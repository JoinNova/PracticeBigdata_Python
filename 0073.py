'''
데이터 출처 : https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset (후처리 작업)
데이터 설명 : 뇌졸증 발생여부 예측
train : https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv
test : https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/test.csv
'''
import pandas as pd
tr_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv'
te_data = 'https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/test.csv'
train = pd.read_csv(tr_data)
#print(train.head())
#print(train.shape)
#print(train.info())
test = pd.read_csv(te_data)
#print(test.head())
#print(test.shape)
#print(test.info())

# 전처리를 어떤걸 해야하는지 발견하는 방법
train['age'] =train['age'].str.replace('*','').astype('int64')
train['bmi'] = train['bmi'].fillna(train['bmi'].mean())
test['bmi'] = test['bmi'].fillna(test['bmi'].mean())
x = train.drop(columns =['id','stroke'])
xd = pd.get_dummies(x)
y = train['stroke']

#학습
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
x_train,x_test,y_train,y_test = train_test_split(xd,y,stratify =y ,random_state=1)
rf = RandomForestClassifier()
rf.fit(x_train,y_train)
#line 305, in fit #accept_sparse="csc", dtype=DTYPE)
#line 433, in _validate_data #X, y = check_X_y(X, y, **check_params)
#line 63, in inner_f #return f(*args, **kwargs)
#line 878, in check_X_y #estimator=estimator)
#line 63, in inner_f #return f(*args, **kwargs)
#line 721, in check_array #allow_nan=force_all_finite == 'allow-nan')
#line 106, in _assert_all_finite #msg_dtype if msg_dtype is not None else X.dtype)
#ValueError: Input contains NaN, infinity or a value too large for dtype('float32')


#line 30, in <module> #rf.fit(x_train,y_train)
#line 305, in fit #accept_sparse="csc", dtype=DTYPE)
#line 433, in _validate_data #X, y = check_X_y(X, y, **check_params)
#line 63, in inner_f #return f(*args, **kwargs)
#line 878, in check_X_y #estimator=estimator)
#line 63, in inner_f #return f(*args, **kwargs)
#line 721, in check_array #allow_nan=force_all_finite == 'allow-nan')
#line 106, in _assert_all_finite #msg_dtype if msg_dtype is not None else X.dtype)
#ValueError: Input contains NaN, infinity or a value too large for dtype('float32').

pred = rf.predict_proba(x_test)
from sklearn.metrics import roc_auc_score,classification_report
print('test roc score : ',roc_auc_score(y_test,pred[:,1]))
#line 53, in <module> #print('test roc score : ',roc_auc_score(y_test,pred[:,1]))
#NameError: name 'roc_auc_score' is not defined


# one-hot encoding시 train셋에만 존재하는 컬럼이 존재
test_preprocessing =pd.get_dummies(test.drop(columns=['id']))
test_preprocessing[list(set(x_train.columns) -set(test_preprocessing))] =0
test_preprocessing =test_preprocessing[x_train.columns]
test_pred = rf.predict_proba(test_preprocessing)
#line 63, in <module> #test_pred = rf.predict_proba(test_preprocessing)
#line 674, in predict_proba #X = self._validate_X_predict(X)
#line 422, in _validate_X_predict #return self.estimators_[0]._validate_X_predict(X, check_input=True)
#line 408, in _validate_X_predict #reset=False)
#line 421, in _validate_data #X = check_array(X, **check_params)
#line 63, in inner_f #return f(*args, **kwargs)
#line 721, in check_array #allow_nan=force_all_finite == 'allow-nan')
#line 106, in _assert_all_finite #msg_dtype if msg_dtype is not None else X.dtype)
#ValueError: Input contains NaN, infinity or a value too large for dtype('float32')

# 아래 코드 예측변수와 수험번호를 개인별로 변경하여 활용
# pd.DataFrame({'id': test.id, 'stroke': pred}).to_csv('003000000.csv', index=False)
pd.DataFrame({'id': test.id, 'stroke': test_pred[:,1]}).to_csv('sony_02_001.csv', index=False)
