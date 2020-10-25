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