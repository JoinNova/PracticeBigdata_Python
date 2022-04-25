import pandas as pd
print("Hello World")

DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
df = pd.read_csv(DataUrl,sep='\t')

type(df)
##print(df)


##Ans = df.head(5)
##print(Ans)

##print(df.shape)
##print('행:',df.shape[0])
##print('열:',df.shape[1])

Ans = df.columns
print(Ans)



print("Hello World")
