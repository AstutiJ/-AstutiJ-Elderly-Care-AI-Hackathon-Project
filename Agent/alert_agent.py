class AlertAgent:
    def __init__(self):
        self.alerts = []

    def receive_alerts(self, new_alerts):
        self.alerts.extend(new_alerts)

    def show_alerts(self):
        print("\n🚨 Alerts:")
        for alert in self.alerts:
            print(alert)
