from makeDis import makeDictionary
from PIL import Image, ImageDraw

def resizeImg(imgPath):
	img = Image.open(imgPath)
	_img = img.convert('RGB')
	width = _img.size[0]
	height = _img.size[1]
	out = img.resize((500, 500*height / width))
	return out

def match(gs):
	fin = 255
	matched = ''
	for img in Dict.keys():
		if fin > abs(gs - Dict[img]):
			fin = abs(gs - Dict[img])
			matched = img
	return matched

box = (0, 0, 10, 10)

Dir = '/home/yeqin/workspace/picToAscii/letter'
makeDict = makeDictionary(Dir)
Dict = makeDict.makeDict()
imgPath = raw_input('Please input the name of the image: ')
img = resizeImg(imgPath)
img.save('img.png')
height = img.size[1]
width = img.size[0]
output = Image.new('RGB', (10*width, 10*height), (255, 255, 255))
for h in range(0, height):
	for w in range(0, width):
		r, g, b = img.getpixel((w, h))
		region = Image.open('letter/'+match((r+g+b)/3))
		output.paste(region, (w*10, h*10))
output.show()
output.save("output_"+imgPath, "JPEG")


