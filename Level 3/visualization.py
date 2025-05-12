import streamlit as st
import pandas as pd
import plotly.express as px

st.title(" Interactive Data Visualization Tool")


uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file,sep=';')
    st.write("### Data Preview", df.head())

    columns = df.columns.tolist()

   
    chart_type = st.selectbox("Select Chart Type", ["Scatter", "Line", "Bar", "Histogram", "Box", "Pie"])

    x_col = st.selectbox("X-axis", columns)
    y_col = st.selectbox("Y-axis", columns)

    if chart_type == "Scatter":
        fig = px.scatter(df, x=x_col, y=y_col)
    elif chart_type == "Line":
        fig = px.line(df, x=x_col, y=y_col)
    elif chart_type == "Bar":
        fig = px.bar(df, x=x_col, y=y_col)
    elif chart_type == "Histogram":
        fig = px.histogram(df, x=x_col)
    elif chart_type == "Box":
        fig = px.box(df, x=x_col, y=y_col)
    elif chart_type == "Pie":
        fig = px.pie(df, names=x_col, values=y_col)

    st.plotly_chart(fig)
