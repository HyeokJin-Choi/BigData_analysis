from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def hollys_store(result):
    for page in range(1,10):
        Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page # 페이지를 클릭하고 url을 가져올것.
        # "각 페이지 번호에 따라 매장 정보를 가져오는 URL을 생성함"
        print(Hollys_url) #  정상적으로 가져오는지 URL의 log 확인
        html = urllib.request.urlopen(Hollys_url) # 해당 페이지의 HTML 소스를 가져옴.
        soupHollys = BeautifulSoup(html, 'html.parser') # HTML을 파싱해서 원하는 데이터를 추출할 수 있도록 준비.
        tag_tbody = soupHollys.find('tbody') # 파싱된 HTML의 tbody태그를 가져옴.
        # print(tag_tbody, '여기서부터 tBody태그')
        for store in tag_tbody.find_all('tr'): # tbody태그의 tr태그에 접근
            if len(store) <= 3: # 유효하지 않은 데이터(컬럼 수 부족 등)를 건너뜀
                print(store) # 유효하지 않은 데이터 출력 
                break
            store_td = store.find_all('td') # tr태그의 td태그에 접근
            #print(store_td,'여기서부터 td태그')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone=store_td[5].string
            result.append([store_name]+[store_sido]+[store_address]+[store_phone]) #추출한 매장 정보를 리스트에 추가

    return

# 데이터 수집
result = []
hollys_store(result)

# DataFrame 생성
df = pd.DataFrame(result, columns=['매장명', '시도', '주소', '전화번호'])

# 시도 앞 두 글자 추출
df['시도앞2글자'] = df['시도'].str[:2]

# 주요 광역시/특별시만 필터링
major_cities = ['서울', '부산', '대구', '대전', '광주', '세종', '울산']
df_filtered = df[df['시도앞2글자'].isin(major_cities)]

# print(df_filtered.where(df['시도앞2글자'].isin(major_cities)).groupby('시도').agg(sido = ('시도','count')))

df_filtered = df[df['시도앞2글자'].isin(major_cities)]
result = df_filtered.groupby('시도앞2글자').agg(매장수=('시도', 'count'))
print(result)


# 결과 출력
print(df_filtered.head())
print(f"총 매장 수: {df_filtered.shape[0]}")
