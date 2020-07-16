from email.message import EmailMessage
import smtplib, os, sys, sqlite3
#Set environment variable use string
EMAIL_ADDRESS = os.environ.get('MAIL_TEST') if os.environ.get('MAIL_TEST') else ''
EMAIL_PASSWORD = os.environ.get('PASSWORD_TEST') if os.environ.get('PASSWORD_TEST') else ''
SMS_GATEWAY='@tmomail.net'

# Establish secure session with gmail out SMTP server with gmail account
server = smtplib.SMTP('smtp.gmail.com', '587')
server.starttls()
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

#Message to be sent out
subject = 'Test'
message = 'Hello World'

phoneNumbers = []
    
for index in range(len(phoneNumbers)):
    TO_PHONE = phoneNumbers[index] + SMS_GATEWAY
    #Create message into phone format
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_PHONE
    msg['Subject'] = subject
    msg.set_content(message)
    SMS = msg.as_string()

    #send text message through SMS gateway of number
    server.sendmail(EMAIL_ADDRESS, TO_PHONE, SMS)

    server.close()
