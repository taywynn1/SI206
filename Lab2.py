fname = open('TheVictors.txt')
l = list()
d = dict()
for line in fname:
	words = line.split()
	for word in words:
		if word in d:
			d[word] += 1
		else:
			d[word] = 1
new_lst = list()
for key, val in d.items():
	new_lst.append((val, key))
new_lst.sort(reverse = True)

for val, key in new_lst[:15]:
	print (key, val)

