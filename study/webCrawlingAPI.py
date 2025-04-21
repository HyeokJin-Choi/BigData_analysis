import requests
import pandas as pd

def test(year=2020, age_list=[14, 20, 30], rank=10):
    df14, df20, df30 = None, None, None
    columnsList = ['대출순위', '제목', '작가', '출판사', '대출회수']
    raw_columns = ['no', 'bookname', 'authors', 'publisher', 'loan_count']
    age_index = 0

    for a in age:
        url = f"http://data4library.kr/api/loanItemSrch?authKey=92d0610b51b298034f363dbd3f366ba1c0415a0bb17dd1c0ac5dc5f40f6d5b04&startDt={year}-01-01&endDt={year}-12-31&age={a}&format=json"
        r = requests.get(url)
        data = r.json()

        books = []
        for d in data['response']['docs']:
            doc = d['doc']
            if int(doc['ranking']) <= rank:
                books.append({
                    'no': doc['no'],
                    'bookname': doc['bookname'],
                    'authors': doc['authors'],
                    'publisher': doc['publisher'],
                    'loan_count': doc['loan_count']
                })

        df = pd.DataFrame(books, columns=raw_columns)
        df.columns = columnsList

        print(df)



year = int(input("확인할 연도 입력: "))
n = int(input("확인하고 싶은 연령의 개수: "))
age = []

for i in range(n):
    a = int(input(f"{i+1}번째 연령 입력: "))
    age.append(a)

rank = int(input("몇 위까지 확인하시겠습니까? (ex. 10): "))


df_by_age = test(year=year, age_list=age, rank=rank)
