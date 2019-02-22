# 1.選擇性敘述的練習-season
# 輸入月份1~12月，判斷相對應的季節春、夏、秋、冬並印出。若不在此範圍則印出”輸入錯誤”。
m=int(input('please input month:'))
if m>=1 and m<=3 :
    print("Spring")
elif m>=4 and m<=6:
    print('Summer')
elif m>=7 and m<=9:
    print('Fall')
elif m>=10 and m<=12:
    print('Winter')
else:
    print('Error')

#2
s= int(input('please input your working hours:'))
if s<=60:
    print('your salary is',s*120,'dollars')
elif s>=61 and s<=80:
    print('your salary is',60*120+(s-60)*120*1.25,'dollars')
else :
    print('your salary is', 60 * 120 +20 * 120 * 1.25+(s-80)*120*1.5, 'dollars')

#3
x = int(input('家庭用電請填0工業用電請填1:'))
y = eval(input('輸入你的用電數:'))
if x == 0 :
    if y<=240:
        print('你的電費為',y*0.15,'元')
    elif y>240 and y<=540:
        print('你的電費為', y * 0.25, '元')
    else :
        print('你的電費為', y * 0.45, '元')
elif x==1:
   print('你的電費為',y*0.45,'元')
else :
    print('請填入0 or 1')


#4
a=int(input('請輸入西元年:'))
if (a % 4== 0 and a %100!=0) or a % 400 == 0 :
    if   a %4000 ==0:
        print(a, '年為平年')
    else:
        print(a, '年為閏年')
else:
    print(a, '年為平年')

#5
p=int(input("請輸入應付金額:"))
a=int(input("請輸入實付金額:"))
x=p-a
if x >0:
    print(x//500,'張五百元',
         (x%500)//100,'張一百元',
         (x % 500)%100//50,'個五十元',
         (x % 500) % 100 % 50//10,'個十元',
         (x % 500) % 100 % 50 % 10//5,'個五元',
         (x % 500) % 100 % 50 % 10 % 5,'個一元')
else:
    print('餘額不足')


#
import math
a,b,c=eval(input('請輸入三個數:'))
if b**2-4*a*c>=0:
    print('x=',(-b+math.sqrt(b**2-4*a*c)/2*a),'and',(-b-math.sqrt(b**2-4*a*c)/2*a))
else:
    print('沒有十根啦')

#2-1

total=0
for i in range(1,50,2):
    total=total+i**2

x=0
for j in range(2,51,2):
    x+=j**2

print(total-x)

#2-2
x=int(input('please input a number:'))
for i in range(1,x+1):
    if x%i==0:
        print(i)
        if i >x:
            break
#2-3


for x in range(1,101):
    w=0
    for i in range(1, x ):
        if x % i == 0:
            w+=i
    if w==x:
        print(x)

#2-4
for a in range (1,10):
    for b in range(0, 10):
        for c in range(0, 10):
            if 100*a+10*b+c==a**3+b**3+c**3:
                print(a*100+b*10+c)



#2-8
#出現”請輸入密碼”的提示，使用者有最多三次輸入的機會。
#若輸入正確，則印出”密碼輸入正確，歡迎使用本系統！”。
#若輸入不正確，再次出現”請輸入密碼”的提示。
#若三次輸入不正確，則印出”密碼輸入超過三次！”，並結束程式的執行。

password='apple123'
x= str(input("請輸入密碼:"))
for i in range(1,3):
    if password == x:
        print('密碼輸入正確，歡迎使用本系統！')
        break
    else :
        x=str(input("請輸入密碼:"))
        if i == 2 and password != x:
            print('密碼輸入超過三次！')
        elif i == 2 and password == x:
            print('密碼輸入正確，歡迎使用本系統！')

2-9
a='*'
for i in range(1,6):
    print(i*a)

a='*'
for i in range(5,0,-1):
    print(format(i*a,'>5s'))

for i in range(4):         # 總共有4層
        for j in range(4 - i - 1): # 在第一個*號出現前，先印出空白
                 print(" ", end = "")
        for k in range(i + 1):                # 印出該層所需要的*字數量
                print("* ", end = "" )
        print()                # 換行

#11.	迴圈敘述的練習-interest
#錢精打以10%單利投資100000元，郝細算則以5%複利投資100000元。
#計算多少年後郝細算的投資可以超過錢精打，並將此時兩人錢數印出。(27年後)
#提示：單利公式：P(1+r*n) 複利公式：P(1+r)n P：本金，r：利率，n：多少年

for i in range(1,100):
    if 100000+(10000*i) < 100000*(1.05)**i:
        print(i,'年')
        print('錢精打:',100000+(10000*i),'元')
        print('郝細算:',round(100000*(1.05)**i),'元')
        break

#2-12
print('  ','|  1  2  3  4  5  6  7  8  9  ')
print('---------------------------------------------')
for i in range(9,0,-1):
    print(i,' | ',end=' ')
    for j in range(1,i+1):
        print(i*j,end=' ')
    print()