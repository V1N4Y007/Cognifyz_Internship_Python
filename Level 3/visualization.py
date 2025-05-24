import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Wine Quality Data Visualizer")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    table = pd.read_csv(uploaded_file, sep=';')
    column_list = table.columns.tolist()
    
   
    graph_type = st.selectbox("Select the graph type", ["Line", "Bar", "Heatmap"])
    
    if graph_type != "Heatmap":
        x_axis = st.selectbox("Select X-axis", column_list)
        y_axis = st.selectbox("Select Y-axis", column_list)
    
    plt.figure(figsize=(10, 6))
    
    if graph_type == "Line":
        plt.plot(table[x_axis], table[y_axis])
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
    elif graph_type == "Bar":
        plt.bar(table[x_axis], table[y_axis])
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
    elif graph_type == "Heatmap":
        num_data = table.select_dtypes(include=['number'])
        corr = num_data.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')

    plt.title(f"{graph_type} Chart")
    st.pyplot(plt.gcf())
else:
    st.info("Please upload a CSV file to proceed.")
