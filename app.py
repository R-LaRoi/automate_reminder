#app.py
import argparse
import subprocess
import sys
import os

def main():
    parser = argparse.ArgumentParser(
        description="Choose and run a desktop reminder system. This script acts as a launcher.",
        formatter_class=argparse.RawTextHelpFormatter # Keeps newlines in help
    )

    parser.add_argument('--mode', type=str, choices=['interval', 'scheduled'], required=True,
                        help='''Choose reminder mode:
  "interval": For repeating notifier (e.g., every 30 mins). Requires -m, -i, -t.
  "scheduled": For specific-time notifier (e.g., at 2 PM, 3 PM). No additional args needed.''')

    # Arguments that will be passed *through* to interval_notifier.py if --mode interval is chosen
    parser.add_argument('-m', '--message', type=str,
                        help='[Interval Mode] Reminder message to display. Required when --mode interval.')
    parser.add_argument('-i', '--interval', type=int, default=60,
                        help='[Interval Mode] Interval in minutes between notifications (default: 60).')
    parser.add_argument('-t', '--times', type=int, default=0,
                        help='[Interval Mode] Number of times to show the notification (0 for infinite).')

    args = parser.parse_args()

    # Determine the Python executable to use
    python_executable = sys.executable

    if args.mode == 'interval':
        if not args.message:
            parser.error("--message is required when --mode is 'interval'")

        print(f"Launching interval reminder via {python_executable} interval_notifier.py...")
        command = [
            python_executable,
            os.path.join(os.path.dirname(__file__), 'interval_notifier.py'), # Ensures correct path
            '-m', args.message,
            '-i', str(args.interval),
            '-t', str(args.times)
        ]
        # Use subprocess.run to execute the other script
        # check=True will raise an error if the subprocess fails
        # If you want it to run in the background without main_app waiting,
        # you'd use subprocess.Popen and might need to detach it.
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running interval_notifier.py: {e}")
            sys.exit(1)

    elif args.mode == 'scheduled':
        # Warn if interval-specific args are provided for scheduled mode
        if args.message or args.interval != 60 or args.times != 0:
            print("Warning: -m, -i, -t arguments are ignored when --mode is 'scheduled'.")
            print("Scheduled notifier are defined within scheduled_notifier.py itself.")

        print(f"Launching scheduled notifier via {python_executable} scheduled_notifier.py...")
        command = [
            python_executable,
            os.path.join(os.path.dirname(__file__), 'scheduled_notifier.py') # Ensures correct path
        ]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running scheduled_notifier.py: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()