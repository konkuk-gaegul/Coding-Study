# ‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다.
# 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.
# 예를 들어, “bdppq”를 거울에 비추면 “pqqbd”처럼 나타날 것이다.
# 2 : 테스트 케이스 수
# bdppq
# qqqqpppbbd
T = int(input())
test_case = list(input())

str_dic = {'b' : 'd',
           'd' : 'b',
           'p' : 'q',
           'q' : 'p'}
keys   = list(str_dic.keys())
values = list(str_dic.values())


for tc in range(1, T+1):
    
    temp = test_case
    val = 0
    for key in keys:
        temp[temp == key] = values[val]
        val += 1
    
    mirrored_case = temp[-1::-1]
    

print(f'#{tc} {mirrored_case}')