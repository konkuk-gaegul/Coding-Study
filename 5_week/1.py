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
        for j in range(N):                  # 입력한 matrix의 j = 2 -> 1 -> 0
            mat_90[i][j] = matrix[N-j-1][i] # 패턴 파악 후, 행/열 순서대로 입력
            
    # mat_90을 90도 돌린다
    for i in range(N):
        for j in range(N):
            mat_180[i][j] = mat_90[N-j-1][i]
            
    # mat_180을 90도 돌린다
    for i in range(N):
        for j in range(N):
            mat_270[i][j] = mat_180[N-j-1][i]
    
    print(f'#{tc}')
    # 각 행렬의 한 행씩 띄어쓰기를 구분으로 출력
    for i in range(N):
        for a in range(N):
            print(mat_90[i][a], end = '') # 행의 요소들을 연이어서 출력
        print(end=' ')
        
        for b in range(N):
            print(mat_180[i][b], end = '')
        print(end=' ')
        
        for c in range(N):
            print(mat_270[i][c], end = '')
        print() # 줄 바꿈