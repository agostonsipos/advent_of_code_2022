
file = open('input.txt',mode='r')

s = file.read()

file.close()

arrays = s.split("\n\n")

m = 0
for array in arrays:
	t = array.split()
	if sum(map(int, t)) > m:
		m = sum(map(int, t))

print(m)


m = []
for array in arrays:
	t = array.split()
	m.append(sum(map(int, t)))

m.sort(reverse=True)
print(m[0]+m[1]+m[2])
