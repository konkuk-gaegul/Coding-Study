# 알파벳 소문자 만으로 이루어진 문자열이 주어진다.
# 이 문자열에서 같은 두 문자들을 짝짓고 남는 문자가 무엇인지 구하는 프로그램을 작성하라.
# 같은 문자를 여러 번 짝지어서는 안 된다.

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 알파벳 소문자 만으로 이루어진 문자열이 주어진다.
# 이 문자열의 길이는 1이상 100이하이다.

# 각 테스트 케이스 마다 남는 문자를 사전 순서대로 출력한다.
# 어떤 문자도 남지 않는다면 “Good”을 출력하도록 한다.

# xxyyzz
# yc
# aaaab
# bca
# ppzqq
# qnwerrewmq

T = int(input())
for test_case in range(1, T+1):
    
    lst = list(input())
    
    # 현재 인덱스 : 연속된 두 문자를 삭제하면 유지, 그대로면 1증가
    i = 0
    print(lst)
    while i < len(lst):
        # 연속된 두 문자가 다른 경우
        if lst[i] != lst[i+1]:
            i += 1
        # 연속된 두 문자가 같은 경우
        else:
            del lst[i:2]
            i =  i
    result = lst
    # 아무것도 남지 않은 경우 'Good'출력
    if len(result) == 0:
        result = 'Good'
    else:
        # 사전 순으로 정렬 (오름차순)
        print(result.sort())