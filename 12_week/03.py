# ‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다.
# 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.
# 예를 들어, “bdppq”를 거울에 비추면 “pqqbd”처럼 나타날 것이다.
# 2 : 테스트 케이스 수
# bdppq
# qqqqpppbbd
T = int(input())

str_dic = {'b' : 'd',
           'd' : 'b',
           'p' : 'q',
           'q' : 'p'}

keys   = list(str_dic.keys())
values = list(str_dic.values())


for tc in range(1, T+1):
    test_case = list(input())
    temp = []
    
    # val = 0
    for i in range(len(test_case)):
        
        idx = keys.index( test_case[i] )    # test_case의 현재 문자의 인덱스
        temp.append( values[idx] )          # 위 인덱스에 맞는 value (d -> d)
            
        mirrored_case = temp[-1::-1]        # 거꾸로 뒤집기
        
        
    print('#',tc, ' ',*mirrored_case, sep = '')