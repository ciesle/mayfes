import matplotlib.pyplot as plt
import numpy as np

# ホワイトノイズを生成
np.random.seed(0)
samples = 1000
noise = np.random.normal(0, 1, samples)

# グラフを描画
plt.figure(figsize=(10, 4))
plt.plot(noise)
# 軸の設定：目盛りは非表示にするが枠線は表示
plt.xticks([])  # 目盛を非表示
plt.yticks([])

# 軸のカスタマイズ
ax = plt.gca()
ax.spines['left'].set_position('zero')     # 左端に縦軸
ax.spines['bottom'].set_position('center') # 中央に横軸
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.tight_layout()



# グラフを表示
plt.savefig('noise.png')
