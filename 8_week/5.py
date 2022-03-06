# 암호 생성기
# 숫자 배열이 주어진다.
# 10 6 12 8 9 4 1 3
# 첫 인덱스부터 5개를 대상으로 한 번씩
# 1, 2, ..., 5 씩 감소시키고 맨 뒤로 이동시킨다. (1 사이클)
# 0 또는 0보다 작아지는 순간의 숫자 배열이 암호가 된다.
T = int(input())
for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    # num_list = [10, 6, 12, 8, 9, 4, 1, 3]
    n = 1
    while True:
        if n == 6: n = 1
        
        num_temp = num_list[0] - n
                
        if num_temp <= 0:
            num_temp = 0
                
        num_list.remove( num_list[0] )
        num_list.append(num_temp)
        n += 1
        if num_list[-1] == 0: break
    print(f'#{tc} {num_list}')