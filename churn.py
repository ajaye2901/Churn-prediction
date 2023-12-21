import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df=pd.read_excel(r"C:\Users\ajuaj\Downloads\archive\E Commerce Dataset.xlsx",sheet_name=1)
features=['Tenure','WarehouseToHome','HourSpendOnApp','OrderAmountHikeFromlastYear','CouponUsed','OrderCount','DaySinceLastOrder']
for i in features :
    x=df[i].mode()[0]
    df.fillna(x,inplace=True)

df.drop(['CustomerID'],axis=1,inplace=True)
df.drop(['Gender'],axis=1,inplace=True)
df.drop(['MaritalStatus'],axis=1,inplace=True)
df.drop(['WarehouseToHome'],axis=1,inplace=True)

le=LabelEncoder()
df['PreferredLoginDevice'] = le.fit_transform(df['PreferredLoginDevice'])
df['PreferredPaymentMode'] = le.fit_transform(df['PreferredPaymentMode'])
df['PreferedOrderCat'] = le.fit_transform(df['PreferedOrderCat'])

X=df.iloc[:,1:]
y=df.iloc[:,:1].values.flatten()

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

model=RandomForestClassifier()
model.fit(X_train,y_train)


with open(r'C:\Users\ajuaj\Desktop\Practice\sristhtiPro\churn_model.pkl','wb') as f:
    pickle.dump(model,f)
