from PIL import Image

img = Image.open('kimi-no-na-wa-scenery-buildings-clouds-sky-grass.png')

n_img = img.crop((10 ,10 , 700, 800))
img.show()
n_img.show()