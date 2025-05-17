import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

table = pd.read_csv('C:/Users/abc/Downloads/internship/Level 3/winequality-white.csv', sep=';')
column_list = table.columns.tolist()

graph_type = input('Enter the graph type Line , Bar or Heatmap?')
x_axis = column_list[0]
y_axis = column_list[1]

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
plt.tight_layout()
plt.show()
