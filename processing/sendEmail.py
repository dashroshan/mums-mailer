import json
import smtplib
from email.mime.text import MIMEText
from utils.updateSentNotice import updateSentNotice


def sendEmail(notice):
    """
    Send email for the given notice according to config.json
    """

    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)

    emailId = data["emailId"]
    emailPass = data["emailPass"]
    recipients = data["toEmail"]

    content = f'Date: {notice["date"]}\nPosted by: {notice["postedBy"]}\nFor: {notice["for"]}\nAttachment: {notice["attachment"]}\n\n{notice["content"]}'

    msg = MIMEText(content)
    msg["Subject"] = "[Notice] " + notice["title"]
    msg["From"] = data["emailId"]
    msg["To"] = ", ".join(recipients)
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    smtp_server.login(emailId, emailPass)
    smtp_server.sendmail(emailId, recipients, msg.as_string())
    smtp_server.quit()
    updateSentNotice(notice["title"])
