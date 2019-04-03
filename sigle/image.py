from PIL import Image # 이미지 열기 
import urllib.request as request

url='https://dbscthumb-phinf.pstatic.net/2315_000_1/20150907163946401_K0Q0LCOAE.jpg/n1676.jpg?type=m250&wm=N'

res = request.urlopen(url)

im = Image.open(res).convert("L") # 이미지 크기 출력 ,response객체도 가능
print(im.size) # 이미지 JPG로 저장 
im.save('google.jpg') # 이미지 화면 출력 im.show()