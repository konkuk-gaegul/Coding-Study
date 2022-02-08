# 입력되는 100x100 배열에서
# 각 행, 열, 대각의 합 중
# 가장 큰 값을 출력하라!

for tc in range(10):
    # T = int(input())
    T = 1
    # 연습삼아 5x5
    N = 5
    matrix = [list(map(int, input().split())) for _ in range(N)]
    a = []  # a에 각 행/열의 총 합을 넣음
    
    for j in range(N):
        a = sum(matrix[j])
    
    
print(f'#{T} {a}')