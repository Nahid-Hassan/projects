#!/bin/bash

meeting_info=$(zenity --forms \
    --title 'Meeting' --text 'Reminder Information' \
    --add-calendar 'Select Meet Date' --add-entry 'Email Subject: ' \
    --add-entry 'Receiver Mail: ' \
    --add-entry 'Receiver Name: ' \
    --add-entry 'Sender Name: ' \
    --forms-date-format='%Y-%m-%d' \
    2>/dev/null)

if [[ -n*$meeting_info ]]; then
    python3 send_reminders.py "$meeting_info"
fi
