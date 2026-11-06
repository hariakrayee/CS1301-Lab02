
# This creates the page for displaying data visualizations.
#my words: this is the page that shows graphs and statistics
import streamlit as st
import pandas as pd
import json
import plotly.express as px

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json

with open("data.json", "r") as file:#this read mode
    data = json.load(file)

df = pd.DataFrame(data["data_points"])

st.subheader("Study Locations")
st.bar_chart(df, x="label", y="value")

if "minimum" not in st.session_state:
    st.session_state.minimum = 0

st.slider("Minimum hours", 0, 30, key="minimum")

filtered = df[df["value"] >= st.session_state.minimum]

#note to self:
#extra cred stuff is mean mediam and that tyoe of stuff so reference the lab sheet

# Keep track of previous statistics
if "jsonMean" not in st.session_state:
    st.session_state.jsonMean = None

if "jsonMedian" not in st.session_state:
    st.session_state.jsonMedian = None

if not filtered.empty:
    fig = px.pie(filtered, names="label", values="value",
                 title="Study Locations")
    st.plotly_chart(fig)

    mean = round(filtered["value"].mean(), 2)
    median = round(filtered["value"].median(), 2)

    # Compare with previous values
    if st.session_state.jsonMean is None:
        meanChange = None
        medianChange = None
    else:
        meanChange = round(mean - st.session_state.jsonMean, 2)
        medianChange = round(median - st.session_state.jsonMedian, 2)

    st.metric("Mean study hours", mean, delta=meanChange)
    st.metric("Median study hours", median, delta=medianChange)

    st.session_state.jsonMean = mean
    st.session_state.jsonMedian = median

else:
    st.write("No data matches.")
    st.metric("Mean study hours", "N/A")
    st.metric("Median study hours", "N/A")


# PART 2: GRAPHS FROM data.csv

csvData = pd.read_csv("data.csv")

st.subheader("Survey Results")
st.bar_chart(csvData, x="Category", y="Value")

if "csvMinimum" not in st.session_state:
    st.session_state.csvMinimum = 0

st.slider("Minimum survey hours", 0, 30, key="csvMinimum")

filteredCSV = csvData[csvData["Value"] >= st.session_state.csvMinimum]

# Keep track of previous CSV statistics
if "csvMean" not in st.session_state:
    st.session_state.csvMean = None

if "csvMedian" not in st.session_state:
    st.session_state.csvMedian = None

if not filteredCSV.empty:
    fig2 = px.pie(filteredCSV, names="Category", values="Value",
                  title="Survey Study Hours")
    st.plotly_chart(fig2)

    meanCSV = round(filteredCSV["Value"].mean(), 2)
    medianCSV = round(filteredCSV["Value"].median(), 2)

    # Compare with previous values
    if st.session_state.csvMean is None:
        meanChangeCSV = None
        medianChangeCSV = None
    else:
        meanChangeCSV = round(meanCSV - st.session_state.csvMean, 2)
        medianChangeCSV = round(medianCSV - st.session_state.csvMedian, 2)

    st.metric("Mean survey hours", meanCSV, delta=meanChangeCSV)
    st.metric("Median survey hours", medianCSV, delta=medianChangeCSV)

    st.session_state.csvMean = meanCSV
    st.session_state.csvMedian = medianCSV

else:
    st.write("No data matches.")
    st.metric("Mean survey hours", "N/A")
    st.metric("Median survey hours", "N/A")
