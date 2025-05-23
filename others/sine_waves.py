import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# ===== パラメータ設定 =====
amplitudes = [1000, 5000, 9000]  # 各正弦波の振幅
frequency = 1                    # 周波数 [Hz]
duration = 1                     # 表示する時間 [秒]
sampling_rate = 1000             # サンプリング周波数 [samples/sec]

# ===== 時間軸を生成 =====
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# ===== 各振幅の正弦波を生成 =====
waves = [A * np.sin(2 * np.pi * frequency * t) for A in amplitudes]

# ===== プロット設定 =====
plt.figure(figsize=(10, 6))
colors = ['orange', 'green', 'red']
labels = [f'4Hz 大きさ {A}' for A in amplitudes]

for wave, color, label in zip(waves, colors, labels):
    plt.plot(t, wave, label=label, color=color)

frequency=3
# ===== 各振幅の正弦波を生成 =====
waves = [A * np.sin(2 * np.pi * frequency * t) for A in amplitudes]

# ===== プロット設定 =====
colors = ['black', 'pink', 'purple']
labels = [f'12Hz 大きさ {A}' for A in amplitudes]

for wave, color, label in zip(waves, colors, labels):
    plt.plot(t, wave, label=label, color=color)

# 軸のカスタマイズ
ax = plt.gca()
ax.spines['left'].set_position('zero')     # 左端に縦軸
ax.spines['bottom'].set_position('center') # 中央に横軸
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

plt.tick_params(axis='y', labelsize=24)

plt.legend()
plt.tight_layout()
plt.savefig('sine_waves.png', transparent=True)
