import os
from PIL import Image

def center_crop(im): 
    crop_size = min(im.size) 
    left = (im.size[0] - crop_size)//2 
    top = (im.size[1] - crop_size)//2 
    right = (im.size[0] + crop_size)//2 
    bottom = (im.size[1] + crop_size)//2 

    return im.crop((left, top, right, bottom))

#파일 추출
list = os.listdir('./GTSRB/Final_Training/Images/00000')
for item in list:
    filename, fileExtension = os.path.splitext(item)
    print('파일명 : ' + filename + ' 확장자명 : ' + fileExtension)
    
    im = Image.open('./'+item).convert("L")
    cropImage = center_crop(im)
    resized_image = cropImage.resize((32,32))
    
    resized_image.save('./GTS/'+filename+'.jpg')
    