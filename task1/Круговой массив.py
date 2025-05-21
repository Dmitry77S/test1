# Круговой массив
n = 5
m = 4
f = []
t = 1
r = False
while r != True:
    if t == 0:
        t = n
    for i in range(m):
        f.append(t)
        t += 1
        if t == n+1:
            t = 1
    t = t-1

    f.append(',')
    if f[-2] == 1:
        r = True

w = ''
d = (f[:-1])
for i in d:
    w += str(i)
s = ''
for i in range(n):
    s += str(i+1)
q = ''
for i in w.split(','):
    q += i[0]

print(f'Круговой массив {s}')
print(f'При длине ообхода {m} получаем интервалы: {w}')
print(f'Полученный путь: {q}')






