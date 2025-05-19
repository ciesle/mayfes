import numpy as np
import matplotlib.pyplot as plt

import japanize_matplotlib

fs = 10000  # サンプリング周波数（10kHz）
duration = 0.1  # 表示時間 0〜0.1秒（100ms）
t = np.linspace(0, duration, int(fs * duration))

fc = 100    # 搬送波周波数（1kHz）
fm = 20      # 音声信号周波数（20Hz）
delta_f = 50  # 周波数偏移（200Hz）

# 変調指数 β
beta = delta_f / fm

# FM信号生成
modulating_signal = np.sin(2 * np.pi * fm * t)
instantaneous_phase = 2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t)
fm_signal = np.cos(instantaneous_phase)

# プロットして保存
plt.figure(figsize=(16, 4))
plt.plot(t, fm_signal, linewidth=5)

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
plt.savefig("fm_signal.png", dpi=300, bbox_inches='tight', pad_inches=0,  transparent=True)
plt.close()