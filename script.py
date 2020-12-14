from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from pathlib import Path

names_file = open("assets/names-list")  # The file with the list of names, one on each line
names_list = names_file.read()
names_array = names_list.splitlines()
count = 1

for name in names_array:
    img = Image.open("assets/sample-certificate.jpg")  # The image file
    draw = ImageDraw.Draw(img)
    img_h, img_w = img.size  # Calculate image dimensions

    (x, y) = (0, 410)  # Initial coordinates
    msg = "{0}".format(name)  # Greeting message
    color = 'rgb(0,0,0)'
    font = ImageFont.truetype(r'assets/DancingScript-Regular.ttf', 72)
    text_h, text_w = font.getsize(msg)  # Rendered text dimensions
    (x, y) = ((img_h - text_h) / 2, y)  # Final coordinates
    draw.text((x, y), msg, fill=color, font=font)

    Path("./output").mkdir(parents=True, exist_ok=True)
    filename = "output/bday_wish {0}.jpg".format(count)
    img.save(filename)
    count += 1
