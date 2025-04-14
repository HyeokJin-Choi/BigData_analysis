from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def hollys_store(result):
    for page in range(1,10):
        Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store' %page
        print(Hollys_url)
        html = urllib.request.urlopen(Hollys_url)
        soupHollys = BeautifulSoup(html, 'html.parser') # 파싱을 해야 URL을 사용할 수 있음
        tag_tbody = soupHollys.find('tbody')
        for store in tag_tbody.find_all('tr'):
            if len(store) <= 3:
                break
            store_td = store.find_all('td')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone=store_td[5].string
            result.append([store_name]+[store_sido]+[store_address]+[store_phone])

    return

# ✅ 호출 및 결과 확인
result = []
hollys_store(result)
df = pd.DataFrame(result, columns=['매장명', '시도', '주소', '전화번호'])

# 결과 일부 출력
print(df.head())
