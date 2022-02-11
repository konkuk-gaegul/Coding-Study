# 원본 문서는 너비가 10인 여러 줄의 문자열로 이루어져 있다.
# 압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 만들자
T = 1
for tc in range(1, T+1):
    # 입력되는 문자 개수
    N = int(input())
    
    # A 10 / B 7 / C 5
    K = [input().split() for i in range(1,N+1)]
    
    lst = []            # 압축된 파일의 문자를 하나씩 리스트화
    original_doc = ''   # 원본 문서로 나타낼 문자열
    
    
    for j in range(N):
        lst += K[j][0] * int(K[j][1]) # lst = ['A', 'A', ..., 'C', 'C']
    
    for k in range(len(lst)):
        original_doc += lst[k][0]     # original_doc = 'AA...CC'
        
        for l in range(1, N+1):
            # 한 줄당 10개의 문자만 표현하고 줄바꿈해준다.
            if len(original_doc) == 10*l + (l-1) : # 줄바꿈하느라 \n을 추가하면
                original_doc += '\n'               # 인덱스가 하나씩 밀려서 보정!
    
    print(f'{original_doc}')