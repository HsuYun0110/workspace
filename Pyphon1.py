times = 0
lasttwo = 0
lastone = 0
while times < 10:
    if times == 0:
        lasttwo = 0
        ans = 0
    elif times == 1:
        lastone = 1
        ans = 1
    else:
        ans = lastone+lasttwo
        lasttwo = lastone
        lastone=ans
    print("第", times + 1, "項:", ans)
    times = times + 1