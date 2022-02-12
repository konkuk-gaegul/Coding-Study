# 10개의 수열을 입력받아, 최대/최소 수를 제거한 나머지의 평균을 출력하라
# 3 17 1 39 8 41 2 32 99 2 
# 22 8 5 123 7 2 63 7 3 46 
# 6 63 2 3 58 76 21 33 8 1 
from calendar import c


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    
    # 내림차순으로 정렬 : 필요 없는 듯??
    # for i in range( len(lst) ):
    #     for j in range(1, len(lst)):
    #         if lst[j-1] <= lst[j]:
    #             lst[j-1], lst[j] = lst[j], lst[j-1]
    
    # 최댓값 찾기
    max_num = max( lst )
    max_length = len(lst) - lst.count( max_num )
    for i in range(max_length):
        if lst[i] == max_num:
            lst.remove(lst[i])
            lst = lst
            
    # 최솟값 찾기
    min_num = min( lst )
    min_length = len(lst) - lst.count( min_num )
    for j in range(min_length):
        if lst[j] == min_num:
            lst.remove(lst[j])
            lst = lst
    
    mean = sum( lst ) / len( lst )
    
    # :.2f => 2자리수까지, float로 표시
    print( f'#{tc} {mean:.0f}' )