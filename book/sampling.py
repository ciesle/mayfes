import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# 元の信号の設定
fs = 10  # サンプリング周波数 [Hz]
f_signal = 8  # 元の信号の周波数 [Hz]
f_alias = abs(f_signal - fs)  # エイリアス周波数（= 2 Hz）

# 時間軸の作成
t_cont = np.linspace(0, 1, 1000)  # 連続時間軸（1秒間）
t_sampled = np.arange(0, 1, 1/fs)  # サンプリング点

# 信号生成
signal_true = np.sin(2 * np.pi * f_signal * t_cont)
signal_alias = -np.sin(2 * np.pi * f_alias * t_cont)
samples = np.sin(2 * np.pi * f_signal * t_sampled)

# グラフ描画
plt.figure(figsize=(10, 5))
plt.plot(t_cont, signal_true, label='8Hzの信号', color='black')
plt.plot(t_cont, signal_alias, label='2Hzの信号', color='black', alpha=0.4, linestyle='--')
plt.scatter(t_sampled, samples,color='black', label='10Hzのサンプリング')

plt.xlabel('時間 [s]')
plt.ylabel('振幅 [V]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()