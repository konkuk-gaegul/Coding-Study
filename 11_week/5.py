# 아래와 같이 숫자를 세는 외계 행성이 있다.
# 그들의 언어로 리스트가 주어졌을 때
# 오름차순으로 각 숫자가 몇 번 나왔는지 출력하시오
word = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for tc in range(1, T+1):
    lst = list(input().split())         # 입력 리스트
    output = []                         # 각 숫자를 반복된 횟수만큼 저장
    for j in range(10):
        num_cnt = lst.count(word[j])    # 각 숫자가 몇 번 나왔는지 확인
        itr = 0                         # 반복 횟수가 num_cnt와 같으면 while문 종료
        while itr != num_cnt:
            itr += 1                    # itr 1씩 증가
            output.append(word[j])
    
    # , & ''를 제외하고 출력한다.
    print(' '.join(output))