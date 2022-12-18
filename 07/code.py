class Directory:
	def __init__(self, ownsize, subdirs):
		self.ownsize = ownsize
		self.subdirs = subdirs

dirs = {}

f = open("input.txt", "r")
s = f.read()

t = s.split("\n")

def fullname(dir, subdir):
	if dir == "/":
		return dir + subdir
	else:
		return dir + "/" + subdir

def parent(dir):
	return "/".join(dir.split("/")[:-1])

for l in t:
	if l[0:4] == "$ cd":
		if l[5:] == "..":
			curDir = parent(curDir)
		elif l[5:] == "/":
			curDir = "/"
		else:
			curDir = fullname(curDir, l[5:])
	elif l[0:4] == "$ ls":
		if not curDir in dirs.keys():
			dirs[curDir] = Directory(0, []) # for /
	else:
		w = l.split(" ")
		if w[0] == "dir":
			dirs[curDir].subdirs.append(w[1])
			dirs[fullname(curDir, w[1])] = Directory(0, [])
		else:
			dirs[curDir].ownsize += int(w[0])

def size(dir):
	data = dirs[dir]
	s = data.ownsize
	for d in data.subdirs:
		s += size(fullname(dir, d))
	return s

x = 0
for d in dirs.keys():
	if size(d) < 100000:
		x += size(d)

print(x) # part 1

needed = size("/") - 40000000

mind = "/"
for d in dirs.keys():
	if size(d) >= needed and size(d) < size(mind):
		mind = d

print(size(mind)) # part 2
