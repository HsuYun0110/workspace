##1.	綜合的練習-checkID
##寫一函數isID (ID)用來判斷ID是否為正確身份証字號。
'''''
A	10	臺北市 B	11	臺中市 C	12	基隆市 D	13	臺南市 E	14	高雄市 F	15	新北市
G	16	宜蘭縣 H	17	桃園市 I	34	嘉義市 J	18	新竹縣 K	19	苗栗縣 M	21	南投縣
N	22	彰化縣 O	35	新竹市 P	23	雲林縣 Q	24	嘉義縣 T	27	屏東縣 U	28	花蓮縣
V	29	臺東縣 W	32	金門縣 X	30	澎湖縣 Z	33	連江縣
'''''
while True:
    strid=str(input('please input ID:'))
    if len(strid)!=10:
        print('長度輸入錯誤')
        break
    sum=0
    if strid[0]=='A':
        sum=1
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='B':
        sum=10
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='C':
        sum=19
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='D':
        sum= 28
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='E':
        sum=37
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='F':
        sum=46
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='G':
        sum=55
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='H':
        sum=64
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='I':
        sum=39
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='J':
        sum=73
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='K':
        sum=82
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='M':
        sum=11
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='N':
        sum=20
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='O':
        sum= 48
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='P':
        sum=29
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='Q':
        sum=38
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='T':
        sum=65
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='U':
        sum=74
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='V':
        sum=83
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='W':
        sum=21
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='X':
        sum=3
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    elif strid[0]=='Z':
        sum=30
        if int(strid[1])==1 or int(strid[1])==2:
            if (sum+int(strid[1])*8+int(strid[2])*7+int(strid[3])*6+int(strid[4])*5+int(strid[5])*4+int(strid[6])*3+int(strid[7])*2+int(strid[8])*1+int(strid[9])*1)%10==0:
                print('輸入正確')
                break
            else:
                print('輸入錯誤')
                break
        else:
            print('輸入錯誤')
            break
    else:
        print('輸入錯誤')
        break








##2.	綜合的練習-idGenerator
##輸入地區和性別，經由亂數產生一個身份証字號。





##3.	綜合練習-poker
##經由亂數發撲克牌(52張)，分為四組列印出來。.
import random
f=['黑桃A','黑桃2','黑桃3','黑桃4','黑桃5','黑桃6','黑桃7','黑桃8','黑桃9','黑桃10','黑桃J','黑桃Q','黑桃K',
'紅心A','紅心2','紅心3','紅心4','紅心5','紅心6','紅心7','紅心8','紅心9','紅心10','紅心J','紅心Q','紅心K',
'磚塊A','磚塊2','磚塊3','磚塊4','磚塊5','磚塊6','磚塊7','磚塊8','磚塊9','磚塊10','磚塊J','磚塊Q','磚塊K',
'梅花A','梅花2','梅花3','梅花4','梅花5','梅花6','梅花7','梅花8','梅花9','梅花10','梅花J','梅花Q','梅花K']
random.shuffle(f)
print(f[0:12])
print(f[13:26])
print(f[27:40])
print(f[40:53])




##4.	日期的練習-MyCalendar
##輸入一個正整數，列印出那一年的年曆。
##輸入兩個整數，第一個數字代表那一年，第二個數字代表那一月，列印出那一年那一月的月曆。

