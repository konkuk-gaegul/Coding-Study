T = 1
for tc in range(1, T+1):
    # N = int(input())    # 입력되는 문자 개수
    # K = [input().split() for i in range(1,N+1)] # A 10 / B 7 / C 5
    
    # 테스트용
    N = 3
    K = [ ['A', '10'], ['B', '7'], ['C', '5'] ]
    lst = []
    
    for j in range(N):
        lst += K[j][0] * int(K[j][1])
    
    length = len(lst)   # 문자열의 길이
    
    for k in range(1,N+1):
        lst.insert( int(k)*10 , '\n' )
    
    print(f'{lst}')