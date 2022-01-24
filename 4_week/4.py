# 주어진 문자열에서 반복되는 패턴을 찾아보자
# 몇 번 반복되는지 출력

T = int(input())
for tc in range(1, T+1):
    
    Pattern = input()
    A = Pattern[0]     # 맨 첫 글자 저장
    
    for i in range(1, len(Pattern)):     # 두 번째 글자부터 마지막까지 반복
        A += Pattern[i]
        length = len(A)
        
        if A[0:(length/2)] == A[(length/2):]:
            
# 3
# KOREAKOREAKOREAKOREAKOREAKOREA
# SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
# GALAXYGALAXYGALAXYGALAXYGALAXY