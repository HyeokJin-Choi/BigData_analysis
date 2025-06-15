import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# ──────────────────────────────────────────────
# 1) 데이터 로드
# ──────────────────────────────────────────────
df = pd.read_csv(r"C:\Users\samsung\Desktop\BigData_analysis\dfdata\prestige.csv")

# ──────────────────────────────────────────────
# 2) 필요한 네 개 컬럼 추출
# ──────────────────────────────────────────────
df_new = df[['education', 'income', 'women', 'prestige']].copy()

# ──────────────────────────────────────────────
# 3) Min-Max 정규화
# ──────────────────────────────────────────────
def min_max_scaling(series):
    return (series - series.min()) / (series.max() - series.min())

df_scaled = df_new.apply(min_max_scaling)

# ──────────────────────────────────────────────
# 4) 인덱스를 'job' 으로 설정
# ──────────────────────────────────────────────
df_scaled.index = df['job'].str.strip()  # 공백 제거(예방 차원)

# ──────────────────────────────────────────────
# 5) 평균 행('avg') 추가
# ──────────────────────────────────────────────
df_scaled.loc['avg'] = df_scaled.mean()

# ──────────────────────────────────────────────
# 6) 비교할 직업 이름 찾기
#    - 데이터마다 철자가 다를 수 있으므로
#      'computer' 문자열이 들어간 행을 자동 탐색
# ──────────────────────────────────────────────
job_candidates = [idx for idx in df_scaled.index if 'computer' in idx.lower()]
if not job_candidates:
    raise ValueError("데이터에 'computer'가 포함된 직업명이 없습니다.")
job_name = job_candidates[0]   # 첫 번째 후보 사용

# ──────────────────────────────────────────────
# 7) 레이더 차트 준비
# ──────────────────────────────────────────────
labels = df_scaled.columns.tolist()
num_vars = len(labels)

programmer_values = df_scaled.loc[job_name].values
avg_values        = df_scaled.loc['avg'].values

# 레이더 차트를 그리기 위해 각도 계산
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

programmer_values = np.append(programmer_values, programmer_values[0])
avg_values        = np.append(avg_values,        avg_values[0])

# ──────────────────────────────────────────────
# 8) 레이더 차트 그리기
# ──────────────────────────────────────────────
plt.figure(figsize=(8, 6))
ax = plt.subplot(111, polar=True)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], labels, fontsize=10)

# 평균
ax.plot(angles, avg_values, label='Average', color='gray', linewidth=2)
ax.fill(angles, avg_values, color='gray', alpha=0.2)

# 컴퓨터 프로그래머
ax.plot(angles, programmer_values, label=job_name, color='royalblue', linewidth=2)
ax.fill(angles, programmer_values, color='royalblue', alpha=0.3)

# 범례와 타이틀
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
plt.title(f"{job_name} vs 전체 평균 (정규화 비교)", fontsize=14)
plt.tight_layout()
plt.show()
