# Searches game executables for lists of enums.
# This helps with aligning XML data with plain english names

import re

f = 'Atelier_Ryza_2.exe'

with open(f, mode='rb') as file:
	filecontent = file.read()
	x = re.findall(b'[A-Z0-9]{2,}[_]{1}[A-Z0-9_]{2,}\0', filecontent)
	
	with open('enums.txt', 'w') as f:
		for enum in x:
			enum = enum.replace(b'\x00', b'')
			f.write(enum.decode('ascii') + '\n')