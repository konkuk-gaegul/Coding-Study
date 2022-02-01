# 크기가 N인 파스칼의 삼각형을 만들어보자
# 첫째 줄은 항상 1이며, 첫 인덱스와 마지막 인덱스는 1이다.
# 그 안쪽은 행의 인덱스를 따라간다.
N = int(input())
matrix = [ [0] * N for _ in range(N) ]

for i in range(N):
    for j in range(i+1):
        if j == 0 or j == i:    # 가장 끝 값은 1이다
            matrix[i][j] = 1
        else:
            matrix[i][j] = matrix[i-1][j] + matrix[i-1][j-1]    # 오른쪽 위 + 왼쪽 위
            
for row in matrix:
    result = [x for x in row if x]  # matrix의 row 중에서 True인 값들을 넣는다.
    print(*result)