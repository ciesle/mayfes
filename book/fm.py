#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# パラメータ
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

# グラフ描画
plt.figure(figsize=(12, 5))
plt.plot(t, fm_signal, label='FM信号', color='black')

plt.xlabel('時間 [s]')
plt.ylabel('振幅 [V]')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()