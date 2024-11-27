from email.message import EmailMessage  # this comes with python
import ssl
import smtplib

email_sender = 'mrkiariekarori@gmail.com'
email_pw = 'password'

email_receiver = 'kevkiarie@yahoo.com'

subject = 'Please dont forget to subscribe for more exiting news'

body = "Please, we have noticed that you watch our videos without subscribing,kindly condiser doing so, cheers,kiarie."

em = EmailMessage()
em['From'] =email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_pw)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
