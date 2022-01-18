# A회사는 P원/1L
# B회사는 R리터 이하인 경우 기본요금 Q원
#              이상인 경우 초과량에 대해 리터당 S원
# 사용량 W
# P   Q   R   S   W
# 9  100  20  3   10
T = int(input())

for i in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    
    if W <= R:
        A = P*W
        B = Q
    else:
        A = P*W
        B = R + (W-R)*S
    
    if A > B:
        cheaper = B
    elif A < B:
        cheaper = A
        
    print(f'#{i} {cheaper}')