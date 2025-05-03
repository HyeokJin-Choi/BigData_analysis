#%% bar 차트 그리기
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import zscore

# 데이터
students = ["철수", "영희", "민수", "지민", "하늘", "수진", "태호", "서연", "도윤", "유진"]
scores = [72, 85, 90, 65, 78, 95, 88, 70, 60, 80]

# 데이터프레임 생성
df = pd.DataFrame({"이름": students, "점수": scores})
df["표준점수"] = zscore(df["점수"])

# 스타일 설정
sns.set(style="whitegrid")

# 1. 점수 바 차트
plt.figure(figsize=(10, 5))

# 바 차트 그리기
sns.barplot(x="이름", y="점수", data=df, palette="pastel")

# 평균 점수에 수평선 추가
plt.axhline(y=df["점수"].mean(), color="red", linestyle="--", label="평균 점수")

# 제목 설정
plt.title("학생별 수학 점수")

# 범례 추가 (선택 사항)
plt.legend()

# 레이아웃 조정
plt.tight_layout()

# 그래프 표시
plt.show()


