# sendSMS
Send T-Mobile Text Messages using through Gmail and SMTP

## Setting Up

#### From Address
```
EMAIL_ADDRESS = os.environ.get('MAIL_TEST') if os.environ.get('MAIL_TEST') else ''
EMAIL_PASSWORD = os.environ.get('PASSWORD_TEST') if os.environ.get('PASSWORD_TEST') else ''
```
Here, there is a ternary operator which takes an enviroment variable, and if there is none it will take a string.
You must add either an enviroment variable, or specify your email and password in your string.

#### To Address
```
phoneNumbers = []
```
This list is used to send the text messages to the phone numbers. The addresses must be separated with a comma.

#### Message
```
subject = 'Test'
message = 'Hello World'
```
The subject and body is used to set the content of your text message.

## Executing the application
* Install python
* Once installed, run the script.
