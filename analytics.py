import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import plotly.express as px

def perform_pca(df):
    n_components = st.slider("Number of Components", 2, min(10, df.shape[1]), 2)
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(df[numeric_columns])
    pca_df = pd.DataFrame(data=pca_result, columns=[f'PC{i+1}' for i in range(n_components)])
    
    fig = px.scatter(pca_df, x='PC1', y='PC2', title='PCA Visualization')
    st.plotly_chart(fig)

    st.write("Explained Variance Ratio:")
    st.write(pca.explained_variance_ratio_)