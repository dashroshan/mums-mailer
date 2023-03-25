import json
import smtplib
from utils.htmlEmail import makeHtml
from utils.trimString import trimString
from utils.updateSentNotice import updateSentNotice
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmail(notice):
    """
    Send email for the given notice according to config.json
    """

    # Read the sender account credentials and recipients
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)

    emailId = data["emailId"]
    emailPass = data["emailPass"]
    recipients = data["toEmail"]

    # Assemble the email content
    msg = MIMEMultipart()
    msg["Subject"] = "[Notice] " + trimString(notice["title"], 3)
    msg["From"] = data["emailId"]
    msg["To"] = ", ".join(recipients)
    msg.attach(MIMEText(makeHtml(notice), "html"))

    # Send the email
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.login(emailId, emailPass)
    smtp_server.sendmail(emailId, recipients, msg.as_string())
    smtp_server.quit()

    # Update last sent notice title in config.json
    updateSentNotice(notice["title"])
