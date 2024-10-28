# I really hated the ads in File Optimizer
# So I took a number of the tools and settings it was using
# I don't have to worry about stuff like APNG and such
# And I want lossy for web
# Many times faster than File Optimizer without the ads, uninstalled that garbage
# I should work out a JPG solution sometime

import sys
import os

folder = sys.argv[1]
files = os.listdir(folder)

for file in files:
	abs = folder + "\\" + file # oh right the join function exists whoops
	os.system("pngquant.exe --strip --quality=85-95 --speed 1 --ext .png --force {}".format(abs))
	os.system("truepng.exe -tz -md remove all -a1 -g1 -l /i0 /nc /tz /quiet /y /out {} {}".format(abs, abs))
	os.system("PngOptimizerCL.exe -KeepPhysicalPixelDimensions -file:{}".format(abs))
	os.system("pngout.exe /q /y /r /d0 /mincodes0 /kacTL,fcTL,fdAT {} {}".format(abs, abs))
	os.system("optipng.exe -zw32k -quiet -strip all {}".format(abs))
	os.system("ect-0.8.3.exe -quiet --mt-deflate --allfilters --reuse {}".format(abs))
	os.system("pingo.exe -x3 {}".format(abs))
	print(abs)