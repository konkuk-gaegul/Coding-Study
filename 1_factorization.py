T = int(input())

for i in range(1, T+1):
    
    # a부터 e까지 0 입력
    a, b, c, d, e = 0,0,0,0,0

    N = int(input())
    
    # 입력된 N을 2, 3, 5, 7, 11로 나누어
    # 나머지가 0이 될 때만 실행
    # 나누어질 때마다 카운트 증가
    while N % 2 == 0:
        a += 1
        N = N // 2
        
    while N % 3 == 0:
        b += 1
        N = N // 3
        
    while N % 5 == 0:
        c += 1
        N = N // 5
        
    while N % 7 == 0:
        d += 1
        N = N // 7
        
    while N % 11 == 0:
        e += 1
        N = N // 11
        
    print(f'#{i} {a} {b} {c} {d} {e}')
    
    