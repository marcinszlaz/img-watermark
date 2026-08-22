from PIL import Image, ImageOps
from pdf2image import convert_from_path
import os, sys
import time


ps_file = convert_from_path("watermark.ps")
print(ps_file)
# im = Image.open('image.png') # it has .save() function too
# print(im.size, im.format, im.mode)
#
# def wsec(how_much_the_fish: int = 1):
#   time.sleep(how_much_the_fish)
#
# def convert_img():
#   for image in sys.argv[1:]: # sys.argv[0] is usual script name
#     path, file = os.path.split(image) # split to path and filename
#     print(path, file)
#     outfile = file + ".jpg"
#     if image != outfile:
#       try:
#         with Image.open(image) as im:
#           im.save(outfile)
#           # save() function have second `format` parameter sets desired extension
#       except OSError:
#         print("cannot convert", image)
# how_to = os.path.splitext(__file__) # splits path+file || file_extension (./app | .py)
#
# def about_image():
#   for infile in sys.argv[1:]:
#     try:
#       with Image.open(infile) as im:
#         print(infile, im.format, f"{im.size}x{im.mode}")
#     except OSError:
#       pass
# # convert_img()
# about_image()
#
# # cutting from image
# box = (0, 0, 568, 250)
# region = im.crop(box) # crop() takes tuple with lef upper, right lower
#                       # corners coordinates
# # region.show()
# # rotating cutted pice of image
# region = region.transpose(Image.Transpose.ROTATE_180)
# im.paste(region, box)
# # im.show()
#
# def roll(im: Image.Image, delta: int) -> Image.Image:
#   """Roll an image sideways."""
#   xsize, ysize = im.size
#
#   delta = delta % xsize
#   if delta == 0:
#     return im
#
#   part1 = im.crop((0, 0, delta, ysize))
#   part2 = im.crop((delta, 0, xsize, ysize))
#   im.paste(part1, (xsize - delta, 0, xsize, ysize))
#   im.paste(part2, (0, 0, xsize - delta, ysize))
#   return im.show()
#
# # roll(im=im, delta=200)
#
# r, g, b = im.split() # splits image to color bands (r,g,b)
# # g.show()
# out = im.resize((128,128))
# # out.show()
# wsec(1)
# out = im.rotate(45)
# # out.show()
# wsec(1)
# out = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# # out.show()
# wsec(1)
# out = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# # out.show()
# wsec(1)
#
# # from PIL import Image, ImageOps
# def modifications():
#   size = (100, 150)
#   with Image.open("image_1.png") as im:
#       ImageOps.contain(im, size).save("imageops_contain.png")
#       ImageOps.cover(im, size).save("imageops_cover.png")
#       ImageOps.fit(im, size).save("imageops_fit.png")
#       ImageOps.pad(im, size, color="#f00").save("imageops_pad.png")
#
#       # thumbnail() can also be used,
#       # but will modify the image object in place
#       im.thumbnail(size)
#       im.save("image_thumbnail.png")
# # modifications()
# print(im.getbands())
#
# from PIL import ImageDraw, ImageFont
#
# # font = ImageFont.truetype(48)
# im = Image.new("RGB", (200, 200), "white")
# d = ImageDraw.Draw(im)
# d.line(((0, 100), (200, 100)), "gray")
# d.line(((100, 0), (100, 200)), "gray")
# d.text((100, 100), "Quick", fill="black", anchor="ms")
# # im.show()
