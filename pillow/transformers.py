from PIL import Image
img = Image.open("img2.jpg")

square_img = img.resize((300,300))
square_img.show()
flip_img = img.transpose(Image.FLIP_TOP_BOTTOM)
flip_img.show()
spin_img = img.transpose(Image.ROTATE_90)
spin_img.show()