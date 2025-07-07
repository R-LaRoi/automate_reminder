import time
import argparse
import sys
import os

try:
    from pync import Notifier
except ImportError:
    print("The 'pync' library is required. Install it with 'pip install pync' and ensure 'terminal-notifier' is installed via Homebrew.")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Pop up desktop notifications at set intervals for reminders.")
    parser.add_argument('-m', '--message', type=str, required=True, help='Reminder message to display')
    parser.add_argument('-i', '--interval', type=int, default=60, help='Interval in minutes between notifications (default: 60)')
    parser.add_argument('-t', '--times', type=int, default=0, help='Number of times to show the notification (0 for infinite)')
    args = parser.parse_args()

    # Get absolute path to star_icon.png in the workspace
    icon_path = os.path.abspath('star_icon.png')

    count = 0
    while True:
        Notifier.notify(
            args.message,
            title='Reminder',
            subtitle='Time to recharge!',
            sound='Glass',
            appIcon=icon_path
        )

        count += 1
        if args.times > 0 and count >= args.times:
            break
        time.sleep(args.interval * 60)

if __name__ == "__main__":
    main()