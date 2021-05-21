import requests
from bs4 import  BeautifulSoup
search="weather in kullu"
url=f"https://www.google.com/search?q=weather&oq=wheather&aqs=chrome.1.69i57j0l7.5284j1j7&sourceid=chrome&ie=UTF-8={search}"
r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser")
update=s.find("div", class_=""vk_bk sol-tmp").text
print(update)