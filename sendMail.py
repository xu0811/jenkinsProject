import smtplib

def sendmail(msg):
    gmail_user = 'ready6302016@gmail.com'
    gmail_password = '06302016'

    sent_from = gmail_user
    to = ['sean0811@gmail.com']
    subject = 'Important Message - ' + msg
    body = 'Hey, what\'s up?\n\n- You'

    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ("Email sent!")
    except:
        print ("Something went wrong...")
