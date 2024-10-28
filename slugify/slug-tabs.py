## spits out a slugged title, does not warn about duplicates
## what's a command line argument, why would I ever do one of those

import sys
from slugify import slugify
import csv
import codecs
' '.join(sys.argv[1:])

with open('slug-me.txt', newline='', encoding='utf-8') as f:
	slugs = []
	for row in f:
		row = row.split('\t')
		arr = []
		for s in row:
			arr.append(slugify(s))
		slugs.append(arr)
	
with open('slug-me.txt', "w", encoding='utf-8') as f:
	for slug in slugs:
		str = ""
		for s in slug:
			str = str + s + '\t'
		f.write(str + '\n')