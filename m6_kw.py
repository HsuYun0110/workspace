def aa(name,age):
    print('{} is {} years old'.format(name,age))
def main():
    aa('brook',18)
    aa(age=30,name='GG')
main()


def greet(*names):
    for i in names:
        print('Hello',i)
def main():
    greet('aaa','aaas','dar')
main()

def stu(*names):
    for i in names:
        print('Hello',i)
def main():
    greet('aaa','aaas','dar')
main()