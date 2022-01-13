def dfs(y, x):
    global res
    data[y][x] = 1
    for d in range(4):
        xf = dx[d] + x
        yf = dy[d] + y
        if (0 <= xf < N) and (0 <= yf < N):  # NxN 행렬
            if data[yf][xf] == 0:
              dfs(yf, xf)
            if data[yf][xf] == 3:
                res = 1
                return
            
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    data = [ list(map(int, input())) for _ in range(N) ]
    
    dx = [1, -1, 0, 0]  # 델타 검색으로
    dy = [0, 0, 1, -1]  # dx, dy를 정의한다.
    
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                x = j
                y = i
                
    res = 0
    dfs(y, x)
    
    print(f'#{tc} {res}')
    