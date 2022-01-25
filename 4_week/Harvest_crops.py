# NxN 행렬이 주어질 때 
# 규칙에 맞게 농작물 수확량을 구하라

T = int(input())
for tc in range(1, T+1):
    N = int(input())      # NxN 행렬
    List = [list(map(int, input())) for _ in range(N)]
    cnt = 0     # 현재 수확량
    
    for j in range(N):
        if j < N/2:    # 가운데 열 기준 윗 부분
            for i in range(N/2):
                
# 1 : tc
# 5 : N
# 14054
# 44250
# 02032
# 51204
# 52212