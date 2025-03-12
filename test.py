import pandas as pd
import numpy as np

# 데이터 입력
#code1
temp = pd.Series([-0.8, -0.1, 7.7, 13.8, 18.0, 22.4,
                  25.9, 25.3, 21.0, 14.0, 9.6, -1.4])
print(temp)  # temp의 내용 확인

# 월 이름을 레이블 인덱스로 지정하기
print(temp.index)  # 인덱스 내용 확인
temp.index = ['1월', '2월', '3월', '4월',  # 월 이름을 인덱스로 지정
              '5월', '6월', '7월', '8월',
              '9월', '10월', '11월', '12월']
print(temp)  # temp의 내용 확인

#code2
salary = pd.Series([20, 15, 18, 30])  # 레이블 인덱스가 없는 시리즈 객체
score = pd.Series([75, 80, 90, 60],
                  index=['KOR', 'ENG', 'MATH', 'SOC'])
print(salary)
print(score)


# 1. CSV 파일 읽기
file_path = 'testCSV/전국대학및전문대학정보표준데이터.csv'
data = pd.read_csv(file_path, usecols=['학교명', '시도명', '소재지도로명주소'])
data.fillna('', inplace=True)  # NaN 값 처리
# 2. 대학명 중복 제거
data['학교명'] = data['학교명'].str.split().str[0]  # 첫 번째 단어 기준으로 추출
data = data.drop_duplicates(subset=['학교명'])  # 중복 제거

# filtered_data = data[data['학교명'].str.endswith('아대학교')]
# # 결과 출력
# print(filtered_data)

file_path2 = 'testCSV/주민등록 인구 및 세대현황.csv'
data2 = pd.read_csv(file_path2, encoding='euc-kr')
data2.fillna('',inplace=True)
print(data2)
len(data)

print(data.loc[(data['학교명']=='동아대학교') | (data['학교명'].str.startswith('동국'))])

print(temp.where(temp > temp.mean()).dropna().index)
