import streamlit as st
import pandas as pd
import plotly.express as px

CSV_FILE = "traffic_log.csv"

st.set_page_config(page_title="Traffic Monitoring Dashboard", layout="wide")

st.title("🚦 Real-Time Traffic Monitoring with Energy Metrics")

# Load Data
try:
    df = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    st.error("CSV file not found. Run the listener script first.")
    st.stop()

# Add simulated energy column if not exists
if "energy" not in df.columns:
    df["energy"] = 5 + df["vehicleCount"] * 0.05  # base 5W + traffic factor

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Messages", len(df))
col2.metric("Unique Devices", df["device"].nunique())
col3.metric("High Traffic Alerts", len(df[df["vehicleCount"] > 50]))
col4.metric("Total Energy (Wh)", round(df["energy"].sum(), 2))

# Energy per device bar chart
st.subheader("🔋 Energy Consumption per Device")
energy_per_device = df.groupby("device")["energy"].sum().reset_index()
fig_energy = px.bar(energy_per_device, x="device", y="energy", title="Total Energy per Device", color="device")
st.plotly_chart(fig_energy, use_container_width=True, key="energy_chart")

# Plotly Pie Chart
st.subheader("📊 Message Distribution per Device")
device_counts = df["device"].value_counts().reset_index()
device_counts.columns = ["device", "count"]
fig_pie = px.pie(device_counts, values="count", names="device", title="Messages per Device", color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig_pie, use_container_width=True, key="pie_chart")

# High Traffic Table
st.subheader("🚨 High Traffic Alerts (vehicleCount > 50)")
high_traffic = df[df["vehicleCount"] > 50].sort_values(by="vehicleCount", ascending=False)
st.dataframe(high_traffic, use_container_width=True, key="high_traffic_table")

# Separate Time-series Charts
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("📈 Vehicle Count Over Time")
    fig_vehicle = px.line(df, x="timestamp", y="vehicleCount", color="device", markers=True, title="Vehicle Count Trend")
    st.plotly_chart(fig_vehicle, use_container_width=True, key="vehicle_line_chart")

with col_b:
    st.subheader("🔋 Energy Consumption Over Time")
    fig_energy_time = px.line(df, x="timestamp", y="energy", color="device", markers=True, title="Energy Consumption Trend")
    st.plotly_chart(fig_energy_time, use_container_width=True, key="energy_line_chart")