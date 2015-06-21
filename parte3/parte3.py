from scipy.misc import imread, imsave

img101 = imread('frames/saida_101.bmp')
img103 = imread('frames/saida_103.bmp')

img109 = imread('frames/saida_109.bmp')
img111 = imread('frames/saida_111.bmp')

img117 = imread('frames/saida_117.bmp')
img119 = imread('frames/saida_119.bmp')

imsave('inter_102.bmp', img101 / 2 + img103 / 2)
imsave('inter_110.bmp', img109 / 2 + img111 / 2)
imsave('inter_118.bmp', img117 / 2 + img119 / 2)
