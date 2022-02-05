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
            
            # 3x3블럭 체크
            if j % 3 == 0 and i % 3 == 0:   # 각 블럭의 첫 원소(0, 3, 6)
                block_index = [0] * 10
                for a in range(j, j+3):
                    for b in range(i, i+3):
                        block = M[a][b]
                        if block_index[block] == False:
                            block_index[block] == 1
                        else: return 0
            
    return 1
            
T = int(input())
for tc in range(1, T+1):
    lst = [list(map(int, input().split())) for _ in range(9)]
    
    result = check(lst)
    
    print(f'#{tc} {result}')
    
# 7 3 6 4 2 9 5 8 1 
# 5 8 9 1 6 7 3 2 4 
# 2 1 4 5 8 3 6 9 7 
# 8 4 7 9 3 6 1 5 2 
# 1 5 3 8 4 2 9 7 6 
# 9 6 2 7 5 1 8 4 3 
# 4 2 1 3 9 8 7 6 5 
# 3 9 5 6 7 4 2 1 8 
# 6 7 8 2 1 5 4 3 9 