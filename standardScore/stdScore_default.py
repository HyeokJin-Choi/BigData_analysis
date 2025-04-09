#%% 표준점수
import numpy as np
from scipy import stats

data = [55, 60, 65, 70, 75]

# 평균과 표준편차 계산
mean = np.mean(data)
std = np.std(data)

# 각 값의 Z-점수 계산 (수동으로)
z_scores = [(d - mean) / std for d in data]
print("Manual Z-scores:", z_scores)

# 또는 scipy 사용하여 Z-점수 계산
z_scores_scipy = stats.zscore(data)
print("Scipy Z-scores:", z_scores_scipy)
