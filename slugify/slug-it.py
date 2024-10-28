## spits out a slugged title, warns about duplicates, used in db

import sys
from slugify import slugify
import csv
import codecs
' '.join(sys.argv[1:])

with open('slug-me.txt', newline='', encoding='utf-8') as f:
	slugs = []
	for row in f:
		row = slugify(row)
		if row in slugs and row != "":
			print("warning: " + row)
		slugs.append(row)
	
with open('slug-me.txt', "w", encoding='utf-8') as f:
	for slug in slugs:
		f.write(slug + '\n')