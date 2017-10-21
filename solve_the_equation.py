string = 'x+5-3+x=6+x-2'

sides = string.split('=')
print(sides)
l = list(sides[0])
r = list(sides[1])
print(l)
print(r)

xs = 0
total = 0
for ch in l:
	if ch == 'x':
		