from PIL import Image
img2 = Image.open("img2.jpg")
img3 = Image.open("img3.jpg")
img4 = img2.crop((150,60,650,341))
img4.show()
print(img2.mode)
print(img3.mode)
r,g,b = img4.split()
r1,g1,b1 = img3.split()
n_img = Image.merge('RGB', (r,g,b1))

n_img.show()