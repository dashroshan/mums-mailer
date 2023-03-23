import requests
from utils.login import login
from utils.noticeList import getAllNotices
from utils.noticeDetails import getDetailedNotice
from utils.updateSentNotice import updateSentNotice


def getLatestNotice(session):
    session = requests.Session()
    notices = getAllNotices(session)
    latestNotice = getDetailedNotice(session, notices[0])
    updateSentNotice(latestNotice["title"])
    print(latestNotice)
