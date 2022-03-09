# 비밀번호를 만들자!
# 철수는 잔머리와 게으름으로 비밀번호를 하나 설정하려한다..
# 0 ~ 9로 이루어진 문자열에서 붙어있는 쌍들을 소거하고
# 남은 번호로 비밀번호를 설정한다.
# 1238099084
# 12380'99'084
# 1238'00'84
# 123'88'4 -> 1234
T = int(input())
for tc in range(1, T+1):
    
    num = list(map(int, input()))
    
    overlap = 0
    # n = 0
    while True:
        for i in range(len(num)-1):
            if num[i] == num[i+1]:
                overlap = num[i]        # 중복된 자료 2개의 값
                if overlap == 'aaa':    # 임의로 'aaa'를 지정
                    break
    
        if overlap != 'aaa':
            for _ in range(2):  # 중복된 값을 2번 제거해야한다
                num.remove(overlap)
            overlap = 'aaa'     # 중복된 값을 제거한 뒤, 다시 'aaa'
        