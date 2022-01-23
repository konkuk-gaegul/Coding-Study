# NxN 크기의 단어 퍼즐에
# 특정 길이 K를 갖는 단어가
# 몇 군데 들어가는지 알아보자
# 막힌 곳 : 0 , 뚫린 곳 : 1
# 한 줄에 N개의 블록이 주어질 때
# N-K 번 인덱스까지만 참조해보자
T = int(input())

for tc in range(1,T+1):
    
    N, K = map(int, input().split())
    List = list(input().split() for _ in range(N))
    