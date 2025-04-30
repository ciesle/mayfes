import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# パラメータの設定
A = 1
f1 = 0
f2 = 10

# 周波数軸の定義
f = np.linspace(-50, 50, 1000)

# sinc関数の計算
y = (A / (2 * f2)) * np.sinc((f - f1) / (2 * f2))

# グラフの描画
plt.figure(figsize=(10, 4))
plt.plot(f, y, label=r'$\frac{A}{2f_2} \mathrm{sinc}\left(\frac{f-f_1}{2f_2}\right)$', color='black')
plt.axhline(0, color='gray', linewidth=1.5, linestyle='--')  # 実数軸（横軸）を追加
plt.xlabel('周波数 [Hz]')
plt.ylabel('振幅 [V]')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()