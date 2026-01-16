# 📡 The Watchtower: Real-time System Monitor

**The Watchtower** is a lightweight, real-time dashboard designed to monitor system resources (CPU, RAM, Disk) during local development. 

Built with **Python** and **Streamlit**, this tool simulates the observability stack required in MLOps environments. It provides visualization of resource consumption, which is critical for identifying bottlenecks when deploying Machine Learning models or running intensive background services.

## 🚀 Features
- **Real-time Monitoring:** Updates CPU, RAM, and Disk metrics every 0.5 seconds.
- **Visual History:** Line chart visualization to track CPU load trends over time.
- **Alert System:** Automated visual warning triggers when CPU usage exceeds safety thresholds (80%).
- **OS Detection:** Automatically detects and displays host system information.

## 🛠️ Tech Stack
- **Python:** Core logic.
- **Streamlit:** Frontend dashboard interface.
- **Psutil:** System retrieval and cross-platform process utilities.

## 💻 How to Run
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install streamlit psutil
3. Run the application:
   ```bash
   streamlit run watchtower.py

## 🎯 Purpose & Motivation
Monitoring is the "heartbeat" of MLOps. Most ML projects fail not because the model is bad, but because the infrastructure supporting it fails silently.

I built **The Watchtower** to:
1.  **Bridge the Gap:** Transition from writing static Python scripts to building dynamic, live-updating infrastructure tools.
2.  **Resource Profiling:** Provide a way to profile how much memory a specific model (like a Transformer or CNN) consumes during inference before moving it to production.
3.  **Simulate Production Observability:** Practice the core principles of the "SRE (Site Reliability Engineering) Golden Signals"—specifically **Saturation** (how full your resources are).
