from headers import headers
from bs4 import BeautifulSoup


def getAllNotices(session):
    """
    Returns the list of urls for details of 50 latest notices with their titles
    """

    # The below request is to emulate an actual user behaviour as the server blocks attempts to get the notice list directly
    session.get(
        "https://hib.iiit-bh.ac.in/m-ums-2.0/start/here/setWindowSize.php",
        headers={
            "Referer": "https://hib.iiit-bh.ac.in/m-ums-2.0/start/login/?client=iiit",
            **headers,
        },
    )

    # Getting the notice list
    req = session.get(
        "https://hib.iiit-bh.ac.in/m-ums-2.0/app.misc/nb/docList.php",
        headers={
            "Referer": "https://hib.iiit-bh.ac.in/m-ums-2.0/start/here/?w=1920&h=930",
            **headers,
        },
    )

    notices = BeautifulSoup(req.text, "lxml").find_all("font", {"color": "red"})
    data = [{"url": n.parent["href"], "title": n.string} for n in notices]
    return data
