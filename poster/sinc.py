import numpy as np
import matplotlib.pyplot as plt

# 描画用パラメータ
num_sincs = 5                 # 配置する sinc 関数の数
spacing = 2.0                 # 各 sinc の中心間距離
x = np.linspace(-10, 10, 5000)  # x軸の範囲と解像度

# 複数の sinc 関数を重ねる
y = np.zeros_like(x)
centers = [-7,0,7]
for c in centers:
    y += np.sinc((x - c) * 4)

# グラフ描画
plt.figure(figsize=(10, 4))
plt.plot(x, y, linewidth=4)

# 軸の設定：目盛りは非表示にするが枠線は表示
plt.xticks([])
plt.yticks([])

# 軸のカスタマイズ
ax = plt.gca()
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

# 画像保存
plt.tight_layout()
plt.savefig("sinc_array.png", dpi=300, bbox_inches='tight', transparent=True)
plt.close()
