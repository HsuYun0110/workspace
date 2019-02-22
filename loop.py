n=1
total=0
while n<=10:
    total= total+n
    n+=1
print(total)

n=1
total=0
while n<=100:
    total= total+n
    n+=1
print(total)

n=1
total=0
while n<=100:
    total= total+n
    n+=2
print(total)

n=2
total=0
while n<=100:
    total= total+n
    n+=2
print(total)

total=0
for i in range(1,11):
    total=total+i
print(total)

for i in range(1,10):
    for j in range(1,10):
        print(i,"*",j,'=',i*j,' ', end=' ')
    print()

    n = 1
    total = 0
    while n<=100:
        total = total + n
        n += 1
        if n==11:
            break
    print(total)