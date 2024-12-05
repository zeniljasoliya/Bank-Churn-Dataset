

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
def load_data():
    data = pd.read_csv('test.csv')
    return data

data = load_data()

# Sidebar
st.sidebar.title("Filter Data")

# Filter options
filter_options = {
    "Geography": st.sidebar.multiselect("Select Geography", data['Geography'].unique()),
    "Gender": st.sidebar.multiselect("Select Gender", data['Gender'].unique()),
    "Age": st.sidebar.slider("Select Age Range", min_value=data['Age'].min(), max_value=data['Age'].max(), value=(data['Age'].min(), data['Age'].max()))
}

filtered_data = data[
    (data['Geography'].isin(filter_options["Geography"])) &
    (data['Gender'].isin(filter_options["Gender"])) &
    (data['Age'].between(filter_options["Age"][0], filter_options["Age"][1]))
]

st.title("Bank Churn Dataset")



# Display filtered data
st.subheader("Filtered Data")
st.write(filtered_data)

# Display statistics
st.subheader("Statistics")
st.write(filtered_data.describe())

# Main content
st.title("Data Visualization")

# Bar Chart
st.subheader("Bar Chart")
bar_col = st.selectbox("Select a column for the bar chart", filtered_data.columns)
bar_chart_data = filtered_data[bar_col].value_counts()
fig, ax = plt.subplots()
ax.bar(bar_chart_data.index, bar_chart_data, color='skyblue')
st.pyplot(fig)

# Box Plot
st.subheader("Box Plot")
box_col = st.selectbox("Select a column for the box plot", filtered_data.columns)
fig, ax = plt.subplots()
sns.boxplot(x=box_col, data=filtered_data, palette='pastel', ax=ax)
st.pyplot(fig)

# Histogram
st.subheader("Histogram")
hist_col = st.selectbox("Select a column for the histogram", filtered_data.columns)
fig, ax = plt.subplots()
ax.hist(filtered_data[hist_col], color='lightgreen')
st.pyplot(fig)

# Scatter Plot
st.subheader("Scatter Plot")
scatter_x = st.selectbox("Select x-axis", filtered_data.columns)
scatter_y = st.selectbox("Select y-axis", filtered_data.columns)
fig, ax = plt.subplots()
sns.scatterplot(x=scatter_x, y=scatter_y, data=filtered_data, color='orange', ax=ax)
st.pyplot(fig)



# Pie Chart
st.subheader("Pie Chart")
pie_col = st.selectbox("Select a column for the pie chart", filtered_data.columns)
pie_chart_data = filtered_data[pie_col].value_counts()
fig, ax = plt.subplots()
ax.pie(pie_chart_data, labels=pie_chart_data.index, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue', 'lightgreen'])
st.pyplot(fig)

