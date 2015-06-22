import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
import scipy.io.wavfile as wavfile

f_original, data_original = wavfile.read('or105.wav')
f, data = wavfile.read('dg105.wav')

assert(f == f_original)
t = np.arange(0, len(data) / f, 1 / f)

plt.subplot(2, 1, 1)
plt.plot(t, data_original)
plt.xlabel('time')
plt.ylabel('or105')

plt.subplot(2, 1, 2)
plt.plot(t, data)
plt.xlabel('time')
plt.ylabel('dg105')

plt.show()

OR = fftpack.fft(data_original)[0: len(t) / 2] / len(t)
DG = fftpack.fft(data)[0: len(t) / 2] / len(t)
f = fftpack.fftfreq(len(t), d=1 / f)[0:len(t) / 2]

plt.subplot(2, 1, 1)
plt.plot(f, np.abs(OR))
plt.xlabel('freq')
plt.ylabel('OR')

plt.subplot(2, 1, 2)
plt.plot(f, np.abs(DG))
plt.xlabel('freq')
plt.ylabel('DG')

plt.show()
