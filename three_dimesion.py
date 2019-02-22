list=[[[12,5],[16,18],[13,25]],[[12,5],[16,18],[13,25]]]
print(list)
for i in range(len(list)):
    for j in range(len(list[i])):
        for k in range(len(list[i][j])):
            print(list[i][j][k],end=' ')
        print()