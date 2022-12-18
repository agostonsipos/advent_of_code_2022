f = open("input.txt", "r")
s = f.read()

t = s.split("\n")

c = []
m = 0

for l in t:
	a = l.split(",")
	c.append(tuple(map(int, a)))
	for i in c[-1]:
		if i > m:
			m = i

space = []
for i in range(m+2):
	space.append([])
	for j in range(m+2):
		space[i].append([])
		for k in range(m+2):
			space[i][j].append(False)

for l in c:
	(i,j,k) = l
	space[i][j][k] = True

A = 0

for i in range(m+1):
	for j in range(m+1):
		for k in range(m+1):
			if space[i][j][k]:
				if not space[i-1][j][k]:
					A += 1
				if not space[i+1][j][k]:
					A += 1
				if not space[i][j-1][k]:
					A += 1
				if not space[i][j+1][k]:
					A += 1
				if not space[i][j][k-1]:
					A += 1
				if not space[i][j][k+1]:
					A += 1


print(A)

import sys
sys.setrecursionlimit((m+2)**3)

air = []
for i in range(m+2):
	air.append([])
	for j in range(m+2):
		air[i].append([])
		for k in range(m+2):
			air[i][j].append(False)

def flow_air(i,j,k):
	if i < 0 or i > m+1 or j < 0 or j > m+1 or k < 0 or k > m+1 or air[i][j][k]:
		return
	if not space[i][j][k]:
		air[i][j][k] = True
		flow_air(i-1,j,k)
		flow_air(i+1,j,k)
		flow_air(i,j-1,k)
		flow_air(i,j+1,k)
		flow_air(i,j,k-1)
		flow_air(i,j,k+1)


flow_air(0,0,0)

A = 0

for i in range(m+1):
	for j in range(m+1):
		for k in range(m+1):
			if not air[i][j][k]:
				if air[i-1][j][k]:
					A += 1
				if air[i+1][j][k]:
					A += 1
				if air[i][j-1][k]:
					A += 1
				if air[i][j+1][k]:
					A += 1
				if air[i][j][k-1]:
					A += 1
				if air[i][j][k+1]:
					A += 1

print(A)
