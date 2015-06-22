import numpy as np
from scipy.misc import imread, imsave
from scipy import ndimage

img = imread('doc1.bmp')


def f(x):
    ret = x * 255 / 150
    if ret > 255:
        ret = 255
    return ret

F = np.vectorize(f)

treated_img = F(img)

imsave('treated_doc.bmp', treated_img)

mask = treated_img < treated_img.mean()

label_im, nb_labels = ndimage.label(mask)
sizes = ndimage.sum(mask, label_im, range(nb_labels + 1))

print(nb_labels)
print(sum(sizes > 1))
print(sum(sizes > 2))
print(sum(sizes > 5))
print(sum(sizes > 10))
