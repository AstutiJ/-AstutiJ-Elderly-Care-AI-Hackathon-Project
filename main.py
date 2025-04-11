import sys
import os

# Fix import path to your Agent folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'Agent')))

from Agent.health_monitor import HealthMonitorAgent
from Agent.reminder_agent import ReminderAgent
from Agent.alert_agent import AlertAgent

# Initialize agents
health_agent = HealthMonitorAgent('data/health_monitoring.csv')
reminder_agent = ReminderAgent('data/daily_reminder.csv')
alert_agent = AlertAgent()

# 🔧 LIMIT the number of alerts here
health_alerts = health_agent.check_vitals(max_alerts=10)  # Limit to 10 alerts only
alert_agent.receive_alerts(health_alerts)

# Show outputs
reminder_agent.show_reminders()
alert_agent.show_alerts()

