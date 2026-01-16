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