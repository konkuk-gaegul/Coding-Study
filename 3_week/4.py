T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Aj = list(map(int, input().split()))    # 1 5 3
    Bj = list(map(int, input().split()))    # 3 6 -7 5 4
    
    Cj = []         # 넣고 비교할 빈문자열
    cnt = 0         # 하나씩 더해줄 곳
    
    if N < M:
        while cnt <= (M-N):
            c = 0           # 하나씩 더해줄 곳
            for i in range(N):
                c += Aj[i]*Bj[i+cnt]
            Cj.append(c)    # Cj에 c를 하나씩 넣어준다.
            cnt += 1        # 넣어줄 때마다 카운트 +1
        print(max( Cj ))    # 이렇게 모인 c들 중에서 가장 큰 것
    else:                   # M이 N보다 작은 경우
        while cnt <= (N-M):
            c = 0
            for j in range(M):
                c += Bj[j]*Aj[j+cnt]
            Cj.append(c)
            cnt += 1
        print(max( Cj ))