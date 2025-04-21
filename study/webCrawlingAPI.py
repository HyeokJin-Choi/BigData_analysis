import requests
import pandas as pd
import calendar # 정확한 날짜의 계산을 위해서 사용

def webAPI(api = "92d0610b51b298034f363dbd3f366ba1c0415a0bb17dd1c0ac5dc5f40f6d5b04",year=2020, month=1, age_list=[14, 20, 30], rank=10):
    columnsList = ['대출순위', '제목', '작가', '출판사', '대출회수']
    raw_columns = ['no', 'bookname', 'authors', 'publisher', 'loan_count']
    result = []

    # 월과 마지막 날짜 계산
    month_str = str(month).zfill(2)  # '01', '02', ..., '12' <- 월은 9월달 이하면 숫자 앞에 0을 붙여야함.
    end_day = calendar.monthrange(year, month)[1]  # 정확한 말일자 계산 <- 예시로 2월은 28일까지 있음. 무조건 31일이 아님.

    for a in age_list:
        url = (
            f"http://data4library.kr/api/loanItemSrch?"
            f"authKey={api}"
            f"&startDt={year}-{month_str}-01"
            f"&endDt={year}-{month_str}-{end_day}"
            f"&age={a}&format=json"
        )

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

# *** 메인 실행 코드 ***
print("*** 도서관 정보나루의 연도, 월, 연령별 인기대출도서 분석 프로그램 ***")
api = str(input("도서관 정보나루에서 발급받으신 API를 입력: "))
year = int(input("확인할 연도 입력: "))
month = int(input(f"{year}년도의 확인할 월 입력 (ex. 1월이면 1, 2월이면 2 ...): "))
n = int(input("확인하고 싶은 연령의 개수: "))
age = []
for i in range(n):
    a = int(input(f"{i+1}번째 연령 입력: "))
    age.append(a)

rank = int(input("몇 위까지 확인하시겠습니까? (ex. 10): "))

result = webAPI(api = api,year=year, month=month, age_list=age, rank=rank)

for d_i in range(n):
    print(f"\n{year}년 {month}월, {age[d_i]}세에게 인기 있었던 상위 {rank}권의 도서입니다.")
    print(result[d_i])

# 과제용
# 2025 년 14,20,30 대의 (1월) rank 10
df14 = pd.DataFrame(result[0])
df20 = pd.DataFrame(result[1])
df30 = pd.DataFrame(result[2])


