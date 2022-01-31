# 숫자 배열 회전
# NxN 행렬이 주어질 때
# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [ list( map(int , input().split() )) for _ in range(N) ]
    
    for i in range(0,N):
        for j in range(1-N,1):
            matrix_90 = matrix[j][i]
            
    print(f'{matrix_90}')