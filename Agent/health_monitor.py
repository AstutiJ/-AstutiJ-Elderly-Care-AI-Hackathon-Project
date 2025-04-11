import pandas as pd

class HealthMonitorAgent:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)
        self.data.columns = self.data.columns.str.strip()
        print("\n✅ Health Columns:", list(self.data.columns))  # Debug

    def check_vitals(self, max_alerts=10):
        alerts = []
        for index, row in self.data.iterrows():
            heart_rate = row.get('Heart Rate')
            bp_flag = row.get('Blood Pressure Below/Above Threshold (Yes/No)', 'No')

            # Basic checks
            if pd.notna(heart_rate) and (heart_rate < 60 or heart_rate > 100):
                alerts.append(f"⚠️ Abnormal heart rate: {heart_rate} bpm")

            if bp_flag.strip().lower() == 'yes':
                alerts.append(f"⚠️ Blood pressure out of threshold")

            if len(alerts) >= max_alerts:
                break  # Limit to max_alerts

        return alerts
