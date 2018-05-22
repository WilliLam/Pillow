from PIL import Image
from PIL import ImageFilter
img = Image.open("img2.jpg")

blur = img.filter(ImageFilter.BLUR)
detail = img.filter(ImageFilter.DETAIL)
edges = img.filter(ImageFilter.FIND_EDGES)
blur.show()
detail.show()
edges.show()