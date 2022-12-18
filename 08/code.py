f = open("input.txt", "r")
s = f.read()

t = s.split("\n")

n = 99

m = []
i = 0
for l in t:
	m.append([])
	for c in l:
		m[i].append(int(c))
	i += 1



def visible(i,j):
	v = True
	for k in range(i-1, -1, -1):
		if(m[k][j] >= m[i][j]):
			v = False
			break
	if v:
		return v
	v = True
	for k in range(i+1, n):
		if(m[k][j] >= m[i][j]):
			v = False
			break
	if v:
		return v
	v = True
	for k in range(j-1, -1, -1):
		if(m[i][k] >= m[i][j]):
			v = False
			break
	if v:
		return v
	v = True
	for k in range(j+1, n):
		if(m[i][k] >= m[i][j]):
			v = False
			break
	if v:
		return v

c = 0
for i in range(n):
	for j in range(n):
		if visible(i, j):
			c += 1

print(c)

def score(i,j):
	if(i == 0 or i == n-1 or j == 0 or j == n-1):
		return 0
	s = 1
	c = 1
	for k in range(i-1, -1, -1):
		if(m[k][j] >= m[i][j] or k == 0):
			break
		c += 1
	s *= c
	c = 1
	for k in range(i+1, n):
		if(m[k][j] >= m[i][j] or k == n-1):
			break
		c += 1
	s *= c
	c = 1
	for k in range(j-1, -1, -1):
		if(m[i][k] >= m[i][j] or k == 0):
			break
		c += 1
	s *= c
	c = 1
	for k in range(j+1, n):
		if(m[i][k] >= m[i][j] or k == n-1):
			break
		c += 1
	s *= c
	return s

c = 0
for i in range(n):
	for j in range(n):
		if score(i,j) > c:
			c = score(i,j)

print(c)
