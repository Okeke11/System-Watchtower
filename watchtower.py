import streamlit as st
import psutil
import time
import platform

st.set_page_config(
    page_title="The Watchtower: System Monitor",
    page_icon="📡",
    layout="wide"
)

st.title("📡 The Watchtower")
st.markdown("### Real-time System Resource Monitor for MLOps")

# Display static system info
col1, col2 = st.columns(2)
with col1:
    st.info(f"**OS:** {platform.system()} {platform.release()}")
with col2:
    st.info(f"**Node Name:** {platform.node()}")

st.divider()

# --- Placeholders ---
alert_placeholder = st.empty() 

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    cpu_placeholder = st.empty()

with kpi2:
    ram_placeholder = st.empty()

with kpi3:
    disk_placeholder = st.empty()

st.divider()
chart_placeholder = st.empty()

cpu_history = []

while True:
    # interval=0.5 blocks for 0.5s to calculate CPU usage
    cpu_percent = psutil.cpu_percent(interval=0.5)
    
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    ram_used = round(ram.used / (1024 ** 3), 2) # Convert to GB
    
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent

    cpu_history.append(cpu_percent)
    if len(cpu_history) > 50:
        cpu_history.pop(0)

    # If CPU usage is > 80%, show an error. Otherwise, clear the placeholder.
    if cpu_percent > 80:
        with alert_placeholder:
            st.error("⚠️ HIGH CPU USAGE DETECTED! Potential Bottleneck.")
    else:
        alert_placeholder.empty()

    with cpu_placeholder:
        st.metric(label="CPU Usage", value=f"{cpu_percent}%")

    with ram_placeholder:
        st.metric(label="RAM Usage", value=f"{ram_percent}%", delta=f"{ram_used} GB Used")
        
    with disk_placeholder:
        st.metric(label="Disk Usage", value=f"{disk_percent}%")
    
    with chart_placeholder:
        st.line_chart(cpu_history, height=200)
        st.caption("CPU Usage History (Last 50 ticks)")