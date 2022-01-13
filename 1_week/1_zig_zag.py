T = int(input())

for i in range(1, T+1):
    
    N = int(input())
    SUM = 0
    while N > 0:
        
        if N % 2 == 1:
            SUM += N
        else :
            SUM -= N
        N -= 1
        
    print(f'#{i} {SUM}')