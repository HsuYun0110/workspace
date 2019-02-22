class Account:
    def __init__(self,number,name):
        self.number=number
        self.name= name
        self.balance=0
    def deposit(self,amount):
        try:
            if amount<=0:
                raise ValueError
            else:
                self.balance=amount+self.balance
        except ValueError:
            print('金額必須為正整數!')
    def withdraw(self,amount):
        try:
            if amount <=self.balance:
                self.balance -= amount
            else:
                raise ValueError
        except ValueError:
            print('餘額不足')

    def __str__(self):
        return ('帳號:{} 姓名:{} 餘額:{}'.format(self.number,self.name,self.balance))
def main():
    accs = Account('122334443', '55')
    print(accs)

    amount = int(input('輸入存款金額:'))
    accs.deposit(amount)
    wa = int(input('輸入提款金額'))
    accs.withdraw(wa)
    print(accs.balance)

main()
