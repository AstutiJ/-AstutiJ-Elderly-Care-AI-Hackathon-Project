import pandas as pd

class ReminderAgent:
    def __init__(self, csv_path):
        self.reminders = pd.read_csv(csv_path)
        self.reminders.columns = self.reminders.columns.str.strip()
        print("\n✅ Reminder Columns:", list(self.reminders.columns))  # for debug

    def show_reminders(self):
        print("\n🕒 Daily Reminders (Top 10):")
        # Show only the first 10 scheduled reminders for demo
        for index, row in self.reminders.head(10).iterrows():
            time = row.get('Scheduled Time', 'N/A')
            task = row.get('Reminder Type', 'N/A')
            print(f"🔔 {time} - {task}")
