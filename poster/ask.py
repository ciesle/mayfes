import numpy as np
import matplotlib.pyplot as plt

import japanize_matplotlib

# パラメータ設定
carrier_freq = 4000      # キャリア周波数 100kHz
sampling_rate = 1e6       # サンプリング周波数
bit_rate = 1000           # ビットレート（1kbps）
duration = 0.01           # 信号の継続時間（秒）

# 時間軸生成
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# ランダムビット列の生成
num_bits = int(duration * bit_rate)
bits = np.random.randint(1, 5, num_bits)

# ビット列をサンプリングレートに合わせて拡張
bit_signal = np.repeat(bits, int(sampling_rate / bit_rate))
bit_signal = bit_signal[:len(t)]  # 長さを調整

# ASK信号の生成
carrier = np.cos(2 * np.pi * carrier_freq * t)
ask_signal = bit_signal * carrier

# プロットして保存
plt.figure(figsize=(16, 4))
plt.plot(t, ask_signal, linewidth=5, color='navy')

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
plt.savefig("ask_signal.png", dpi=300, bbox_inches='tight', pad_inches=0,  transparent=True)
plt.close()