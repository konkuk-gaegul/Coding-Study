# 주어지는 수와 제곱근이 둘 다 
# palindrome인 수는 몇 개인가?
# 3개 테스트 케이스
# 이상 이하
# 1     9       3
# 10    99      0
# 100   1000    2
import math
T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    
    n = 0
    # i는 1이상 9이하
    for num in range(A, B+1):
        # num과 sqrt(num) 정의
        num_sqrt = math.sqrt(num)
        
        # num과 sqrt(num)을 하나 하나 리스트화 함
        num_list = list(str(num))
        num_sqrt_list = list(str(num_sqrt))
        
        if num_sqrt_list[-1] == '0':
            num_sqrt_list = list(str(int(num_sqrt)))
        # 슬라이스를 이용하여 거꾸로 출력
        num_inv = num_list[-1::-1]
        num_sqrt_inv = num_sqrt_list[-1::-1]
        
        if num_list == num_inv and num_sqrt_list == num_sqrt_inv :
            n += 1
    
    print(f'#{tc} {n}')