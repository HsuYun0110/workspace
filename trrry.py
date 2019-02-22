while True:
    try :
        num= int(input('請輸入整數0-100:'))
        if num>0 and num<100:
            print('{} is {}'.format(num,'奇數' if num%2!=0 else '偶數'))
            break
        else:
            raise IndexError
    except ValueError:
        print('please input a number ')
    except IndexError:
        print('out of range')
    finally:
        print('haha')