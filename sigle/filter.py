from PIL import Image, ImageFilter 
im = Image.open('00000_00000.ppm')
blurImage = im.filter(ImageFilter.BLUR) 
blurImage.save('python-blur.png')