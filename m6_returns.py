def sum_avg(a,b):
    total = 0
    for i in range(a,b+1):
        total+=i
    avg = total/(b-a+1)
    return total,avg

def main():
    total,avg = sum_avg(1,30)
    print('sum={},avg={}'.format(total,avg))
main()