from slugify import slugify
from shutil import copyfile

import os
files = os.listdir(".")

with open("map.txt") as f:
	for line in f:
		if line:
			line = line.rstrip().split('\t')
			name = "a18_monster_l_" + line[1].zfill(3) + "_.png"
			if name in files and len(line)>1:
				line[0] = slugify(line[0])
				copyfile(name, "new/" + line[0]+".png")