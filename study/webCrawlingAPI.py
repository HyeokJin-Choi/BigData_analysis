import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://data4library.kr/api/loanItemSrch?authKey=92d0610b51b298034f363dbd3f366ba1c0415a0bb17dd1c0ac5dc5f40f6d5b04&startDt=2022-01-01&endDt=2022-03-31&age=20&format=json"
r = requests.get(url)

data = r.json()
print(data)
