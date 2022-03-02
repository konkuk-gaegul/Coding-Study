def power(num, cnt):
    if cnt == 0:
        return 1
    else:
        return( power(num , cnt-1) * num )

print(power(2,3))
