#%% 라인 그래프
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import zscore
import pandas as pd

# 데이터
students = ["철수", "영희", "민수", "지민", "하늘", "수진", "태호", "서연", "도윤", "유진"]
scores = [72, 85, 90, 65, 78, 95, 88, 70, 60, 80]

# 표준 점수 계산
z_scores = zscore(scores)

# 데이터프레임 생성
df = pd.DataFrame({"이름": students, "점수": scores, "표준점수": z_scores})
# 라인 그래프 그리기
plt.figure(figsize=(10, 5))
sns.lineplot(x=df["이름"], y=df["표준점수"], marker="o", color='blue', label="표준 점수")

# 평균 수평선 추가 (Z=0)
plt.axhline(0, color="gray", linestyle="--", label="평균 (Z=0)")

# 제목 설정
plt.title("학생별 수학 점수의 표준 점수(Z-score)", fontsize=16)

# 범례 추가
plt.legend()

# 그래프 여백 조정
plt.tight_layout()

# 그래프 출력
plt.show()
