# RC카의 이동거리를 구해보자
# 매 초 아래와 같은 Command가 정수로 주어진다
# 0 : 현재 속도 유지, 1 : 가속, 2 : 감속
# 1번, 2번 Command의 경우엔 이어서 양의 정수(가속도)가 주어진다.
# N개의 Command를 모두 수행했을 때,
# N초 동안 이동한 거리를 계산해보자
T = int(input())        # Test 횟수
for tc in range(1, T+1):
    N = int(input())        # N개의 Command가 주어진다.
    speed = 0
    distance = 0
    
    for i in range(N):
        a = list(map(int, input().split()))
        
        if a[0] == 0:
            distance += speed
        
        elif a[0] == 1:
            speed = speed + a[1]
            distance += speed
            
        elif a[0] == 2:
            speed = speed - a[1]
            if speed < 0:
                speed = 0
            distance += speed
            
        
    print(f'#{tc} {distance}')