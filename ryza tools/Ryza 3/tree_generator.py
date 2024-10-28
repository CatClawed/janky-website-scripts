# generates a recipe 'tree'
# one line per final item, rather than a tree structure
# child parent order

import csv

with open('item_recipe_list.txt') as f:
	reader = csv.reader(f, delimiter='\t')
	recipes = list(reader)

# find roots, 'flatten' children with two parents
i = 0
rm = []
recipe_links = []
for root in recipes:
	if len(root) == 1:
		recipe_links.append(root)
		rm.append(i)
	if len(root) == 3:
		recipes.append([root[0], root[1]])
		recipes.append([root[0], root[2]])
		rm.append(i)
	i = i + 1

depth = 1 # index +1
i = len(rm)-1
while len(rm) > 0:
	del recipes[rm[i]]
	del rm[i]
	i = i - 1

# for each parent
# find child that matches
# create new ancestry line
	
depth = 0
new_children = 1 # since this is guaranteed
while new_children > 0:
	new_children = 0
	for parent in recipe_links:
		if len(parent) == depth+1:
			# search for matching children
			for child in recipes:
				if parent[depth] == child[1]:
					new_children = new_children + 1
					p = parent.copy()
					p.append(child[0])
					recipe_links.append(p)		
	depth = depth + 1
		
#print(recipe_links)

file = open('recipe_links.txt', 'w')
for recipe in recipe_links:
	s = ""
	depth = 0
	item = recipe[len(recipe)-1]
	for item in recipe:
		s += ' > ' + item
		depth = depth + 1
	if len(recipe) > 1:
		file.write(item + '\t' + s + '\t' + str(depth) + '\n')

file.close()
