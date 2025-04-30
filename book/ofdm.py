#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# パラメータ
num_carriers = 5          # サブキャリア数（5本）
symbol_duration = 1       # シンボル期間（任意単位）
t = np.linspace(-5, 5, 1000)

# 線種と太さの設定（白黒でも区別しやすく）
linestyles = ['-', '--', '-.', ':', (0, (3, 1, 1, 1))]  # 最後はカスタム破線
linewidths = [1.5, 1.2, 1.5, 1.2, 1.5]

# 描画
plt.figure(figsize=(12, 6))
for idx, n in enumerate(range(-num_carriers // 2, num_carriers // 2 + 1)):
    style = linestyles[idx % len(linestyles)]
    width = linewidths[idx % len(linewidths)]
    carrier = np.sinc(t - n)
    plt.plot(t, carrier, linestyle=style, linewidth=width, label=f'Carrier {n}', color='black')

# グラフ設定
plt.xlabel('周波数 [Hz]')
plt.ylabel('振幅 [V]')
plt.grid(True)
plt.tight_layout()
plt.show()