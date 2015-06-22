import numpy as np
from scipy import signal
import scipy.io.wavfile as wavfile


D = 500

f, data = wavfile.read('sp04.wav')
t = np.arange(0, len(data) / f, 1 / f)


echoes = np.concatenate((data[:D], data[D:] + 0.5 * data[:-D]))
wavfile.write('echoes.wav', f, echoes)

num = np.zeros(1)
num[0] = 1.0
den = np.zeros(D + 1)
den[0] = 1.0

for a in [0.5, 0.9, 0.25]:
    den[-1] = -a

    tf = (num, den, 1 / f)
    _, y = signal.dlsim(tf, echoes, t=t)
    wavfile.write('q2_minus_{0:.2f}.wav'.format(a), f, y)

for a in [0.5, 0.9, 0.25]:
    den[-1] = a

    tf = (num, den, 1 / f)
    _, y = signal.dlsim(tf, echoes, t=t)
    wavfile.write('q2_plus_{0:.2f}.wav'.format(a), f, y)
