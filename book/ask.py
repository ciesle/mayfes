#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# パラメータ設定
fs = 3000       # サンプリング周波数（3kHz）
bit_rate = 100  # ビットレート（100bps）
fc = 300        # 搬送波周波数（300Hz）

Tb = 1 / bit_rate  # 1ビットの時間
samples_per_bit = int(fs * Tb)

# ランダムなビット列を生成（5ビット）
num_bits = 10
data = np.random.randint(0, 5, num_bits)

# 各ビットをサンプリングに展開
data_upsampled = np.repeat(data, samples_per_bit)

# 時間軸
t = np.linspace(0, num_bits * Tb, num_bits * samples_per_bit)

# 搬送波生成
carrier = np.cos(2 * np.pi * fc * t)

# ASK変調：ビットが1のとき搬送波、0のときは0
ask_signal = data_upsampled * carrier

# グラフ描画
plt.figure(figsize=(10, 4))
plt.plot(t, ask_signal, color='black')
plt.xlabel('時間 [s]')
plt.ylabel('振幅 [V]')
plt.grid(True)
plt.tight_layout()
plt.show()