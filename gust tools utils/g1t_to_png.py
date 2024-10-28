# convert G1T to PNG
# usage: g1t_to_png.py path_to_file_folder
# is not recursive

import sys
import os
import glob

ls = os.listdir(os.getcwd())

# convert all gt1 to dds
for file in ls:
	if '.g1t' in file:
		os.system("gust_g1t.exe " + file)

ls = os.listdir(os.getcwd())

# go into created folders, convert dds to png, delete dds
for item in ls:
	if os.path.isdir(item):
		ls2 = os.listdir(item)
		for item2 in ls2:
			if '.dds' in item2:
				print(item2)
				print(os.path.basename(item))
				os.system("magick " + os.path.basename(item) + '\\' + item2 + " -trim " + os.path.basename(item) + '\\' + os.path.basename(item) + "_" + item2[:-4] +".png")
		os.system("DEL " + os.path.basename(item) + "\\*.dds")
		os.system("DEL " + os.path.basename(item) + "\\*.json")
