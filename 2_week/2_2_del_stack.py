# 함수
def del_stack( A ):
    
    top = -1
    
    for i in range( len(A) ):
        top += 1                # top=0 에서 시작
        stack.append( A[i] )    # 0번 인덱스에 A[i]추가
          
        if top > 0 and stack[top] == stack[top - 1]:
            # top=0인 경우 13행의 top-1에서 오류를 보정하기 위함
            
            stack.pop(top)      # 이번 루프에서 추가한 것
            stack.pop(top-1)    # 이전 루프에서 추가한 것
            top -= 2            # 2개를 제거한 만큼 보정
    
# 전역변수
T = int(input())

# 메인
for i in range(1, T+1):
    N = input()
    stack = []
    
    del_stack(N)
    print(f'#{i} {len(stack)}')
    
# ABCCB
# NNNASBBSNV
# UKJWHGGHNFTCRRCTWLALX