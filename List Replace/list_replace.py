## replaces files from a list.
## This is used for turning XML game data enums into a humam readable, database ready format.
## usage: list_replace.py find-replace.txt file.txt

import sys
import csv
import codecs
' '.join(sys.argv[1:])

with open(sys.argv[1], newline='', encoding='utf-8') as csvfile:
	reader = csv.reader(csvfile, delimiter='\t')
	with open (sys.argv[2], 'U') as f:
		text = f.read()
		for row in reader:
			if row[0]:
				print(row[0] + '\t' + row[1])
				if row[1]:
					while row[0]+'\t' in text:
						text = text.replace(row[0]+'\t', row[1]+'\t')
	with open(sys.argv[2], "w") as f:
		f.write(text)