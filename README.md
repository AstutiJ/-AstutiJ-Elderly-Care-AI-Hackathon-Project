# 🧓 Elderly Care AI Assistant 🧠
> Built for Hack the Future: A Gen AI Sprint – Problem Statement 4: Empowering Elderly Care with Multi-Agent AI System

---

## 🗂️ Overview

This project is a multi-agent AI system designed to assist in elderly care by:
- 🔍 Monitoring vital health parameters (like heart rate & blood pressure)
- ⏰ Reminding users of important tasks like medications and appointments
- 🚨 Generating alerts and notifying caregivers in case of abnormalities

---

## 🧠 Agents in the System

| Agent | Role |
|-------|------|
| **Health Monitor Agent** | Reads real-time vitals from CSV, detects anomalies (e.g., abnormal heart rate or BP) |
| **Reminder Agent** | Displays scheduled tasks (medications, hydration, appointments) |
| **Alert Agent** | Collects alerts from other agents and displays warnings |

---

## 📂 Project Structure
elderly_care_ai/
│
├── agents/                 # All agent code
│   ├── health_monitor.py
│   ├── behavior_agent.py
│   ├── reminder_agent.py
│   └── alert_agent.py
│
├── data/                   # Store the CSV files here
│   ├── health_monitoring.csv
│   ├── safety_monitoring.csv
│   └── daily_reminder.csv
│
├── main.py                 # Where you run everything together
├── requirements.txt        # Add libraries like pandas
└── README.md               # Project overview
## 🛠️ Technologies Used

- Python 3.x 🐍
- pandas 📊
- Command-line interface (CLI) for agent output
## 🚀 How to Run the Project

1. Clone this repo:
```bash
git clone https://github.com/AstutiJ/-AstutiJ-Elderly-Care-AI-Hackathon-Project.git
cd Elderly-Care-AI-Hackathon-Project
Install dependencies:
pip install -r requirements.txt

Run the system:
python main.py

You’ll see:
Reminders displayed from the dataset
Vital checks with alert messages
Clean output in terminal

🏁 Conclusion
This project showcases how AI agents can collaborate to support elderly individuals by improving their:
-Safety
-Medication compliance
-Peace of mind
-It demonstrates a working prototype using real datasets and simple automation logic — ready for further development or deployment.

