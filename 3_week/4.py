T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Aj = list(map(int, input().split()))    # 1 5 3
    Bj = list(map(int, input().split()))    # 3 6 -7 5 4
    a = len(Aj)     # Aj의 길이
    b = len(Bj)     # Bj의 길이
    Cj = []         # 넣고 비교할 빈문자열
    cnt = 0
    
    if a < b:
        while cnt <= (a-b):
            c = 0           # 하나씩 더해줄 곳
            for i in range(a):
                c += Aj[i]*Bj[i+cnt]
            Cj.append(c)
            cnt += 1
        print(max( Cj ))
    # else:
    #     while a >= b: