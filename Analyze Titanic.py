import pandas as pd

df = pd.read_csv(r'C:\Users\bosss\Desktop\aQ_hzkRWQ86P4c5EVvPOCQ_8fb0d10da4924825af5d43d023003ce3_titanic.csv')

# print(df)
# print(len(df))
print(df.columns)
# print(len(df[df['Sex'] == 'male']))
# print(len(df[df['Parch'] > 0]))
# print(len(df[df['Pclass'] == 1])/len(df['Pclass']))
# print(len(df[df['Survived'] == 1])/len(df['Survived']))
# print(len(df.query('Pclass == 1 and Survived == 1')) / len(df.query('Pclass == 1')))
# print(df['Age'].value_counts())
a = df['Fare'].mean()
print(len(df.query('Fare > @a')))
