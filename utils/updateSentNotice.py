import json


def updateSentNotice(latestNoticeTitle):
    """
    Updates the latestSentNotice attribute in config.json to detect new notices
    """

    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["latestSentNotice"] = latestNoticeTitle

    with open("config.json", "w") as jsonFile:
        json.dump(data, jsonFile)
