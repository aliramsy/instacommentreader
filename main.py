import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime


link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'

time = int(datetime.now().timestamp())

payload = {
    'username': '',
    'enc_password': '',
    'queryParams': {},
    'optIntoOneTap': 'false'
}

with requests.Session() as s:
    #r = s.get(link)
    r = s.get(link,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
    r = s.post(login_url, data=payload, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    })
    print(r.content)
    print(r.status_code)
    print(r.headers)
    print(r.cookies)

cookies = {"csrftoken":"QlXpKrvuUnRca6CcUbUXUdkB1lNRPfeU"}