
file = open('input.txt',mode='r')

s = file.read()

file.close()

t = s.split("\n")

def prio(c):
	if ord(c) >= ord('a'):
		return ord(c) - ord('a') + 1
	else:
		return ord(c) - ord('A') + 27

m = 0
for s in t:
	n = len(s)
	s1 = set(list(s[0:(n//2)]))
	s2 = set(list(s[(n//2):n]))
	st = s1.intersection(s2)
	for el in st:
		m += prio(el)

print(m)

i = 0
m = 0
while i < len(t) - 2:
	s1 = set(list(t[i]))
	s2 = set(list(t[i+1]))
	s3 = set(list(t[i+2]))
	st = s1.intersection(s2).intersection(s3)
	for el in st:
		m += prio(el)
	i += 3

print(m)
