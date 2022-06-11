'''
다음은 iris 데이터 세트이다.
주어진 데이터를 이용하여 Species rpart, svm 예측 모형을 만든 후
높은 Accuracy 값을 가지는 모델의 예측 값을 csv파일로 제출하시오.
'''
import pandas as pd
data = 'iris.csv'
df = pd.read_csv(data)
#print(df)
#print(df.info())
#print(df.describe())

#모듈
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor()

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import plot_confusion_matrix

#전처리
print(df.isnull().sum())

#Encoding Catergorical data
df['Species'] = encoder.fit_transform(df['Species'])

train = df.head(int(len(df)*0.9))
test = df.tail(int(len(df)*0.1))

x = train.drop(columns = ['Species'])
xd = pd.get_dummies(x)
y = train['Species']



#학습
sns.pairplot(df, hue="Species")
#plt.show()

#x_train, x_test, y_train, y_test = train_test_split(xd, y, stratify = y, random_state = 1)
#rf.fit(x_train, y_train)
#pred = rfr.predict(x_test)
#print(pred)
#print('test roc score : ', roc_auc_score(y_test, pred[:, 1]))

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
class_LR  = LogisticRegression(solver='liblinear').fit(X_train, y_train)
y_pred_LR = class_LR.predict(X_test)
class_rep_LR = classification_report(y_test, y_pred_LR)
print('\t\t\tClassification report:\n\n', class_rep_LR, '\n')
plot_confusion_matrix(class_LR, X_test, y_test) 
#plt.show()


#출력&저장
class_rep_LR.to_csv('new01_002_01.csv', index = False)
