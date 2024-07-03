import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams["figure.figsize"] = (20,10)

#import the dataset
df = pd.read_csv("./assets/Mumbai House Prices.csv", low_memory=False) 

#filter out the relevant columns
df_fil = df.drop(['locality', 'status', 'age', 'price', 'price_unit', 'type'], axis='columns')

#price per square feet
df_new = df_fil.copy()
df_new['price_per_sqft'] = df_new['actual_price']/df_new['area']

#removing outliers by property location
def remove_outliers(df):

    df_out = pd.DataFrame()

    for key, subdf in df.groupby('region'):
        m = np.mean(subdf.price_per_sqft)
        st = np.std(subdf.price_per_sqft)

        reduced_df = subdf[((subdf.price_per_sqft > (m-2*st)) & (subdf.price_per_sqft <= (m+2*st)))]
        df_out = pd.concat([df_out,reduced_df], ignore_index=True)
    
    return df_out

df_val = remove_outliers(df_new)

df_val['region'] = df_val['region'].str.lower()

#Convert all the regions into columns
dummies = pd.get_dummies(df_val.region)
df_dummy = pd.concat([df_val, dummies.drop('kasaradavali thane west', axis='columns')], axis='columns')
df_fin = df_dummy.drop('region', axis='columns')
df_fin = df_fin.drop('price_per_sqft', axis='columns')

X = df_fin.drop(['actual_price'], axis='columns')
y = df_fin.actual_price

X.columns = [col.lower() for col in X.columns]

#train and test the model - Method 1
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=10)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr_clf = LinearRegression()
lr_clf.fit(X_train_scaled,y_train)
lr_clf.score(X_test_scaled,y_test)

#Method 2
# from sklearn.model_selection import ShuffleSplit
# from sklearn.model_selection import cross_val_score

# cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
# cross_val_score(LinearRegression(), X,y, cv=cv)

def predict_price(region,area,bhk):

    loc_index = np.where(X.columns == region)[0][0]

    x = np.zeros(len(X.columns))

    x[0] = bhk
    x[1] = area

    if loc_index >= 0:
        x[loc_index] = 1

    x_df = pd.DataFrame([x], columns=X.columns)
    x_scaled = scaler.transform(x_df)
    
    return lr_clf.predict(x_scaled)[0]

import pickle
with open('mumbai_home_prices_model.pickle', 'wb') as f:
    pickle.dump(lr_clf,f)

with open('scaler.pickle', 'wb') as f:
    pickle.dump(scaler, f)

import json
columns = {
    'data_columns':[col.lower() for col in X.columns]
}
with open("columns.json", 'w') as f:
    f.write(json.dumps(columns))





