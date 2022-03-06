# 암호 생성기
# 숫자 배열이 주어진다.
# 10 6 12 8 9 4 1 3
# 첫 인덱스부터 5개를 대상으로 한 번씩
# 1, 2, ..., 5 씩 감소시키고 맨 뒤로 이동시킨다. (1 사이클)
# 0 또는 0보다 작아지는 순간의 숫자 배열이 암호가 된다.
T = int(input())
for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    
    n = 1
    while num_list[-1] != 0:
        if n == 6: n = 1    # 계속 1씩 증가하는 n을 6이되면 1로 되돌려준다.
        
        num_temp = num_list[0] - n
                
        if num_temp <= 0:   # n을 뺐는데, 0또는 그 이하가 되면
            num_temp = 0    # 0으로 변환
                
        num_list.remove( num_list[0] )  # 첫 인덱스를 제거 후,
        num_list.append(num_temp)       # 마지막 인덱스로 보낸다.
        n += 1  # while문에 의해 n은 계속 1씩 증가
            
    print(f'#{tc} {num_list}')

# test case
# 9550 9556 9550 9553 9558 9551 9551 9551
# 6 2 2 9 4 1 3 0
# 2419 2418 2423 2415 2422 2419 2420 2415
# 9 7 9 5 4 3 8 0