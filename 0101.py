'''
dataurl = https://github.com/JoinNova/PracticeBigdata_Python/blob/main/Train.csv
'''
import pandas as pd
import numpy as np
data = 'Train.csv'
df = pd.read_csv(data)
#print(df.head())
#print(df.info())
#print(df.shape)
#print(df.isnull().sum())
#print(df.describe())
#print(df.describe(include = 'object'))

#모듈
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
'''rf = RandomForestClassifier(nn_estimators=1000, max_depth=9,\
                            min_samples_split=5, min_samples_leaf=3,\
                            max_features='auto', random_state=42, n_jobs = -1)'''
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
from xgboost import XGBClassifier
xgb_model = XGBClassifier()

from sklearn.metrics import roc_curve, roc_auc_score, auc    # roc_auc_score
from datetime import datetime

#전처리
x_train = df.drop(['Reached.on.Time_Y.N'], axis = 1)
#print(x_train)
y_train = df['Reached.on.Time_Y.N']
#print(y_train)
#print(type(y_train))
#print(y_train.value_counts())
##y_train = y_train.map(lambda x:int(x))
y_train = y_train.astype('int')
#print(type(y_train))
#print(y_train.value_counts())
#print(x_train.info())
#print(type(x_train))


'''#mapping
cat_features = ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']
for _ in cat_features:
    print(_, ':', set(x_train[_]))
print(x_train.info())
def wb_map(x):
    if x =='A':
        return 1
    elif x == 'B':
        return 2
    elif x == 'C':
        return 3
    elif x == 'D':
        return 4
    else:
        return 5

def ms_map(x):
    if x == 'Flight':
        return 1
    elif x == 'Ship':
        return 2
    else:
        return 3

def pi_map(x):
    if x == 'low':
        return 1
    elif x == 'high':
        return 2
    else:
        return 3

def sex_map(x):
    if x == 'F':
        return 1
    else:
        return 0

x_train['Warehouse_block'] = x_train['Warehouse_block'].map(wb_map)
x_train['Mode_of_Shipment'] = x_train['Mode_of_Shipment'].map(ms_map)
x_train['Product_importance'] = x_train['Product_importance'].map(pi_map)
x_train['Gender'] = x_train['Gender'].map(sex_map)'''

#print(x_train.info())

#Label Encoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
cat_features = ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']
for _ in cat_features:
    x_train[_] = le.fit_transform(x_train[_])
#print(x_train.info())




#학습
#Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
feats = ['Cost_of_the_Product', 'Discount_offered', 'Weight_in_gms']
for _ in feats:
    x_train[_] = sc.fit_transform(x_train[[_]]).flatten()
#print(x_train.head())

train_x, val_x, train_y, val_y = \
         train_test_split(x_train, y_train, test_size = 0.2, shuffle = True, random_state = 42)

print(x_train.shape, y_train.shape)
print(train_x.shape, val_x.shape, train_y.shape, val_y.shape)

print(rf.__class__.__name__)

models = [lr, dtree, rf, xgb_model]
for m in models:
    start = datetime.now()    # 학습 시작시간
    m.fit(train_x, train_y)   # 모델 학습
    end = datetime.now()      # 학습 종료시간
    
    # 예측 (.predict_proba())
    # roc_auc_score를 확인하기 위해, predict_proba (확률)이 필요함
    pred_y = m.predict_proba(val_x)[:,1]
    
    # 평가
    name = m.__class__.__name__         # 모델명 ('LogisticRegression','DecisionTreeClassifier',..)
    auc = roc_auc_score(val_y, pred_y)  # 예측값으로 roc_auc_score 확인
    time = end - start                  # 학습 소요시간
    print('Model {0} - AUC score: {1}, Training time: {2}'.format(name, auc, time))

#저장

