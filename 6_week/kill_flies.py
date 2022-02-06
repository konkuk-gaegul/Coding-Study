# 최대한 많은 파리를 죽이자!
# NxN 행렬에서 MxM으로 최대한 많은 수를 찾자
def kill_flies(lst, n, m):
    ma = [0]
    for j in range(n-m+1):
        for i in range(n-m+1):
            for a in range(j,j+m):
                for b in range(i,i+m):
                    ma.append(lst[a][b])
            total = sum(ma)
            ma = [0]

    return max(ma)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = kill_flies(matrix, N, M)

print(f'#{tc} {result}')
    
# 10
# 5 2 (N M)
# 1 3 3 6 7
# 8 13 9 12 8
# 4 16 11 12 6
# 2 4 1 23 2
# 9 13 4 7 3