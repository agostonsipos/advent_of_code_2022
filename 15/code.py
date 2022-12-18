f = open("input.txt", "r")
s = f.read()

t = s.split("\n")

import re
r = re.compile('[a-zA-y :,=]+')

l = []

for b in t:
	a = r.split(b)
	l.append(list(map(int, a[1:5])))

#print(l)

def dist(a, b, x, y):
	return abs(a-x) + abs(b-y)

N = 10 
N = 2000000

s = set([])
l2 = []

for b in l:
	r = dist(b[0], b[1], b[2], b[3])
	l2.append([b[0], b[1], r])
	x = b[0]
	dy = dist(x, N, x, b[1])
	if dy <= r:
		dx = r - dy
		for i in range(x-dx, x+dx+1):
			if not (N == b[3] and i == b[2]):
				s.add(i)

print(len(list(s)))

M = 20
M = 4000000

for i in range(0, M+1):
	j = 0
	while j <= M:
		t = True
		jmp = 1
		for b in l2:
			if dist(i, j, b[0], b[1]) <= b[2]:
				dx = abs(i - b[0])
				dy = b[1] - j
				m = max(dy * 2 - 1, b[2] - dx - abs(dy))
				if m > jmp:
					jmp = m
				t = False
		if t:
			print(i*M + j)
			exit()
		j += jmp


