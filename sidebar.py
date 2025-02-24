import streamlit as st
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import base64

def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

def sidebar():
    st.sidebar.title("🧠 DataMind Navigator")

    # Data Upload
    st.sidebar.header("📤 Data Upload")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.session_state.df = df
        st.sidebar.success("Data loaded successfully!")

        # Data Sampling
        st.sidebar.header("📊 Data Sampling")
        sample_size = st.sidebar.slider("Sample Size", 10, 1000, 100)
        if st.sidebar.checkbox("Use Sampled Data"):
            df = df.sample(sample_size)
            st.sidebar.info(f"Using a sample of {sample_size} rows.")

        # Column Selection
        st.sidebar.header("🔍 Column Selection")
        selected_columns = st.sidebar.multiselect("Select Columns for Analysis", df.columns)
        if selected_columns:
            df = df[selected_columns]
            st.sidebar.info(f"Selected columns: {', '.join(selected_columns)}")

        # Data Filtering
        st.sidebar.header("🔎 Data Filtering")
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        categorical_columns = df.select_dtypes(include=["object", "category"]).columns

        if numeric_columns.any():
            selected_numeric = st.sidebar.selectbox("Filter by Numeric Column", numeric_columns)
            min_val, max_val = float(df[selected_numeric].min()), float(df[selected_numeric].max())
            filter_range = st.sidebar.slider("Filter Range", min_val, max_val, (min_val, max_val))
            df = df[(df[selected_numeric] >= filter_range[0]) & (df[selected_numeric] <= filter_range[1])]
            st.sidebar.info(f"Filtered {selected_numeric} between {filter_range[0]} and {filter_range[1]}.")

        if categorical_columns.any():
            selected_category = st.sidebar.selectbox("Filter by Categorical Column", categorical_columns)
            unique_values = df[selected_category].unique()
            selected_values = st.sidebar.multiselect("Select Values", unique_values)
            if selected_values:
                df = df[df[selected_category].isin(selected_values)]
                st.sidebar.info(f"Filtered {selected_category} for {', '.join(selected_values)}.")

        # Data Sweeper
        st.sidebar.header("🧹 Data Sweeper")
        
        if st.sidebar.checkbox("Remove Duplicates"):
            df = df.drop_duplicates()
            st.sidebar.info(f"Removed {len(df) - df.shape[0]} duplicate rows.")

        if st.sidebar.checkbox("Handle Missing Values"):
            missing_method = st.sidebar.selectbox("Choose method", ["Remove", "Mean", "Median", "Mode"])
            if missing_method == "Remove":
                df = df.dropna()
            else:
                imputer = SimpleImputer(strategy=missing_method.lower())
                df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
            st.sidebar.info("Missing values handled.")

        if st.sidebar.checkbox("Remove Outliers"):
            df = remove_outliers(df)
            st.sidebar.info("Outliers removed.")
            
        def remove_outliers(df):
            for col in df.select_dtypes(include=[np.number]).columns:
                q1 = df[col].quantile(0.25)
                q3 = df[col].quantile(0.75)
                iqr = q3 - q1
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr
                df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
            return df

        if st.sidebar.checkbox("Normalize Data"):
            df = normalize_data(df)
            st.sidebar.info("Data normalized.")

        def normalize_data(df):
            scaler = StandardScaler()
            df[df.select_dtypes(include=[np.number]).columns] = scaler.fit_transform(df.select_dtypes(include=[np.number]))
            return df

        if st.sidebar.button("Download Cleaned Data"):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="cleaned_data.csv" class="btn">Download Cleaned CSV</a>'
            st.sidebar.markdown(href, unsafe_allow_html=True)

    # App Info
    st.sidebar.header("ℹ️ App Info")
    st.sidebar.write("**Version:** 1.0.0")
    st.sidebar.write("**Author:** Qurratulain")
   

    # Motivational Quote
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Strive not to be a success, but rather to be of value. - Albert Einstein"
    ]
    st.sidebar.markdown(f"**Quote of the Day:**\n\n*{np.random.choice(quotes)}*")