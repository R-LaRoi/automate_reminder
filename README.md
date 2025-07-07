# Automate Reminders

A Python project for scheduling and displaying desktop notifications as reminders at specific times or intervals. Supports custom messages, notification sounds, and custom icons.

## Features

- **Scheduled Reminders:** Set notifications for specific times of day.
- **Interval Reminders:** Pop up notifications at regular intervals.
- **Custom Notification Icon:** Use your own PNG icon (e.g., `star_icon.png`).
- **Sound Alerts:** Play a system sound with each notification.
- **Cross-platform:** Works on macOS (with `pync` and `terminal-notifier`).

## Requirements

- Python 3.x
- [pync](https://github.com/setem/pync) (`pip install pync`)
- [schedule](https://pypi.org/project/schedule/) (`pip install schedule`)
- [terminal-notifier](https://github.com/julienXX/terminal-notifier) (macOS, install via Homebrew: `brew install terminal-notifier`)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/R-LaRoi/automate_reminder.git
   cd automate_reminder
   ```

2. **Install Python dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **(macOS only) Install terminal-notifier:**
   ```sh
   brew install terminal-notifier
   ```

## Usage

### Scheduled Reminders

Edit `scheduled_notifier.py` to customize your reminders and times:

```python
reminders = [
    ("Check Slack!", "15:00"),  # 3 PM
    ("Client Call", "14:00"),   # 2 PM
    ("Recap with team", "16:00")# 4 PM
]
```

Run the script:

```sh
python scheduled_notifier.py
```

### Interval Reminders

If you have `interval_notifier.py`, you can use it to set reminders at regular intervals:

```sh
python interval_notifier.py -m "Take a break!" -i 30 -t 5
```

- `-m`: Message to display
- `-i`: Interval in minutes
- `-t`: Number of times to show the notification (0 for infinite)

### Custom Icon

Place your PNG icon (e.g., `star_icon.png`) in the project directory. The scripts will use this icon for notifications.

## Example Notification

- Title: Reminder
- Subtitle: Time to recharge!
- Sound: Glass
- Icon: `star_icon.png`

## License

MIT License
