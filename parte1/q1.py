"""Resolução da primeira questão"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

dt = 0.01
fs = 1 / dt

t = np.arange(0, 10, dt)
tw = np.arange(0, 20, dt)
N = len(t)

y = np.sin(20 * np.pi * t) + np.cos(30 * np.pi * t)
z = np.sin(40 * np.pi * t) + np.cos(60 * np.pi * t)
w = np.concatenate((y, z))

# Calculo de ffts
Y = fftpack.fft(y)[0:N / 2] / N
Z = fftpack.fft(z)[0:N / 2] / N
W = fftpack.fft(w)[0:N] / (2 * N)
f_space = fftpack.fftfreq(N, d=dt)[0:N / 2]
f_spaceW = fftpack.fftfreq(2 * N, d=dt)[0: N]


def print_function_and_fft(x, X, t, f, label):
    plt.subplot(3, 1, 1)  # plot function
    plt.plot(t, x)
    plt.xlabel('time')
    plt.ylabel(label.lower())

    plt.subplot(3, 1, 2)  # plot fft amplitude
    plt.plot(f, np.abs(X))
    plt.xlabel('freq (Hz)')
    plt.ylabel('{} amplitude'.format(label.upper()))

    plt.subplot(3, 1, 3)  # plot fft phase
    plt.plot(f, np.angle(X))
    plt.xlabel('freq(Hz)')
    plt.ylabel('{} phase (rad)'.format(label.upper()))

    plt.show()

print_function_and_fft(y, Y, t, f_space, 'y')
print_function_and_fft(z, Z, t, f_space, 'z')
print_function_and_fft(w, W, tw, f_spaceW, 'w')
