#!/usr/bin/env python3

# import packages
import datetime
import email
import smtplib
import sys


def usage():
    print("Send_reminders: Send meeting reminders")
    print("Send reminders 'date|Meeting Title|Emails|Receiver Name| Sender Name' ")
    
    return 1


def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")


def message_template(meeting_date, mail_subject, receiver_name, sender_name):
    messages = email.message.EmailMessage()
    weekday = dow(meeting_date)
    messages['Subject'] = f'Meeting reminder: {mail_subject}'
    messages.set_content(f'''
    Dear {str(receiver_name).title()},\n
    Assalamualkum. Hope you are good.\n
    This is a quick mail to remind you all that we have a meeting about: "{mail_subject}" the {weekday} {meeting_date}.\n
    See you there,
    {str(sender_name).title()}''')
    return messages


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


def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        meeting_date, mail_subject, receiver_mail, receiver_name, sender_name = sys.argv[1].split('|')
        message_body = str(message_template(meeting_date, mail_subject, receiver_name, sender_name))
        send_message(receiver_mail, message_body)
        print("Successfully send reminders to: {}".format(receiver_mail))
    except Exception as e:
        print("Failure to send email{}".format(e), file=sys.stderr)


if __name__ == '__main__':
    sys.exit(main())