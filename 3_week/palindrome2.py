# 4글자 회문을 찾으면 된다.
# 가로 방향(i)은 0, 1, 2, 3, 4 인덱스 참조
# 따라서 첫 i의 인덱스는 0,1,2,3,4가 된다.
# 세로방향(j)는 0, 1, 2, 3, 4 인덱스 참조 후
# A에 임시 저장

for tc in range(1,11):        # 10회 테스트 반복
    N = int(input())        # N = 4글자 회문
    List = list(input() for _ in range(8))
    Answer = 0
    
    # 가로(i) 방향
    for j in range(8):
        for i in range(8-N+1):      # 4글자 회문을 찾기위해 보정
            A = List[j][i : i+N]    # i부터 (i+N-1)번 인덱스까지
            if A == A[::-1]:
                Answer += 1
                
    # 세로(j) 방향
    for i in range(8):
        for j in range(8-N+1):
            A = ''                  # j방향은 리스트가 아니라 인덱스 불가
            for k in range(N):      # 임시 저장소인 빈문자열 A 생성
                A += List[j+k][i]
            if A == A[::-1]:
                Answer += 1
    
    print(f'#{tc} {Answer}')          

# CBBCBAAB 8x8 행렬
# CCCBABCB
# CAAAACAB
# BACCCCAC
# AABCBBAC
# ACAACABC
# BCCBAABC
# ABBBCCAA