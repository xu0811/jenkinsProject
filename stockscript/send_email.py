
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fetchHistory import fetchHistory

def sendmail(msg):
    sender_email = "ready6302016@gmail.com"
    receiver_email = "ready6302016@gmail.com"
    #receiver_email = "hsu0811@gmail.com"
    password = "06302016"

    message = MIMEMultipart("alternative")
    message["Subject"] = "New picks"
    message["From"] = "Python Script"
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    """
    new_text = msg
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(new_text, "plain")
    #part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    #message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )