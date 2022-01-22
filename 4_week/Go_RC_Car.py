# RC카의 이동거리를 구해보자
# 매 초 아래와 같은 Command가 정수로 주어진다
# 0 : 현재 속도 유지, 1 : 가속, 2 : 감속
# 1번, 2번 Command의 경우엔 이어서 양의 정수(가속도)가 주어진다.
# N개의 Command를 모두 수행했을 때,
# N초 동안 이동한 거리를 계산해보자
T = int(input())        # Test 횟수
for tc in range(1, T+1):
    N = int(input())        # N개의 Command가 주어진다.
    speed = 0               # 초기 속도 0
    distance = 0            # 초기 이동거리 0
    
    for i in range(N):
        a = list(map(int, input().split()))     # command 입력
        
        if a[0] == 0:               # 현재 속도 유지
            distance += speed       # 현재 속도의 단위 시간 이동거리
        
        elif a[0] == 1:             # 가속의 경우
            speed = speed + a[1]    # 현재 속도에 가속도*1초 더해주기
            distance += speed       
            
        elif a[0] == 2:             # 감속의 경우
            speed = speed - a[1]    # 현재 속도에 가속도*1초 빼주기
            if speed < 0:           # 속도가 0이하, 후진하는 경우
                speed = 0           # 속도는 0으로 보정
            distance += speed
            
        
    print(f'#{tc} {distance}')