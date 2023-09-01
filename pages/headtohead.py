import streamlit as st
import pandas as pd

# Create a Streamlit app
st.title("Filtered DataFrame")

# Sample DataFrame
df=pd.read_csv('/pages/consolidatedresults.csv')

# Define the dropdowns for column 1 and column 2
selected_column_1 = st.selectbox("Select column 1:", df["team"].unique())
selected_column_2 = st.selectbox("Select column 2:", df["team_1"].unique())

# Filter the DataFrame
filtered_df = df[
    ((df["team"] == selected_column_1) & (df["team_1"] == selected_column_2)) |
    ((df["team"] == selected_column_2) & (df["team_1"] == selected_column_1))
]

# Display the filtered DataFrame
st.write("Filtered DataFrame:")
st.write(filtered_df)
