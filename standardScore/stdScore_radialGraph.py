#%%   방사형 그래프
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import zscore

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus']=False


# 과목별 점수
subjects = ["국어", "수학", "영어", "과학", "사회"]
scores = [85, 90, 70, 95, 80]

# 표준 점수 계산 (z-score)
z_scores = zscore(scores)

# 방사형 차트를 위한 데이터 준비
num_vars = len(subjects)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# 표준 점수에 대해 원형 차트를 만들기 위해 시작점 다시 추가
z_scores = z_scores.tolist()
z_scores += z_scores[:1]  # 첫 번째 점수를 마지막에 다시 추가하여 원형이 되도록 함
angles += angles[:1]  # 첫 번째 각도를 마지막에 다시 추가하여 원형이 되도록 함

# 그래프 그리기
fig, ax = plt.subplots(figsize=(6, 6), dpi=80, subplot_kw=dict(polar=True))

# 방사형 그래프 그리기
ax.plot(angles, z_scores, color='blue', linewidth=2, linestyle='solid')
ax.fill(angles, z_scores, color='skyblue', alpha=0.4)

# 라벨 설정
ax.set_xticks(angles[:-1])
ax.set_xticklabels(subjects)

# 표준 점수 눈금 설정
ax.set_title("학생의 과목별 표준 점수 (Z-score)", size=15)
ax.set_yticklabels(["-2", "-1", "0", "1", "2"])  # y축 표준점수 눈금 설정

# 그래프 레이아웃 조정
plt.tight_layout()
plt.show()
