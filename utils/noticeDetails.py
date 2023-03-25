from headers import headers
from bs4 import BeautifulSoup
from utils.attachment import getAttachmentUrl


def getDetailedNotice(session, slug):
    """
    Returns notice title, content, date, posted by, for, and attachment download url for the given notice
    """

    noticeUrl = "https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/nb/" + slug["url"]

    req = session.get(
        noticeUrl,
        headers={
            "Referer": "https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/nb/docList.php",
            **headers,
        },
    )

    noticeBody = BeautifulSoup(req.content, "lxml")
    noticeContent = noticeBody.find(class_="well well-lg col-lg-10 col-lg-offset-1 text-left")

    noticeDate = noticeBody.find(class_="btn btn-primary").get_text()[6:]
    noticePostedBy = noticeBody.find(class_="btn btn-success").get_text()[11:]
    noticeFor = noticeBody.find(class_="btn btn-danger").get_text()[11:]

    noticeAttachment = noticeBody.find(
        class_="btn btn-info btn-md btn-danger hvr-wobble-top"
    )
    if noticeAttachment:
        noticeAttachment = getAttachmentUrl(session, noticeAttachment["href"])
    # The url provided here leads to another page with attachment in iframe, so the download url needs to be fetched separately

    noticeData = {
        "title": slug["title"],
        "content": noticeContent,
        "date": noticeDate,
        "postedBy": noticePostedBy,
        "for": noticeFor,
        "attachment": noticeAttachment,
    }

    return noticeData
