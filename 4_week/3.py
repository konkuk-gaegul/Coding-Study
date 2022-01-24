# NxN 크기의 단어 퍼즐에
# 특정 길이 K를 갖는 단어가 몇 군데 들어가는지 알아보자
# 막힌 곳 : 0 , 뚫린 곳 : 1
# 한 줄에 N개의 블록이 주어질 때 1을 만나면 cnt를 하나씩 증가 시킨다
# 그 다음 cnt == K이면 합격!
T = int(input())

for tc in range(1,T+1):
    
    N, K = map(int, input().split())
    List = [list(map(int, input().split()) ) for _ in range(N)]
    ans = 0     # K글자의 총 개수
    
    # 행(i) 방향
    for j in range(N):
        cnt = 0     # 1을 만나면 하나씩 증가
        for i in range(N):
            if List[j][i] == 1:
                cnt += 1
            if List[j][i] == 0 or i == N-1:
                if cnt == K:    # cnt == K 인지 검사
                    ans += 1    # 맞다면 개수 1 증가
                cnt = 0         # 0을 중간에 만난 순간 0으로 초기화
                                # 1 0 1 0 1 방지
    # 열(j) 방향
    for i in range(N):
        cnt = 0
        for j in range(N):
            if List[j][i] == 1:
                cnt += 1
            if List[j][i] == 0 or j == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0
            
    print(f'#{tc} {ans}')