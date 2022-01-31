#    우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# nr : next row   , nc : next col
# cr : current row, cc : current col

T = int(input())
for tc in range(1, T+1):
    
    N = int(input())
    
    matrix = [[0]*N for _ in range(N)]
    
    # 초기 위치
    r, c = 0, 0
    dist = 0    # 0:우, 1:하, 2:좌, 3:상
    
    for n in range(1, N*N + 1):
        matrix[r][c] = n
        r += dr[dist]   # row의 증/감
        c += dc[dist]   # col의 증/감
        
        if r < 0 or c < 0 or c == N or r == N or matrix[r][c] != 0:
            # 실행취소
            r -= dr[dist]
            c -= dc[dist]
            
            dist = (dist + 1) % 4   # 다음 방향으로 나타내기 위해 +1 보정
            
            r += dr[dist]
            c += dc[dist]
            
    print(f'#{tc}')
    # print 할 때 *을 붙여주면 [] 없이 출력된다
    for row in matrix:
        print(*row)
    print()