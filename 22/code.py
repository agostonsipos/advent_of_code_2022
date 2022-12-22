f = open("input.txt", "r")
s = f.read()

ls = s.split("\n\n")[0].split("\n")
mat = list(map(list, ls))

rs = s.split("\n\n")[1].replace("L", " L ").replace("R", " R ").split(" ")

m = 0
for l in mat:
	if len(l) > m:
		m = len(l)

for l in mat:
	while len(l) < m:
		l.append(" ")

n = len(mat)

y = 0
x = 0
while mat[y][x] == " ":
	x += 1

dx = 1
dy = 0

def index(x, y):
	return mat[y%n][x%m]


for r in rs:
	if r == "R":
		ndy = dx
		dx = -dy
		dy = ndy
	elif r == "L":
		ndy = -dx
		dx = dy
		dy = ndy
	else:
		k = int(r)
		for i in range(k):
			nx = x+dx
			ny = y+dy
			while index(nx, ny) == " ":
				nx += dx
				ny += dy
			if index(nx, ny) == "#":
				break
			x = nx % m
			y = ny % n

d = 0

if dx == 1 and dy == 0:
	d = 0
if dx == 0 and dy == 1:
	d = 1
if dx == -1 and dy == 0:
	d = 2
if dx == 0 and dy == -1:
	d = 3

print((y+1)*1000 + (x+1)*4 + d)

#  12
#  3
# 54
# 6
E = n // 4
y = 0
x = 0
while mat[y][x] == " ":
	x += 1

dx = 1
dy = 0

for r in rs:
	if r == "R":
		ndy = dx
		dx = -dy
		dy = ndy
	elif r == "L":
		ndy = -dx
		dx = dy
		dy = ndy
	else:
		k = int(r)
		for i in range(k):
			nx = x+dx
			ny = y+dy
			odx = dx
			ody = dy
			if index(nx, ny) == " ":
				nx = nx % m
				ny = ny % n
				if ny == 4*E-1 and E <= nx and nx < 2*E and dy == -1: # 1 to 6
					ny = nx + 2*E
					nx = 0
					dx = 1
					dy = 0
				elif ny == 4*E-1 and 2*E <= nx and nx < 3*E and dy == -1: # 2 to 6
					nx = nx - 2*E
					ny = 4*E-1
					dx = 0
					dy = -1
				elif nx == E-1 and 0 <= ny and ny < E and dx == -1: # 1 to 5
					ny = 3*E-1 - ny
					nx = 0
					dx = 1
					dy = 0
				elif nx == 0 and 0 <= ny and ny < E and dx == 1: # 2 to 4
					nx = 2*E-1
					ny = 3*E-1 - ny
					dx = -1
					dy = 0
				elif ny == E and 2*E <= nx and nx < 3*E and dy == 1: # 2 to 3
					ny = nx - E
					nx = 2*E-1
					dx = -1
					dy = 0
				elif nx == 2*E and E <= ny and ny < 2*E and dx == 1: # 3 to 2
					nx = ny + E
					ny = E-1
					dx = 0
					dy = -1
				elif nx == E-1 and E <= ny and ny < 2*E and dx == -1: # 3 to 5
					nx = ny - E
					ny = 2*E
					dx = 0
					dy = 1
				elif ny == 2*E-1 and 0 <= nx and nx < E and dy == -1: # 5 to 3
					ny = nx + E
					nx = E
					dx = 1
					dy = 0
				elif nx == 3*E-1 and 2*E <= ny and ny < 3*E and dx == -1: # 5 to 1
					ny = 3*E-1 - ny
					nx = E
					dx = 1
					dy = 0
				elif nx == 2*E and 2*E <= ny and ny < 3*E and dx == 1: # 4 to 2
					ny = 3*E-1 - ny
					nx = 3*E-1
					dx = -1
					dy = 0
				elif ny == 3*E and E <= nx and nx < 2*E and dy == 1: # 4 to 6
					ny = nx + 2*E
					nx = E-1
					dx = -1
					dy = 0
				elif nx == E and 3*E <= ny and ny < 4*E and dx == 1: # 6 to 4
					nx = ny - 2*E
					ny = 3*E-1
					dx = 0
					dy = -1
				elif nx == 3*E-1 and 3*E <= ny and ny < 4*E and dx == -1: # 6 to 1
					nx = ny -2*E
					ny = 0
					dx = 0
					dy = 1
				elif ny == 0 and 0 <= nx and nx < E and dy == 1: # 6 to 2
					nx = nx + 2*E
					ny = 0
					dx = 0
					dy = 1
				else:
					print("leaving board at wrong location")
					print(nx, ny)
					exit()
			if index(nx, ny) == "#":
				dx = odx
				dy = ody
				break
			x = nx % m
			y = ny % n

#  12
#  3
# 54
# 6

d = 0

if dx == 1 and dy == 0:
	d = 0
if dx == 0 and dy == 1:
	d = 1
if dx == -1 and dy == 0:
	d = 2
if dx == 0 and dy == -1:
	d = 3

print((y+1)*1000 + (x+1)*4 + d)
