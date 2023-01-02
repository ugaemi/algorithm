x = int(input())
stick = 64

while stick > 0:
    if stick == x:
        print(1)
        break
    if stick > x:
        stick >>= 1
    else:
        answer = 1
        tmp = [stick]
        stick >>= 1
        while stick > 0:
            if (sum(tmp) + stick) <= x:
                tmp.append(stick)
            if sum(tmp) == stick:
                break
            stick >>= 1
        print(len(tmp))
