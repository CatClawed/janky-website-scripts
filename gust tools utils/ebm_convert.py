import sys
import os
import glob

ls = os.listdir(os.getcwd())

for item in ls:
	if os.path.isdir(item):
		ls2 = os.listdir(item)
		for item2 in ls2:
			if '.ebm' in item2:
				os.system("gust_ebm.exe " + item2)