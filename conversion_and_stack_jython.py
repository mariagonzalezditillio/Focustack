import os
from ij import IJ, ImagePlus, ImageStack
from ij.process import ImageConverter
from ij.io import FileSaver
from ij.gui import GenericDialog

IMAGE_WIDTH = 1600
IMAGE_LENGTH = 1200
stack = ImageStack(IMAGE_WIDTH, IMAGE_LENGTH)

def process(srcDir, dstDir, currentDir, fileName):
	print "Processing:"
	# Opening the image
	print "Open image file", fileName
	imp = IJ.openImage(os.path.join(currentDir, fileName))
	if not os.path.exists(dstDir):
		os.mkdir(dstDir)
	# Make image 8 bits
	print "Make image 8 bits", fileName
	ic = ImageConverter(imp)
	ic.convertToGray8()
	imp.updateAndDraw()
	print "Saving to", dstDir
	IJ.saveAs(imp, "Tiff", os.path.join(dstDir, fileName))
	# Stack 
	print "Stack", fileName 
	stack.addSlice(imp.title, imp.getProcessor())
	imp.close()

def main():
	srcDir = IJ.getDirectory("Source Folder")
	if not srcDir:
		return
		
	dstDir = IJ.getDirectory("Destination Folder")
	if not dstDir:
		return
	
	for root, directories, filenames in os.walk(srcDir):
		for filename in filenames:
	  		process(srcDir, dstDir, root, filename)
	  
	ip = ImagePlus("stack", stack).show()

main()
