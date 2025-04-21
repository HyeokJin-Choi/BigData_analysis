import requests
import pandas as pd

def webAPI(year=2020, age_list=[14, 20, 30], rank=10):
    columnsList = ['대출순위', '제목', '작가', '출판사', '대출회수']
    raw_columns = ['no', 'bookname', 'authors', 'publisher', 'loan_count']
    result = []

    for a in age_list:
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

        result.append(df)
    return result

# 메인 실행 코드
print("*** 도서관 정보나루의 연도, 연령별 인기대출도서에 대한 분석 프로그램입니다. ***")
year = int(input("확인할 연도 입력: "))
n = int(input("확인하고 싶은 연령의 개수: "))
age = []

for i in range(n):
    a = int(input(f"{i+1}번째 연령 입력: "))
    age.append(a)

rank = int(input("몇 위까지 확인하시겠습니까? (ex. 10): "))

result = webAPI(year=year, age_list=age, rank=rank)

for d_i in range(n):
    print(f"\n{year}년도, {age[d_i]}세에게 인기가 많았던 상위 {rank}권의 도서입니다.\n")
    print(result[d_i])
