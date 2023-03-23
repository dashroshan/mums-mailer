import requests

from utils.login import login
from processing.latestNotice import getLatestNotice

s = requests.Session()

a = login(s, "b121046", "1337d@Roshan")
getLatestNotice(s)
