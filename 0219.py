from m9_class import Account

class CheckingAccount(Account):
    def __init__(self, number, name):
        super(CheckingAccount,self).__init__(number,name)
        self.credit=10000


    def withdraw(self, amount):
        try:
            if amount <= self.balance+self.credit:
                self.balance -= amount
            else:
                raise ValueError
        except ValueError:
            print('餘額不足')

    def __str__(self):
        return ('帳號:{} 姓名:{} 餘額:{}'.format(self.number, self.name, self.balance))


def main():
    accs = CheckingAccount('122334443','GG')
    print(accs)

    amount = int(input('輸入存款金額:'))
    accs.deposit(amount)
    wa = int(input('輸入提款金額'))
    accs.withdraw(wa)
    print(accs.balance)



main()