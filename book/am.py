#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# パラメータ設定
fs = 100000  # サンプリング周波数（100kHz）
duration = 0.01  # 表示時間（20ms）
t = np.linspace(0, duration, int(fs * duration))

fc = 3000  # 搬送波周波数を遅く（3kHz）
M = 0.7    # 変調指数

# よりリアルな音声信号（複数の周波数とゆらぎを混ぜる）
fm1 = 500
fm2 = 700
fm3 = 1200
noise = 0.05 * np.random.randn(len(t))  # 微小ノイズ

modulating = (
    1 + M * (
        0.6 * np.cos(2 * np.pi * fm1 * t) +
        0.3 * np.sin(2 * np.pi * fm2 * t + np.pi/4) +
        0.2 * np.cos(2 * np.pi * fm3 * t + np.pi/3)
    )
)

# 搬送波とAM信号
carrier = np.cos(2 * np.pi * fc * t)
am_signal = modulating * carrier

# 包絡線
envelope_upper = modulating
envelope_lower = -modulating

# グラフ描画
plt.figure(figsize=(12, 6))
plt.plot(t, am_signal, label='AM信号', color='black')
plt.plot(t, envelope_upper, '--', label='包絡線', color='black')
plt.xlabel('時間 [s]')
plt.ylabel('振幅 [V]')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()