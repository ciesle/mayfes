import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
fs = 1000  # サンプリング周波数
f = 1      # 周波数（1Hz）
T = 5      # 5周期表示
t = np.linspace(0, T, int(fs * T))
y = np.sin(2 * np.pi * f * t)

# 窓関数（ハン窓）を適用して、最初と最後をすぼませる
window = np.hanning(len(t))
y_windowed = y * window

# 背景透過で線の太さを大きくしてプロット
plt.figure(figsize=(10, 3), dpi=300)
plt.plot(t, y_windowed, color='black', linewidth=12)
plt.axis('off')
plt.tight_layout()
plt.savefig('sin.png', transparent=True)
plt.close()