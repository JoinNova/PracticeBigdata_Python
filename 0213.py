'''
penguins
youtube = https://www.youtube.com/watch?v=WYxfdvukFnY&list=PLjh1hlmDSDkc-raFsiUXZbdZ0cA-1gPrP&index=7
datasource = https://www.kaggle.com/datasets/pancaldi/palmerpenguins
'''
import pandas as pd
data = 'penguins.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier()
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

#전처리
df.loc[df.bill_length_mm.isnull(), 'bill_length_mm'] = df.bill_length_mm.fillna(df.bill_length_mm.mean())
df.loc[df.bill_depth_mm.isnull(), 'bill_depth_mm'] = df.bill_depth_mm.fillna(df.bill_depth_mm.mean())
df.loc[df.flipper_length_mm.isnull(), 'flipper_length_mm'] = df.flipper_length_mm.fillna(df.flipper_length_mm.mean())
df.loc[df.body_mass_g.isnull(), 'body_mass_g'] = df.body_mass_g.fillna(df.body_mass_g.mean())
df.loc[df.sex.isnull(), 'sex'] = df.sex.fillna(method = 'ffill')
#print(df.isnull().sum())


#라벨링
label = ['species', 'island', 'sex']
df[label] = df[label].apply(le.fit_transform)

#카테고리
category = ['island', 'sex']
for _ in category:
    df[_] = df[_].astype('category')

df = pd.get_dummies(df)

#파생변수
df['body_mass_g_qcut'] = pd.qcut(df['body_mass_g'], 5, labels = False)

#스케일링
scaler = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
mms.fit(df[scaler])
df[scaler] = mms.transform(df[scaler])

print(df)

x = df.drop(columns = ['species'])
xd = pd.get_dummies(x)
y = df['species']

#학습
x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 42)

rf.fit(x_train, y_train)
rf_pred = rf.predict(x_test)
print(*rf_pred)

ada.fit(x_train, y_train)
ada_pred = ada.predict(x_test)
print(*ada_pred)

result = VotingClassifier(estimators = [('rf',rf), ('ada', ada)], voting = 'hard')
result.fit(x_train, y_train)
vot_pred = result.predict(x_test)
print(*vot_pred)

print('RanForest : ', accuracy_score(y_test, rf_pred))
print('AdaBoost : ', accuracy_score(y_test, ada_pred))
print('Voiting : ', accuracy_score(y_test, vot_pred))

##print('test roc_score : ', roc_auc_score(y_test, pred[:, 1]))

##submission = pd.DataFrame({'id': x_test.index, 'predict': pred[:, 1]})

#출력&저장
##print('submission file\n', submission.head())
##submission.to_csv('kaggle02_002_01.csv', index = False)
