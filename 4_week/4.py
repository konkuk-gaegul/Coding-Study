# 주어진 문자열에서 반복되는 패턴을 찾아보자
# 몇 번 반복되는지 출력

T = int(input())
for tc in range(1, T+1):
    
    Pattern = input()
    A = Pattern[0]     # 맨 첫 글자 저장
    
    for i in range(1, len(Pattern)):     # 두 번째 글자부터 마지막까지 반복
        A += Pattern[i]                  # A에 한 글자씩 넣어주기
        length = len(A)                  
        
        if A[:int(length/2)] == A[int(length/2):]:  # 매회 A의 길이의 절반까지 슬라이스
            break                                   # 남은 절반과 일치하는지 확인
    print(f'#{tc} {int(length/2)}')                 # 일치하면 중단 후, A의 길이의
                                                    # 절반 인덱스까지 반복 패턴으로 간주
                                                    
# 3
# KOREAKOREAKOREAKOREAKOREAKOREA
# SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
# GALAXYGALAXYGALAXYGALAXYGALAXY