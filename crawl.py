from bs4 import BeautifulSoup
import requests


cookies = {"csrftoken":"hlDWW1v0jmFhnXrvcYxje8ocKNBGGbeD"}
content= requests.get("https://www.instagram.com/p/CgpTDCCpkum/",cookies=cookies).text
soup= BeautifulSoup(content, "lxml")

main_tags= soup.find_all("div", class_="rq0escxv l9j0dhe7 du4w35lb")
print(main_tags)