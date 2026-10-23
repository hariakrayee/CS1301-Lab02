# This creates the page for displaying data visualizations.

import streamlit as st
import pandas as pd
import json
import plotly.express as px
# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---
with open("data.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["data_points"])
st.bar_chart(df, x="label", y="value")
if "minimum" not in st.session_state:
    st.session_state.minimum = 0

st.slider("Minimum hours", 0, 30, key="minimum")

filtered = df[df["value"] >= st.session_state.minimum]
fig = px.pie(filtered, names="label", values="value",
             title="Study Locations")
st.plotly_chart(fig)
# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---
csvData = pd.read_csv("data.csv")

st.subheader("Survey Results")
st.bar_chart(csvData, x="Category", y="Value")
if "csvMinimum" not in st.session_state:
    st.session_state.csvMinimum = 0

st.slider("Minimum survey hours", 0, 30, key="csvMinimum")

filteredCSV = csvData[csvData["Value"] >= st.session_state.csvMinimum]

if not filteredCSV.empty:
    fig2 = px.pie(filteredCSV, names="Category", values="Value",
                  title="Survey Study Hours")
    st.plotly_chart(fig2)
else:
    st.write("No data matches.")