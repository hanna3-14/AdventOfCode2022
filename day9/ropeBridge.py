import re

f = open("ropeBridge.txt", "r")
lines = f.readlines()

ihead = 0
jhead = 0
itail = 0
jtail = 0

visited = []

# task 1
for line in lines:
	re.sub("\n", "", line)
	chunks = line.split(' ')

	if re.match('R', line):
		jhead += int(chunks[1])
		if not (abs(ihead - itail) <= 1 and abs(jhead - jtail) <= 1):
			itail = ihead
			jtail += 1
			while jtail < jhead:
				visited.append([itail, jtail])
				jtail += 1
			jtail -= 1
	elif re.match('L', line):
		jhead -= int(chunks[1])
		if not (abs(ihead - itail) <= 1 and abs(jhead - jtail) <= 1):
			itail = ihead
			jtail -= 1
			while jtail > jhead:
				visited.append([itail, jtail])
				jtail -= 1
			jtail += 1
	elif re.match('U', line):
		ihead += int(chunks[1])
		if not (abs(ihead - itail) <= 1 and abs(jhead - jtail) <= 1):
			jtail = jhead
			itail += 1
			while itail < ihead:
				visited.append([itail, jtail])
				itail += 1
			itail -= 1
	elif re.match('D', line):
		ihead -= int(chunks[1])
		if not (abs(ihead - itail) <= 1 and abs(jhead - jtail) <= 1):
			jtail = jhead
			itail -= 1
			while itail > ihead:
				visited.append([itail, jtail])
				itail -= 1
			itail += 1

filtered = []
[filtered.append(x) for x in visited if x not in filtered]
print(len(filtered))
