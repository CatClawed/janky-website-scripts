# convert XML.3
# usage: gust_XML.py game
# is not recursive

import sys
import os
import glob

if len(sys.argv) != 2:
	print("Two arguments plz")
else:
	ls = os.listdir(os.getcwd())

	# convert all gt1 to dds
	for file in ls:
		if '.xml.e' in file:
			os.system("gust_enc.exe " + str(sys.argv[1]) + " " + file)