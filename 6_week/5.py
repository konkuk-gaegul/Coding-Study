# 입력되는 100x100 배열에서
# 각 행, 열, 대각의 합 중
# 가장 큰 값을 출력하라!
for tc in range(1):
    T = int(input())
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]
    total = []  # 각 행/열/대각의 합을 나열
    c = []  # 좌상->우하 대각
    d = []  # 우상->좌하 대각
    
    # 행의 합
    for j in range(N):
        a = sum(matrix[j])
        total.append( a )
        
    # 열의 합
    for i in range(N):
        col = 0
        b = []
        for j in range(N):
            b.append(matrix[j][i])
        col = sum(b)
        total.append( col )
        
    # 좌상->우하 대각
    diag_1 = 0  # 원소 하나씩 더하는 방법
    for j in range(N):
        for i in range(j,j+1):
            diag_1 += matrix[j][i]
    
    # 우상->좌하 대각
    for j in range(N):
        for i in range(-(j+1),-(j+2),-1):
            d.append(matrix[j][i])
    total.append(sum(d))
    
print(f'# {max(total)}')