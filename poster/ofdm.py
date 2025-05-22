import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# パラメータ
num_sincs = 5                 # 配置する sinc 関数の数
spacing = 1                  # OFDMでの直交条件に基づく間隔
bandwidth = 3 / spacing

x = np.linspace(-10, 10, 5000)  # 時間軸

# sinc関数の中心位置（左右対称配置）
centers = np.linspace(-2, 2, num_sincs)

# カラーマップ（青系）から色を取得
colors = cm.Blues(np.linspace(0.4, 0.9, num_sincs))  # 明るすぎず濃すぎない範囲

# グラフ描画
plt.figure(figsize=(10, 4))

# 各 sinc 関数を青のバリエーションで描画
for c, color in zip(centers, colors):
    plt.plot(x, np.sinc((x - c) / spacing), linewidth=3, color=color)

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

# PNG保存
plt.tight_layout()
plt.savefig("ofdm_array.png", dpi=300, bbox_inches='tight', transparent=True)
plt.close()
