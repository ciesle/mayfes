import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# パラメータ
fs = 1000  # サンプリング周波数 [Hz]
duration = 1.0  # 信号長 [秒]（5Hzが5周期）
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# 信号の生成（5Hz, 7Hz, 10Hzの加算）
signal = (
    np.sin(2 * np.pi * 5 * t) +
    np.sin(2 * np.pi * 7 * t) +
    np.sin(2 * np.pi * 10 * t)
)

# フーリエ変換
fft_result = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(t), 1/fs)

# 正の周波数成分のみを抽出
positive_freqs = freqs[:len(freqs)//2]
magnitude = np.abs(fft_result[:len(freqs)//2])

# 描画
plt.figure(figsize=(12, 6))

# 時間領域の信号
plt.subplot(2, 1, 1)
plt.plot(t, signal, color='black', linewidth=2)
plt.title("時間領域")
plt.xlabel("時間 [s]")
plt.ylabel("振幅 [V]")
plt.grid(True)

# 周波数領域（フーリエ変換）
plt.subplot(2, 1, 2)
plt.stem(positive_freqs, magnitude, linefmt='k-', markerfmt='ko', basefmt='k-')
plt.title("周波数領域")
plt.xlabel("周波数 [Hz]")
plt.ylabel("振幅スペクトル")
plt.xlim(0, 20)
plt.grid(True)

plt.tight_layout()
plt.show()