# 날짜 계산기
# 월 / 일로 주어지는 날짜를 2쌍 입력 받는다.
# 두 번째 날짜가 첫 번째 날짜의 며칠째 인지 출력하라.
import datetime

T = int(input())        # test 횟수

for tc in range(1, T+1):
    
    lists = list(map(int, input().split()))     # 4개의 수, 2쌍의 날짜 입력
    year = 2022     # 임의로 2022년 지정
    
    dt1 = datetime.datetime(year, lists[0], lists[1])   # 0번 1번 인덱스를 월/일
    dt2 = datetime.datetime(year, lists[2], lists[3])   # 2번 3번 인덱스를 월/일
    dt = (dt2 - dt1).days       # dt2와 dt1의 일 차이
    
    print( f'#{tc} {dt+1}' )    # 며칠째인지 보정
    
# T = 3
# 3 1 3 31
# 5 5 8 15
# 7 17 12 24  