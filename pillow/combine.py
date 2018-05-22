from PIL import Image
img1 = Image.open("kimi-no-na-wa-scenery-buildings-clouds-sky-grass.png")
img2 = Image.open("img2.jpg")

area = (100,100,750,441)
img1.paste(img2, area)

img1.show()

