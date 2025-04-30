#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import japanize_matplotlib

# フォント設定（IPAexゴシック）
prop = fm.FontProperties(fname='/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf')
plt.rcParams['font.family'] = prop.get_name()

# x軸（2周期分）
x = np.linspace(0, 4 * np.pi, 2000)

# 理想的な矩形波
square_wave = np.where((x % (2 * np.pi)) < np.pi, 1, -1)

# 各段階のフーリエ近似
def fourier_approximation(n_terms, x):
    sum_ = np.zeros_like(x)
    for n in range(1, n_terms + 1):
        k = 2 * n - 1
        sum_ += np.sin(k * x) / k
    return (4 / np.pi) * sum_

# グラフ描画（縦に4つ並べる）
fig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

# 1. 理想的な矩形波
axs[0].plot(x, square_wave, color='black', linewidth=2)
axs[0].set_title('理想的な矩形波')
axs[0].set_ylabel('振幅 [V]')

# 2. 1項までのフーリエ近似
approx1 = fourier_approximation(1, x)
axs[1].plot(x, approx1, color='black', linestyle='--')
axs[1].set_title('フーリエ変換結果（1項まで）')
axs[1].set_ylabel('振幅 [V]')

# 3. 10項までのフーリエ近似
approx10 = fourier_approximation(3, x)
axs[2].plot(x, approx10, color='black', linestyle='-.')
axs[2].set_title('フーリエ変換結果（3項まで）')
axs[2].set_ylabel('振幅 [V]')

# 4. 50項までのフーリエ近似
approx50 = fourier_approximation(50, x)
axs[3].plot(x, approx50, color='black', linestyle=':')
axs[3].set_title('フーリエ変換結果（50項まで）')
axs[3].set_xlabel('時間 [s]')
axs[3].set_ylabel('振幅 [V]')

# グリッド・レイアウト調整
for ax in axs:
    ax.grid(True)

plt.tight_layout()
plt.show()
