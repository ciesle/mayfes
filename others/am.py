import numpy as np
import matplotlib.pyplot as plt

import japanize_matplotlib

# パラメータ設定
carrier_freq = 8000      # キャリア周波数 100kHz
modulating_freq = 1000     # 変調信号周波数 1kHz
modulation_index = 0.5    # 変調指数
sampling_rate = 1e6       # サンプリング周波数

duration = 0.002          # 信号の継続時間（秒）
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# 変調信号（メッセージ信号）
modulating_signal = np.sin(2 * np.pi * modulating_freq * t)

# AM信号（振幅変調）
am_signal = (1 + modulation_index * modulating_signal) * np.cos(2 * np.pi * carrier_freq * t)
am_signal = np.clip(am_signal, 0, None)

# プロットして保存
plt.figure(figsize=(16, 4))
plt.plot(t, am_signal, linewidth=5)

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
plt.savefig("am_signal.png", dpi=300, bbox_inches='tight', pad_inches=0,  transparent=True)
plt.close()