# 최대한 많은 파리를 죽이자!
# NxN 행렬에서 MxM으로 최대한 많은 수를 찾자
def kill_flies(lst, n, m):
    # MxM에 해당하는 원소들을 하나씩 추가한다
    ma = []
    # 이렇게 모인 ma의 M*M개의 원소를 모두 더한다
    total = []
    for j in range(n-m+1):
        for i in range(n-m+1):
            for a in range(j,j+m):
                for b in range(i,i+m):
                    ma.append(lst[a][b])
            total.append(sum(ma))
            ma = []
            
    return max(total)

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