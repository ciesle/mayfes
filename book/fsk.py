#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# パラメータ設定
fs = 10000        # サンプリング周波数（10kHz）
bit_rate = 100    # ビットレート（100bps）
Tb = 1 / bit_rate
samples_per_bit = int(fs * Tb)

# 搬送波の周波数（0と1で異なる）
f0 = 50  # 0 のときの周波数
f1 = 200  # 1 のときの周波数

# ランダムビット列を生成
num_bits = 10
data = np.random.randint(0, 3, num_bits)

# 全体の時間軸
t = np.linspace(0, num_bits * Tb, num_bits * samples_per_bit)

# FSK信号生成
fsk_signal = np.zeros_like(t)

for i, bit in enumerate(data):
    t_bit = t[i * samples_per_bit : (i + 1) * samples_per_bit]
    freq = f1 if bit == 1 else f0
    fsk_signal[i * samples_per_bit : (i + 1) * samples_per_bit] = np.cos(2 * np.pi * freq * t_bit)

# グラフ描画
plt.figure(figsize=(12, 6))
plt.plot(t, fsk_signal, color='black')
plt.xlabel('時間 [s]')
plt.ylabel('振幅 [V]')
plt.grid(True)
plt.tight_layout()
plt.show()