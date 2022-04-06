import smtplib, ssl
import getpass

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = input("Enter Sender's Email: ")  # Enter your address
receiver_email = input("Enter Receiver's Email: ")  # Enter receiver address
password = getpass.getpass('Password:')
message = """\
Subject: Subject

This message is sent from Python to multiple people.\
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)