# 시각 덧셈
# 시/분으로 이루어진 시각을 2개 입력 받아
# 더한 값을 시/분으로 출력하는 프로그램
# 12시간제로 표현한다.
T = int(input())
for tc in range(1,T+1):
    hour_min = list( map( int, input().split() ) )
    length = len(hour_min)
    
    hour = hour_min[0] + hour_min[2]
    min = hour_min[1] + hour_min[3]
    
    if min >= 60:
        hour += 1
        min = min - 60
        
    if hour  > 12:
        hour -= 12
        
    print(f'#{tc} {hour} {min}')