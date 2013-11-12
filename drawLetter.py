import PIL
from PIL import ImageFont, Image, ImageDraw

font = ImageFont.truetype("font.ttf", 11)

for text in range(ord('a'), ord('z')+1):
	img = Image.new("RGB", (10, 10), (255, 255, 255))
	draw = ImageDraw.Draw(img)
	if chr(text) == 'm' or chr(text) == 'w':
		draw.text((0, -3), chr(text), font=font, fill="#000000")
	elif chr(text) == 'g' or chr(text) == 'p' or chr(text) == 'q' or  chr(text) == 'y':
		draw.text((2, -5), chr(text), font=font, fill="#000000") 
	elif chr(text) == 'i' or chr(text) == 'j' or chr(text) == 'f' or chr(text) == 't' or chr(text) == 'r' or chr(text) == 'l':
		draw.text((3, -3), chr(text), font=font, fill="#000000")
	else:
		draw.text((2, -3), chr(text), font=font, fill="#000000")
	img.save("letter/" + chr(text) + ".png")
for text in range(ord('A'), ord('Z')+1):
	img = Image.new("RGB", (10, 10), (255, 255, 255))
	draw = ImageDraw.Draw(img)
	if chr(text) == 'M' or chr(text) == 'W':
		draw.text((-0.8, -3), chr(text), font=font, fill="#000000")
	elif chr(text) == 'I' or chr(text) == 'J':
		draw.text((3, -3), chr(text), font=font, fill="#000000")
	else:
		draw.text((1, -3), chr(text), font=font, fill="#000000")
	img.save("letter/" + chr(text) + ".png")

img = Image.new("RGB", (10, 10), (255, 255, 255))
draw = ImageDraw.Draw(img)
img.save("letter/space.png")


