# Automate Your Day: Time Schedule

| Time     | Task           |
| :------- | :------------- |
| 8:00 AM  | Open Workspace |
| 8:00 AM  | Online Course  |
| 11:00 PM | Open Facebook  |
| 12:00 PM | Close Facebook |

## Task

If `time == 8.00 AM` then do;

1. Mount Workspace
2. Open Google Chrome
3. Open Coursera, Udacity, Youtube, Mail, and Github Account.
4. Open Vscode with path to `workspace`

## Security

1. If you are not sit in front of laptop, then laptop `logged out` automatically and immediately.

## Future Task

1. Take input from `Google Calender`

## Code file overview

Firstly we create a daemon for running all the script as background process.

1. `fb.py`: Activate when your clock time is around 11:00 PM.
1. `ts.py`: This script create logical statement when which script is run.
