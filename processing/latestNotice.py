import json
import requests
from utils.login import login
from utils.noticeList import getAllNotices
from utils.noticeDetails import getDetailedNotice


def getLatestNotice():
    """
    Returns the latest notice title, content, date, posted by, for, and attachment download link
    """

    session = requests.Session()

    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)

    isLoggedIn = login(session, data["loginId"], data["loginPass"])
    if not isLoggedIn:
        return False

    notices = getAllNotices(session)
    latestNotice = getDetailedNotice(session, notices[0])

    session.close()
    return latestNotice
