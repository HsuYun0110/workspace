def fractorial(x):
    total=1
    for i in range(1,x+1):
        total = total*i
    return total

def main():
    a=int(input("輸入一個輸字:"))
    c= fractorial(a)
    print(a,'!',' =',c)
main()