import time
from utils.sentStatus import isMailSent
from processing.sendEmail import sendEmail
from processing.latestNotice import getLatestNotice


def mainLoop():
    """
    Get the latest notice, and mail it if not done so already.
    """

    notice = getLatestNotice()
    if not isMailSent(notice):
        sendEmail(notice)
        print(f"Emails sent!\nNotice: {notice['title']}")
    else:
        print("Latest notice mailed already!")


consecutiveErrors = 0
while consecutiveErrors < 5:
    """
    Loop infinitely as long as nothing crashes for more than 5 consecutive times.
    """

    print("\n[LOOPING]")
    try:
        mainLoop()
        consecutiveErrors = 0
    except Exception as error:
        print("Error: ", error)
        consecutiveErrors += 1
    time.sleep(600)  # 10 minutes delay between each loop

print("\nStopping program due to frequent crashes!")
