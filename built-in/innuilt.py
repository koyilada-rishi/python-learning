l = [1, 2, 3, 4, 5, 4, 6, 7, 8, 9, 10]
print(l[-5])
l.append(30)
print(l)
l.insert(1, 22)
print(l)
print(4 in l)
print(l.count(4))
print(l.index(4))
print(l.index(4, 2, 6))

l.remove(3)
print(l)
print(l.pop())
print(l)
print(l.pop(2))
print(l)
del l[1]
print(l)
del l[0:2]
print(l)

print(max(l))
print(min(l))
print(sum(l))
l.reverse()
print(l)
l.sort()
a=sorted(l)
print(l)