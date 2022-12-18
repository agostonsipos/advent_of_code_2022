f = open("input.txt", "r")
s = f.read()

t = s.split("\n")

xmin = xmax = 500
ymax = 0

for l in t:
	s = l.split(" -> ")
	for k in s:
		r = k.split(",")
		i = int(r[0])
		j = int(r[1])
		if i < xmin:
			xmin = i
		elif i > xmax:
			xmax = i
		if j > ymax:
			ymax = j

mat = [[" "] * 1000 for _ in range(ymax + 2)]

for l in t:
	s = l.split(" -> ")
	p = s[0].split(",")
	x = int(p[0])
	y = int(p[1])
	mat[y][x] = "#"
	for i in range(1, len(s)):
		r = s[i].split(",")
		if x == int(r[0]):
			z = int(r[1])
			for j in range(min(y, z), max(y, z)+1):
				mat[j][x] = "#"
			y = z
		else: # y == int(r[1])
			z = int(r[0])
			for j in range(min(x, z), max(x, z)+1):
				mat[y][j] = "#"
			x = z

def sim1():
	c = 0
	while True:
		x = 500
		y = 0
		while True:
			if y >= ymax + 1:
				return c
			elif mat[y+1][x] == " ":
				y += 1
			elif mat[y+1][x-1] == " ":
				x -= 1
				y += 1
			elif mat[y+1][x+1] == " ":
				x += 1
				y += 1
			else:
				mat[y][x] = "*"
				break
		c += 1

a = sim1()

print(a)

def sim2():
	c = 0
	while True:
		x = 500
		y = 0
		if mat[y][x] == "*":
			return c
		while True:
			if y >= ymax + 1:
				mat[y][x] = "*"
				break
			elif mat[y+1][x] == " ":
				y += 1
			elif mat[y+1][x-1] == " ":
				x -= 1
				y += 1
			elif mat[y+1][x+1] == " ":
				x += 1
				y += 1
			else:
				mat[y][x] = "*"
				break
		c += 1

b = sim2()

print(a + b)

