# NxN 행렬이 주어질 때 
# 규칙에 맞게 농작물 수확량을 구하라

T = int(input())
for tc in range(1, T+1):
    N = int(input())      # NxN 행렬 N=5
    List = [list(map(int, input())) for _ in range(N)]
    cnt = 0     # 현재 수확량
    
    for j in range(N):  # j = [0,1,2,3,4]
        if j < int(N/2):
            A = List[j][ int(N/2)-j : int(N/2)+j+1 ]    # 중간 인덱스인 int(N/2)를
            cnt += sum(A)                               # 기준으로 0,1,2,...씩 넓혀진다.
            
        if j == int(N/2):   
            A = List[j]     # 중간 열은 모든 원소를 더해준다.
            cnt += sum(A)
            
        if j > int(N/2):
            A = List[j][ int(N/2)-(N-j-1) : int(N/2)+(N-j-1)+1 ]
            cnt += sum(A)
            
    print(f'#{tc} {cnt}')
                
# 1 : tc
# 5 : N
# 14054
# 44250
# 02032
# 51204
# 52212