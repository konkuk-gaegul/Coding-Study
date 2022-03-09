# 원재가 또...!!
# 이진 비트로 이루어진 수를 다시 비밀번호 형태로 바꿀 예정이다
# n번째 비트를 다른 수(0->1 or 1->0)로 바꾸면
# n+1번째부터 끝 수 까지 전부 같이 변환된다
# 이떄, 수정되어 변환하는 횟수를 구하여라
# 2
# 0011
# 100
T = int(input())
for tc in range(1, T+1):
    # 비밀번호 초기 값 : 타겟
    bit_init = list( input() )
    # 비밀번호 시작 값
    bit_orig = [ 0 for _ in range(len(bit_init))] 
    # 수정 횟수 : 비트가 변환되면 1씩 증가
    n = 0
    
    for i in range(len(bit_init)):
        if bit_init[i] == str(0): 
            n += 1  # 0->1 변환에 의해 증가
            for j in range( i, len(bit_init) ): # range안에 i로 시작하게끔 보정
                bit_orig[j] = 0
                
        else:
            n += 1  # 1->0 변환에 의해 증가
            for j in range( i, len(bit_init) ): # range안에 i로 시작하게끔 보정
                bit_orig[j] = 1
    
    # 첫 시작이 0이면 변환할 필요가 없지만, n은 증가한다.
    # 따라서 첫 1이 몇 번째 인덱스에서 나오는지 알아야한다.
    # 첫 1이 나오기 전 0은 모두 횟수 n에서 빼준다.
    one_idx = bit_init.index('1')
    # 수정된 횟수이기 때문에 -1로 보정해준다.
    print(f'#{tc} {n-one_idx-1}')