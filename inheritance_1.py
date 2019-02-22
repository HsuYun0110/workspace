class Parent():
    def m1(self):
        print('p_m1')
class Kid(Parent):
    pass

def main():
    a=Parent()
    b=Kid()
    a.m1()
    b.m1()
main()