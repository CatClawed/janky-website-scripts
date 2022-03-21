# Inserts newlines
# for atelier games
# properly aligns text with enums and other data
# encoding sucks, binary rocks

import xml.etree.ElementTree as ET
import struct
import glob
import os

ls = os.listdir(os.getcwd())

for f in ls:
	if f.endswith('.xml'):
		print(f)
		txt = open(f[:-3] + "txt", "wb")
		tree = ET.parse(f)
		root = tree.getroot()
		
		if len(root) == 0:
			continue
			
		num = int(root[0].attrib['String_No'])

		for child in root:
			num2 = int(child.attrib['String_No'])
            
			
			if num2 > num:
				while num < num2:
					txt.write('\n'.encode())
					num = num+1
			try:
				thing = child.attrib['String_ID']
			except:
				thing = ""
			txt.write(child.attrib['String_No'].encode('utf-8') + '\t'.encode('utf-8') + thing.encode('utf-8') + '\t'.encode('utf-8') + child.attrib['Text'].encode('utf-8'))
			num = num2
			
		txt.close()