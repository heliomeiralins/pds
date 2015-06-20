from scipy.misc import imread, imsave
from scipy.ndimage.filters import gaussian_filter

rings = imread('lena_rings.bmp')

imsave('gaussian.bmp', gaussian_filter(rings, 1.5))
