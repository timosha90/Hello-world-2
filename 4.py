from random import randint
a = (1, 18, 55, 6, 78, 99, 78, 85, 12, 22 )
print(max(a))
print(min(a))


b = []
c = []
for i in range(10):
    k = randint(0, 5)
    b.append(randint(0, 5))
    c.append(randint(0, 5))
b = tuple(b)
c = tuple(c)
print(b)
print(c)
d = b+c
print(d)
print(d.count(0))


