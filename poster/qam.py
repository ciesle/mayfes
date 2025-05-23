#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# Gray符号（2ビット）を4点QAMに対応
gray_2bit = ['00', '01', '11', '10']
amplitudes = [-1, 1]

# グリッド点を生成
I = []
Q = []
labels = []

for q in reversed(range(2)):
    for i in range(2):
        i_val = amplitudes[i]
        q_val = amplitudes[q]
        I.append(i_val)
        Q.append(q_val)
        label = gray_2bit[q * 2 + i]
        labels.append(label)

# プロット
plt.figure(figsize=(6, 6))
plt.scatter(I, Q, color='black', edgecolors='black', s=108)  # 点を3倍に
for i in range(len(I)):
    plt.text(I[i] + 0.1, Q[i] + 0.1, labels[i], fontsize=30)  # 文字サイズを3倍に

# 軸ラベルを消す
plt.xlabel('')
plt.ylabel('')

# グリッドと補助線
plt.grid(True)
plt.axhline(0, color='black', lw=2)  # 軸を太く
plt.axvline(0, color='black', lw=2)  # 軸を太く
plt.xticks(np.arange(-2, 3, 1), fontsize=20)  # 数字を大きく
plt.yticks(np.arange(-2, 3, 1), fontsize=20)  # 数字を大きく
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.gca().set_aspect('equal')
plt.tight_layout()
plt.savefig('4qam_large.png')
