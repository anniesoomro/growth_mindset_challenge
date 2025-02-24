import streamlit as st
import plotly.express as px

def show_correlation_heatmap(df):
    fig = px.imshow(df.corr(), text_auto=True, color_continuous_scale='coolwarm', title="Correlation Heatmap")
    st.plotly_chart(fig)

def show_scatter_plot(df):
    x_axis = st.selectbox("X-axis", df.columns)
    y_axis = st.selectbox("Y-axis", df.columns)
    fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
    st.plotly_chart(fig)

def show_line_chart(df):
    x_axis = st.selectbox("X-axis", df.columns)
    y_axis = st.selectbox("Y-axis", df.columns)
    fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} over {x_axis}")
    st.plotly_chart(fig)

def show_bar_chart(df):
    x_axis = st.selectbox("X-axis", df.columns)
    y_axis = st.selectbox("Y-axis", df.columns)
    fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")
    st.plotly_chart(fig)

def show_histogram(df):
    column = st.selectbox("Select Column", df.columns)
    fig = px.histogram(df, x=column, title=f"Distribution of {column}")
    st.plotly_chart(fig)