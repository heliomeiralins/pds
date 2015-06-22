import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
from scipy.signal import kaiserord, firwin, lfilter
import scipy.io.wavfile as wavfile

FREQ = 466.16

fs, data = wavfile.read('teste_de_som.wav')
print("Taxa de amostragem: {} Hz".format(fs))
t = np.arange(0, len(data) / fs, 1 / fs)

new = 30 * data.astype('float64') + 10000 * np.sin(2 * np.pi * FREQ * t)

O = fftpack.fft(data) / len(t)
N = fftpack.fft(new) / len(t)
f = fftpack.fftfreq(len(t), d=1 / fs)

plt.subplot(2, 1, 1)
plt.plot(t, data)
plt.xlabel('time')
plt.ylabel('original')

plt.subplot(2, 1, 2)
plt.plot(t, new)
plt.xlabel('time')
plt.ylabel('new')

plt.show()

plt.subplot(2, 1, 1)
plt.plot(f, np.abs(O))
plt.xlabel('freq')
plt.ylabel('original')

plt.subplot(2, 1, 2)
plt.plot(f, np.abs(N))
plt.xlabel('freq')
plt.ylabel('new')

plt.show()
wavfile.write('noisy.wav', 8000, new)

REC = N
df = fs / len(REC)

wavfile.write('fft_normalized.wav', 8000, np.abs(fftpack.ifft(REC)))

REC[np.where(np.abs(466.16 - f) < 30)] = 0

wavfile.write('fft_treated.wav', 8000, np.abs(fftpack.ifft(REC)))


# FIR FILTER - KAISER
nyq = fs / 2
width = 1 / fs
ripple_db = 11

numtaps, beta = kaiserord(ripple_db, width)


fir = firwin(
    numtaps, [(FREQ - 30) / nyq, (FREQ + 30) / nyq], window=('kaiser', beta))
fir_response = lfilter(fir/10000, 1, new)

wavfile.write('fir_filter.wav', 8000, fir_response)
