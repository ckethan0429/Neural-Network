from PIL import Image
import numpy as np
import os


im = Image.open('google.jpg')

#image------> numpy array
im2array = np.array(im)
print(im2array)

#numpy array --> image
arr2im = Image.fromarray(im2array)
print(im2array)