f = open("input.txt", "r")
s = f.read()

def solve(psize):
	a = 0
	while True:
		b = True
		for i in range(psize):
			for j in range(i+1, psize):
				if s[a+i] == s[a+j]:
					b = False
		if b:
			print(a+psize)
			break
		a += 1

solve(4)
solve(14)
