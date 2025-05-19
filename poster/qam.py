#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# Gray符号（2ビット）を4レベルに対応（-3, -1, 1, 3 に割り当て）
gray_2bit = ['00', '01', '11', '10']  # 2ビットGray符号
amplitudes = [-3, -1, 1, 3]           # 振幅レベル（I, Qとも）

# グリッド点を生成
I = []
Q = []
labels = []

# Q軸は画像で上に行くほどビットが小さくなるので、逆順にする
for q in reversed(range(4)):
    for i in range(4):
        i_val = amplitudes[i]
        q_val = amplitudes[q]
        I.append(i_val)
        Q.append(q_val)
        label = gray_2bit[q] + gray_2bit[i]  # Qが上位ビット, Iが下位ビット
        labels.append(label)

# プロット
plt.figure(figsize=(6, 6))
plt.scatter(I, Q, color='black', edgecolors='black')
for i in range(len(I)):
    plt.text(I[i] + 0.15, Q[i] + 0.15, labels[i], fontsize=9)

plt.xlabel('I 軸 (sin波)')
plt.ylabel('Q 軸 (cos波)')
plt.grid(True)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.gca().set_aspect('equal')
plt.tight_layout()
plt.savefig('qam.png')