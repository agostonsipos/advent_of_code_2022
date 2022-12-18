
hx = 0
hy = 0
tx = 0
ty = 0


f = open("input.txt", "r")
s = f.read()

t = s.split("\n")

places = [(0,0)]

for l in t:
	cmd = l.split(" ")
	dir = cmd[0]
	step = int(cmd[1])
	if dir == 'R':
		for i in range(step):
			hx += 1
			if hx >= tx + 2:
				tx = hx - 1
				ty = hy
				places.append((tx,ty))
	elif dir == 'L':
		for i in range(step):
			hx -= 1
			if hx <= tx - 2:
				tx = hx + 1
				ty = hy
				places.append((tx,ty))
	elif dir == 'U':
		for i in range(step):
			hy += 1
			if hy >= ty + 2:
				ty = hy - 1
				tx = hx
				places.append((tx,ty))
	elif dir == 'D':
		for i in range(step):
			hy -= 1
			if hy <= ty - 2:
				ty = hy + 1
				tx = hx
				places.append((tx,ty))


print(len(list(set(places))))


x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

places = [(0,0)]

def update(j):
	a = x[j] >= x[j+1] + 2
	b = x[j] <= x[j+1] - 2
	c = y[j] >= y[j+1] + 2
	d = y[j] <= y[j+1] - 2
	if a and c:
		x[j+1] = x[j] - 1
		y[j+1] = y[j] - 1
		return
	if a and d:
		x[j+1] = x[j] - 1
		y[j+1] = y[j] + 1
		return
	if b and c:
		x[j+1] = x[j] + 1
		y[j+1] = y[j] - 1
		return
	if b and d:
		x[j+1] = x[j] + 1
		y[j+1] = y[j] + 1
		return
	if a:
		x[j+1] = x[j] - 1
		y[j+1] = y[j]
	if b:
		x[j+1] = x[j] + 1
		y[j+1] = y[j]
	if c:
		y[j+1] = y[j] - 1
		x[j+1] = x[j]
	if d:
		y[j+1] = y[j] + 1
		x[j+1] = x[j]


for l in t:
	cmd = l.split(" ")
	dir = cmd[0]
	step = int(cmd[1])
	for i in range(step):
		if dir == 'R':
			x[0] += 1
		elif dir == 'L':
			x[0] -= 1
		elif dir == 'U':
			y[0] += 1
		elif dir == 'D':
			y[0] -= 1
		for j in range(9):
			update(j)
		places.append((x[9], y[9]))

print(len(list(set(places))))

