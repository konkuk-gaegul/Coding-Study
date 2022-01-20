# 4글자 회문을 찾으면 된다.
# 가로 방향(i)은 0~3, 1~4, 2~5, 3~6,4~7 인덱스 참조
# 따라서 첫 i의 인덱스는 0,1,2,3,4가 된다.
# 세로방향(j)는 0~7의 모든 인덱스 참조

for tc in range(10):        # 10회 반복
    N = int(input())        # N = 4글자 회문
    List = list(input() for _ in range(8))
    Answer = 0
    
    # 가로 확인
    for j in range(0,8):
        for i in range(0,8-N+1):
            A = List[j][i : i+N]
            if A == A[::-1]:
                Answer += 1
                
    # 세로 확인
    for j in range(0,8-N+1):
        for i in range(0,8):
            A = ''              # j방향은 리스트가 아니라 인덱스 불가
            for k in range(N):
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