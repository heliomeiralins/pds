import numpy as np
from scipy.misc import imsave, imread

dalton = imread('dalton.bmp')

cb = np.copy(dalton)
cb[:, :, 0] = 255 / 2 + (dalton[:, :, 0] - dalton[:, :, 1])
cb[:, :, 1] = 255 / 2 + (dalton[:, :, 1] - dalton[:, :, 0])

imsave('color_blind.bmp', cb)

cb[:, :, 2] = 0

imsave('no_blue.bmp', cb)
