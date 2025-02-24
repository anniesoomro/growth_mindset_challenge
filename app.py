import streamlit as st
from utils import load_data, handle_missing_values, remove_outliers, normalize_data
from visualization import show_correlation_heatmap, show_scatter_plot, show_line_chart, show_bar_chart, show_histogram
from analytics import perform_pca
from growth_tracker import daily_challenge, mistake_journal, progress_tracker, progress_visualization
from sidebar import sidebar

# Page Configuration
st.set_page_config(
    page_title="DataMind: Analysis & Growth",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    /* Your custom CSS here */
</style>
""", unsafe_allow_html=True)

# Sidebar
sidebar()

# Main Content
st.title("🧠 DataMind: Analysis & Growth")
st.write("Unlock the potential of your data while nurturing your growth mindset!")

if 'df' in st.session_state:
    df = st.session_state.df

    # Data Overview
    st.header("📊 Data Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Data Types", df.dtypes.nunique())

    if st.checkbox("Show Data Preview"):
        st.write(df.head())

    # Data Exploration
    st.header("🔍 Data Exploration")
    if st.checkbox("Show Descriptive Statistics"):
        st.write(df.describe())

    if st.checkbox("Show Correlation Heatmap"):
        show_correlation_heatmap(df)

    # Data Visualization
    st.header("📈 Data Visualization")
    chart_type = st.selectbox("Select Chart Type", ["Scatter Plot", "Line Chart", "Bar Chart", "Histogram"])
    
    if chart_type == "Scatter Plot":
        show_scatter_plot(df)
    elif chart_type == "Line Chart":
        show_line_chart(df)
    elif chart_type == "Bar Chart":
        show_bar_chart(df)
    elif chart_type == "Histogram":
        show_histogram(df)

    # Advanced Analytics
    st.header("🧪 Advanced Analytics")
    if st.checkbox("Perform PCA"):
        perform_pca(df)

# Growth Mindset Tracker
st.header("🌱 Growth Mindset Tracker")
daily_challenge()
mistake_journal()
progress_tracker()
progress_visualization()

# Footer
st.markdown("---")
st.markdown("© 2023 DataMind: Analysis & Growth. Empowering data-driven growth.")