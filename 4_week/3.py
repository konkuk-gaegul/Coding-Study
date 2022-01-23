# NxN 크기의 단어 퍼즐에
# 특정 길이 K를 갖는 단어가
# 몇 군데 들어가는지 알아보자
# 막힌 곳 : 0 , 뚫린 곳 : 1
# 한 줄에 N개의 블록이 주어질 때
# N-K 번 인덱스까지만 참조해보자
T = int(input())

for tc in range(1,T+1):
    
    N, K = map(int, input().split())
    List = list(map(int, input().split()) for _ in range(N))
    cnt = 0
    B = []
    
    # 가로(i) 방향
    for j in range(N):
        for i in range(N-K+1):
            
            if List[j][i] == 1 and List[j][i+1] == 1 and List[j][i+2] == 1:
                cnt += 1
    # 세로(j) 방향
    for i in range(N):
        for j in range(N-K+1):
            if List[j][i] == 1 and List[j+1][i] == 1 and List[j+2][i] == 1:
                cnt += 1
                
    print( f'#{tc} {cnt}' )