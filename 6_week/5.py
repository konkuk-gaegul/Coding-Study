# 입력되는 100x100 배열에서
# 각 행, 열, 대각의 합 중
# 가장 큰 값을 출력하라!

for tc in range(1):
    # T = int(input())
    T = 1
    
    # 연습삼아 3x3
    N = 3
    matrix = [list(map(int, input().split())) for _ in range(N)]
    A = []
    c = []
    d = []
    # 행의 합
    for j in range(N):
        a = sum(matrix[j])
        A.append( a )
        
    # 열의 합
    for i in range(N):
        col = 0
        b = []
        for j in range(N):
            b.append(matrix[j][i])
        col = sum(b)
        A.append( col )
        
    # # 좌상->우하 대각
    # for j in range(N):
    #     for i in range(j,j+1):
    #         c.append(matrix[j][i])
    # A.append(sum(c))
    
    # # 우상->좌하 대각
    # for j in range(N):
    #     for i in range(-(j+1),-(j+2),-1):
    #         d.append(matrix[j][i])
    # A.append(sum(d))
    
    # D = max(A)
    
print(f'#{T} {A}')