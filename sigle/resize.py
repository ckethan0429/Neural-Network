from PIL import Image # 이미지 열기 


im = Image.open('00000_00000.ppm') 

#크기를 600*600으로
img2 = im.resize((600,600))
img2.save('python-600.jpg')

#90도 회전
img3 = im.rotate(90)
img3.save('python-rotate.jpg')