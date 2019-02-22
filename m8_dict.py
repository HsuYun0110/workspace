dict1={'Apple':'jOBS','MS':'BG','AMAZON':'JEFF'}
print(dict1.keys())
print('Apple' in dict1)
dict1['III']='trash'
print(tuple(dict1.keys()))
print(tuple(dict1.values()))
print(dict1)


def greet(*names):
    for name in names:
        print('Hello',name)
def main():
    name1=tuple(dict1.values())
    greet(*name1)
main()


x=(i*i for i in range(1,10))
for y in x:
    print(y,end=" ")
