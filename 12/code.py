f = open("input.txt", "r")
s = f.read()

t = s.split("\n")

mat = []
dist = []

N = 41*136

x = y = -1
j = 0
for l in t:
	mat.append(list(l))
	dist.append([float("inf")] * len(l))
	for i in range(len(mat[-1])):
		if mat[-1][i] == 'S':
			mat[-1][i] = 'a'
			dist[-1][i] = 0
		if mat[-1][i] == 'E':
			mat[-1][i] = 'z'
			x = j
			y = i
	j += 1

def updatek(i, j, k, l):
	try:
	    if (ord(mat[i][j]) - ord(mat[i+k][j+l]) <= 1 and dist[i+k][j+l] + 1 < dist[i][j]):
	    	dist[i][j] = dist[i+k][j+l] + 1
	except IndexError:
	    return

def update(i, j):
	updatek(i, j, -1, 0)
	updatek(i, j, 1, 0)
	updatek(i, j, 0, -1)
	updatek(i, j, 0, 1)

def solve():
	for i in range(N):
		if i > dist[x][y]:
			return dist[x][y]
		for a in range(len(dist)):
			for b in range(len(dist[a])):
				update(a, b)

print(solve())

for i in range(len(mat)):
	for j in range(len(mat[i])):
		if mat[i][j] == 'a':
			dist[i][j] = 0

print(solve())


