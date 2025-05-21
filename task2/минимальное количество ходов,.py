d = 1, 10, 2, 9
f = sum(d)
t = len(d)
r = f//t
cound = 0

for i in d:
    while i != r:
        if i < r:
            i = i+1
            cound+=1
        if i > r:
            i = i-1
            cound+=1
print(cound)




