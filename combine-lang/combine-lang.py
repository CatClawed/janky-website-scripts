import sys

# Aligns all the language data side by side so I don't want to end myself doing this by hand
# Usage: combine-lang.py filename [file 1] [file2] etc ...
# If ya mess up it ain't checking

# combine-lang.py effects.txt text_en/str_item_effect.txt text_en/str_library_eff_detail.txt text_jp/str_item_effect.txt text_jp/str_library_eff_detail.txt text_kr/str_item_effect.txt text_kr/str_library_eff_detail.txt text_fr/str_item_effect.txt text_fr/str_library_eff_detail.txt text_sc/str_item_effect.txt text_sc/str_library_eff_detail.txt text_tc/str_item_effect.txt text_tc/str_library_eff_detail.txt 

if len(sys.argv) < 4:
	print("provide more files")
else:
	full = []
	for i in range(2, len(sys.argv)):
		print(sys.argv[i])
		lines = []
		with open(sys.argv[i]) as file:
			for row in file:
				data = row.split('\t')
				lines.append(data[len(data)-1].rstrip()) # consistently last in row
		full.append(lines)
	with open(sys.argv[1], "w", encoding='utf-8') as file:
		for i in range(0, len(full[1])):
			str = ""
			for j in range(0, len(full)):
				str = str + full[j][i] + '\t'
			file.write(str + '\n')