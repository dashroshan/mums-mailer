import json


def isMailSent(notice):
    """
    Checks whether the email for the latest notice has been sent.
    """

    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)
    return data["latestSentNotice"] == notice["title"]
