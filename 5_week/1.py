# 숫자 배열 회전
# NxN 행렬이 주어질 때
# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.
T = int(input())
for tc in range(1,T+1):
    N = int(input())    # NxN행렬
    matrix = [ list( map(int , input().split()) ) for _ in range(N) ]
    
    mat_90 = [ [0 for _ in range(3)] for _ in range(3)]     # 0행렬 생성
    mat_180 = [ [0 for _ in range(3)] for _ in range(3)]    # 0행렬 생성
    mat_270 = [ [0 for _ in range(3)] for _ in range(3)]    # 0행렬 생성
    
    for i in range(N):
        for j in range(N):
            mat_90[i][j] = matrix[N-j-1][i]
    
    for i in range(N):
        for j in range(N):
            mat_180[i][j] = mat_90[N-j-1][i]
    
    for i in range(N):
        for j in range(N):
            mat_270[i][j] = mat_180[N-j-1][i]
    
    print(f'{mat_90} {mat_180} {mat_270}')