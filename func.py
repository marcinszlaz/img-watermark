from PIL import Image, ImageDraw, ImageFont
import sys, os, pathlib
TEXT = "! W A T E R M R K E D !"

def watermark_it(image: str = None, text: str = TEXT):
  with Image.open(image, 'r').convert("RGBA") as im:
    width, height = im.size
    txt = Image.new(mode="RGBA", size=(width, height), color=(255, 255, 255, 0))
    font = ImageFont.truetype("./font/STENCIL.TTF", size=45)
    draw = ImageDraw.Draw(txt)
    draw.text(xy=(width * 0.5, height * 0.5), text=text, fill=(255, 0, 0, 64), font=font, anchor="mm",
              stroke_width=3, spacing=0, stroke_fill="black")
    out = Image.alpha_composite(im, txt.rotate(angle=-45, expand=False))
    fp = pathlib.Path(image)
    directory, file, ext = fp.parent, fp.stem, fp.suffix
    path = directory / f"{file + '_marked' + ext}"  # overloaded `\` operator concatenate path-strings
    out.save(path)
    print(f"File saved \u2705")

if __name__ == "__main__":
  watermark_it()