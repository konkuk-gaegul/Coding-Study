def check(M):
    for j in range(9):   # 열 방향
        row_index = [0] * 10
        col_index = [0] * 10
        for i in range(9):  # 행 방향
            
            # i방향 체크
            row = M[j][i]
            if row_index[row] == False:
                row_index[row] = 1
            else: return 0
                
            # j방향 체크
            col = M[i][j]
            if col_index[col] == False:
                col_index[col] == 1
            else: return 0
            
    return 1
            
T = int(input())
for tc in range(1, T+1):
    lst = [list(map(int, input().split())) for _ in range(9)]
    
    result = check(lst)
    
    print(f'#{tc} {result}')