import re

fname = open("mbox-short.txt", "r")
l = list()
for line in fname:
	line = line.rstrip()
	results = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	#print (results)
	if len(results) == 0:
		continue
	num = float(results[0])
	#print(num)
	l.append(num)
#print (l)
print("Number of Values:", len(l))
print("Maximum:", max(l))
print("Minimum:", min(l))
print("Average:", ((sum(l)/len(l))))

