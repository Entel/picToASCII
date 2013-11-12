# -*- coding: utf-8 -*- 
import os, ImageFilter, Image

class makeDictionary:

	def __init__(self, Dir):
		self.Dir = Dir
	
	def getGrayscale(self, imgPath):
		img = Image.open('letter/' + imgPath)
		sumGs = 0
		_img = img.convert('RGB')
		width = _img.size[0]
		height = _img.size[1]
		# print width, height
		for h in range(0, height):
			for w in range(0, width):
				r, g, b = _img.getpixel((w, h))
				sumGs = (r + g + b) / 3 + sumGs
			#	print sumGs
		aveGs = sumGs / 100
	#	print aveGs
		return aveGs

	def getLettersPath(self):
		for imgPath in os.listdir(self.Dir):
			self.getGrayscale(imgPath)

	def makeDict(self):
		gsDict = {}
		for imgPath in os.listdir(self.Dir):
			gsDict[imgPath] = self.getGrayscale(imgPath)
		return gsDict
	

