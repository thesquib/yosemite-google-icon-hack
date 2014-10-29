#!/usr/bin/env python

"""
Copying and distribution of this file, with or without modification,
are permitted in any medium without royalty provided the copyright
notice and this notice are preserved.  This file is offered as-is,
without any warranty.


The current version of Google Chrome and Google Hangouts is not compatible with the
dark menu bar on Mac OS X Yosemite

This simple script works with the current version of the Google Hangouts extension, and inverts the 
presence images so they are visible in the menu bar. 

To reverse, just run again. 

Assumptions:
Mac OS X Yosemite
Google Chrome with Google Hangouts extension
You know what you are doing (I wrote this for myself)
python is installed with python PIL or Pillow, i.e:
 brew install pillow
"""

import sys
import os
from PIL import Image,ImageOps


supportedPatchLevels = ["2014.910.433.1_0"]
iconFileNames = ["available_19.png", "available_38.png", "available_mac_19.png", 
				"available_mac_38.png", "available_missed_19.png", "available_missed_38.png", 
				"available_missed_mac_19.png", "available_missed_mac_38.png", "offline_19.png", 
				"offline_38.png", "offline_mac_19.png", "offline_mac_38.png", "offline_unknown_19.png", 
				"offline_unknown_38.png", "offline_unknown_mac_19.png", "offline_unknown_mac_38.png", 
				"offline_working_19.png", "offline_working_38.png", "offline_working_mac_19.png", 
				"offline_working_mac_38.png"]
chromePath = "/Library/Application Support/Google/Chrome/Default/Extensions/nckgahadagoaajjgafhacjanaoiihapd/"
imagePath = "images_4/presence"

def patchFolder(folder):
	contents = os.listdir(folder)
	for f in contents:
		if f in iconFileNames:
			print("... converting " + folder+"/"+f)
			invertImage(folder+"/"+f)

def invertImage(filename):
	if filename is None:
		print("Filename is None")
		return None
	if ".png" not in filename:
		print("File is not png")
		return None
	if not os.path.isfile(filename):
		print("There is no file!")
		return None

	try:
		f = open(filename)
		image = Image.open(f)
		image.verify()
		f.seek(0)
		image = Image.open(f)

		if image.mode == 'RGBA':
			r,g,b,a = image.split()
			rgb_image = Image.merge('RGB', (r,g,b))
			invertImage = ImageOps.invert(rgb_image)
			r,g,b = invertImage.split()
			invertImage = Image.merge('RGBA', (r,g,b,a))
		else:
			invertImage = ImageOps.invert(image)

		invertImage.save(filename)
	except Exception as e:
		print("Exception!!" + str(e))
		return None

if __name__ == "__main__":
	#quick sanity check
	if not os.path.exists("/Users/"):
		print("There's no users folder! What system are you running on?")
		sys.exit(1)

	chromeDir = os.getenv("HOME") + chromePath

	if not os.path.exists(chromeDir):
		print("Have you got Chrome, and the Google Hangouts extension installed? If you do, then maybe they've updated it")
		sys.exit(1)

	print("Inverting the Chrome Google Hangout Files in " + chromeDir)
	dirList = os.listdir(chromeDir)
	for f in dirList:
		if f in supportedPatchLevels and os.path.exists(chromeDir+f+"/"+imagePath):
			patchFolder(chromeDir+f+"/"+imagePath)

