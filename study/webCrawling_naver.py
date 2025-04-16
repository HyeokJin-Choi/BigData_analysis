# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 06:09:17 2025

@author: ekoh2
"""
#%% code= 뒤의 숫자를 가져와야 원하는 webCrawling이 가능한 코드
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_stock_codes(pages=5):
    base_url = "https://finance.naver.com/sise/sise_market_sum.naver?page=" #url주소
    stock_list = []

    for page in range(1, pages + 1): # 1페이지부터 5페이지까지지
        url = base_url + str(page) # 숫자인 페이지를 문자형태로 변경해서 url추가.
        headers = {'User-Agent': 'Mozilla/5.0'}
        res = requests.get(url, headers=headers) # url주소에 get을 사용해서 요청함.
        soup = BeautifulSoup(res.text, 'html.parser') # url파싱.

        table = soup.select('table.type_2')[0] # table의 class를 확인해서 해당 class에 부여된 type_2만 본다는 뜻.
        rows = table.select('tr')[2:] # 왜 2인지? 1이 아니라?

        for row in rows:
            cols = row.select('td')
            if len(cols) > 1:
                link_tag = cols[1].select_one('a')# <a href="/item/main.naver?code=005930" class="tltle">삼성전자</a> 
                if link_tag:
                    name = link_tag.text.strip()
                    href = link_tag['href']
                    code = href.split('=')[-1]
                    stock_list.append({'종목명':name, '종목코드':code})

    return pd.DataFrame(stock_list)

# 사용 예시
df = get_stock_codes(pages=3)
print(df.head())
#%%
x2_str="""
<books>
    <book>
        <name>"xml 변환해보기"</name>
        <func>"findtext"</func>
        <where>"book1"</where>
    </book>
    <book>
        <name>"API 스크래핑"</name>
        <func>"findall"</func>
        <where>"book2"</where>
    </book>
</books>
"""
