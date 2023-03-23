from headers import headers
from bs4 import BeautifulSoup


def getAttachmentUrl(session, slug):
    """
    Returns the downloadable url for the given attachment slug.
    """

    req = session.get(
        "https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/nb/" + slug,
        headers={
            "Referer": "https://hib.iiit-bh.ac.in/m-ums-2.0/start/here/?w=1920&h=930",
            **headers,
        },
    )
    attachmentBody = BeautifulSoup(req.content, "lxml")
    attachmentUrl = attachmentBody.find("iframe")["src"]
    attachmentUrl = "https://hib.iiit-bh.ac.in/m-ums-2.0" + attachmentUrl[5:]
    return attachmentUrl
