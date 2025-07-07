import time
import sys
import os
import schedule 

try:
    from pync import Notifier
except ImportError:
    print("The 'pync' library is required. Install it with 'pip install pync' and ensure 'terminal-notifier' is installed via Homebrew.")
    sys.exit(1)

def set_scheduled_reminder(message, scheduled_time_str):
    icon_path = os.path.abspath('star_icon.png')

    def job():
        Notifier.notify(
            message,
            title='Scheduled Reminder', # Changed title for clarity
            subtitle='Specific Time Alert!',
            sound='Glass',
            appIcon=icon_path
        )
        print(f"Reminder triggered: {message} at {scheduled_time_str}")

    schedule.every().day.at(scheduled_time_str).do(job)
    print(f"Set scheduled reminder: '{message}' for {scheduled_time_str}")

def run_scheduled_reminders(): 
    # Define your reminders here as a list of tuples: (message, time_string)
    reminders = [
        ("Check Slack!", "15:00"),  # 3 PM EDT
        ("Client Call", "14:00"),    # 2 PM EDT
        ("Recap with team", "16:00") # 4 PM EDT
    ]

    for message, time_str in reminders:
        set_scheduled_reminder(message, time_str)

    print("All scheduled reminders set. The script will now run in the background to trigger them.")
    print("Press Ctrl+C to exit.")

    while True:
        schedule.run_pending()
        time.sleep(1) # Check every second for pending jobs

if __name__ == "__main__":
    run_scheduled_reminders()