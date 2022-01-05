T = int(input())
P = 0

for i in range(1, T+1):
    
    N = int(input())
    
    while N > 0:
        
        if N % 2 == 1:
            P += N
            
        else :
            P -= N
            
        N -= 1
        
    print(f'#{i} {P}')