# Projects

## easyreminder

### Clone and Run

```sh
> git clone https://github.com/Nahid-Hassan/projects.git
> cd projects
> cd easyreminder
```

Lets' first you need to done some work ....
In send_reminders.py file you need to change those two lines with necessary information.

```py
def send_message(receiver_mail, message_body):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    sender = '<-----------put-sender-gmail-is-here-------->'

    smtp.starttls()

    # Authentication
    # sender_email_id_password = input("Enter your mail password")
    sender_email_id_password = "<----put-google-app-password-is-here---->"
    smtp.login(sender, sender_email_id_password)

    smtp.sendmail(sender, receiver_mail, message_body)
    smtp.quit()
```

`Note`: To generate Google app password...First visit [Google Account Security](https://myaccount.google.com/security). Next, in `Signing in to Google` section you can generate `Google App Password`. `Google App Password` is `16 digit` password.

Finally for run...

```sh
> bash meeting_reminder.sh
```

### Advanced Work `pprofile3` Test for Slowness of this Little Reminder Tool

First we check how many times our main script send_reminders.py take.
To check this we run,

```sh
# First we make send_reminders.py script is executable
> chmod +x send_reminders.py

# Next run `time` command with send_reminders.py script
> time ./send_reminders "2020-10-29|Example|example@gmail.com"
..............
real 0m0.119s
user 0m0.099s
sys 0m0.017s
```

```sh
> p
profile3 -f callgrind -o profile.out ./send_reminders "2020-10-29|Example|example@gmail.com"
> ls
profile.out
> kcachegrind profile.out
```
