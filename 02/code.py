f = open("input.txt", "r")
s = f.read()

t = s.split("\n")

def p1(c1, c2):
	return ord(c2) - ord('W')

def p2(c1, c2):
	return ((ord(c2) - (ord(c1) + ord('X') - ord('A')) + 4) % 3) * 3

sc = 0
for r in t:
	sc += p1(r[0], r[2]) + p2(r[0], r[2])

print(sc)


def p1_(c1, c2):
	return ((ord(c1) - ord('A')) + (ord(c2) - ord('Y'))) % 3 + 1

def p2_(c1, c2):
	return (ord(c2) - ord('X')) * 3 

sc = 0
for r in t:
	sc += p1_(r[0], r[2]) + p2_(r[0], r[2])

print(sc)
