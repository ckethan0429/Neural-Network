from PIL import Image # 이미지 열기 


def center_crop(im): 
    crop_size = min(im.size) 
    left = (im.size[0] - crop_size)//2 
    top = (im.size[1] - crop_size)//2 
    right = (im.size[0] + crop_size)//2 
    bottom = (im.size[1] + crop_size)//2 

    return im.crop((left, top, right, bottom))

im = Image.open('00000_00000.ppm') 
cropImage = center_crop(im) 
cropImage.save('python-crop.jpg')