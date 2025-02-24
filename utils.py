import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def load_data(uploaded_file):
    data = pd.read_csv(uploaded_file)
    return data

def handle_missing_values(df, method="mean"):
    if method == "remove":
        df = df.dropna()
    else:
        imputer = SimpleImputer(strategy=method)
        df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    return df

def remove_outliers(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[col] >= Q1 - 1.5*IQR) & (df[col] <= Q3 + 1.5*IQR)]
    return df

def normalize_data(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    scaler = StandardScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    return df