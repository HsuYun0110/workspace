place=str(input('請輸入縣市'))
gender=int(input('請輸入性別1:男,2:女'))
dict1={'台北市': 'A', '新竹縣': 'J', '台中市': 'B', '苗栗縣': 'K', '屏東縣': 'T', '基隆市': 'C',
     '花蓮縣': 'U', '台南市': 'D', '南投縣': 'M', '台東縣': 'V', '高雄市': 'E', '彰化縣': 'N',
    '金門縣': 'W',  '新竹市': 'O', '澎湖縣': 'X', '宜蘭縣': 'G', '雲林縣': 'P',
    '桃園市': 'H', '嘉義縣': 'Q', '連江縣': 'Z'}

import random
while True:
    strid = []
    strid.append(dict1[place])
    strid.append(gender)
    for i in range(8):
        strid.append(random.randint(0,9))
    strid=str(strid[0])+str(strid[1])+str(strid[2])+str(strid[3])+str(strid[4])+str(strid[5])+str(strid[6])+str(strid[7])+str(strid[8])+str(strid[9])

    if strid[0] == 'A':
        sum = 1
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為',strid)
                break
    elif strid[0] == 'B':
        sum = 10
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'C':
        sum = 19
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'D':
        sum = 28
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'E':
        sum = 37
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'F':
        sum = 46
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'G':
        sum = 55
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break

    elif strid[0] == 'H':
        sum = 64
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'I':
        sum = 39
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'J':
        sum = 73
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
    elif strid[0] == 'K':
        sum = 82
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
    elif strid[0] == 'M':
        sum = 11
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'N':
        sum = 20
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'O':
        sum = 48
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'P':
        sum = 29
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'Q':
        sum = 38
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'T':
        sum = 65
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'U':
        sum = 74
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'V':
        sum = 83
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break

    elif strid[0] == 'W':
        sum = 21
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'X':
        sum = 3
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
    elif strid[0] == 'Z':
        sum = 30
        if int(strid[1]) == 1 or int(strid[1]) == 2:
            if (sum + int(strid[1]) * 8 + int(strid[2]) * 7 + int(strid[3]) * 6 + int(strid[4]) * 5 + int(
                    strid[5]) * 4 + int(strid[6]) * 3 + int(strid[7]) * 2 + int(strid[8]) * 1 + int(
                    strid[9]) * 1) % 10 == 0:
                print('你的身分證為', strid)
                break
