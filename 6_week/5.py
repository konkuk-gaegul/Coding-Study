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
    # 행의 합
    for j in range(N):
        a = matrix[j]
        A.append(sum(a))
        
    # 열의 합
    for i in range(N):
        b = matrix[j]
        A.append(sum(b))
        
    # 대각 합
    for j in range(N):
        for i in range(j):
            c.append(matrix[j][i])
        A.append(sum(c))
        
    D = max(A, B, C)
    
print(f'#{T} {D}')