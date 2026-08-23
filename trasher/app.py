import os, sys, math
from PIL import Image, ImageOps, ImageDraw, ImageFont


c, width, height, format_, im = None, None, None, None, None
print(f"Welcome!\n"
      f"Program takes one argument (after script name).\n"
      f"Argument has to be image file.\n"
      f"Program adding watermark to it.")

if len(sys.argv[:]) == 1:
  print(f"Input one image filename after {sys.argv[0]}")
elif len(sys.argv[:]) > 2:
  print("Input only one image filename please")
elif len(sys.argv[:]) == 2:
  im = Image.open(sys.argv[1]).convert("RGBA")
  print(f"Image size/format/mode: {im.size}/{im.format}/{im.mode}")
  width, height = im.size
  _format = im.format
  c = math.sqrt(pow(width,2) + pow(height,2)) * 0.66

txt = Image.new(mode="RGBA", size=(width, height), color=(255,255,255,0))
font = ImageFont.truetype("./STENCIL.TTF", size=45)
draw = ImageDraw.Draw(txt)
text = "! W A T E R M A R K E D !"
draw.text(xy=(width*0.5, height*0.5),text=text, fill=(255,0,0,64), font=font, anchor="mm", stroke_width=3, spacing=0, stroke_fill="black")
out = Image.alpha_composite(im, txt.rotate(angle=-45, expand=False))
out.show()
im.close()