import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# パラメータ設定
cycles = 3  # 周期の数
samples_per_cycle = 100  # 1周期あたりのサンプル数
total_samples = cycles * samples_per_cycle

# データ生成
x = np.linspace(0, 2 * np.pi * cycles, total_samples)
y = np.sin(x-2)

# 軸および枠線を表示し、背景を透明にして再レンダリング
plt.figure(figsize=(16, 4))
plt.plot(x, y, color='blue', lw=5)


# 軸の設定：目盛りは非表示にするが枠線は表示
plt.xticks([])  # 目盛を非表示
plt.yticks([])

ax = plt.gca()
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_position('center')

# 枠線の色や太さを調整（任意）
for spine in ax.spines.values():
    spine.set_linewidth(1)
    spine.set_color('black')

plt.tight_layout(pad=0)
plt.savefig('sin_wave.png', transparent=True)
plt.close()
