import pandas as pd
from  sklearn.preprocessing import LabelEncoder
from sklearn import tree
df = pd.read_csv("salaries.csv")
print(df)

inputs = df.drop('salary_more_then_100k',axis='columns')

target = df['salary_more_then_100k']

print(inputs)

print(target)

le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_company.fit_transform(inputs['job'])
inputs['degree_n'] = le_company.fit_transform(inputs['degree'])
print(inputs)

inputs_n = inputs.drop(['company','job','degree'],axis='columns')
print(inputs_n)

model = tree.DecisionTreeClassifier()
model.fit(inputs_n,target)

print(model)

print(model.score(inputs_n,target))

print(model.predict([[2,2,1]]))
print(model.predict([[2,0,1]]))
