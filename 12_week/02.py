# 은비는 빵을 좋아한다.
# 현미 빵은 A원, 단호박 빵은 B원, 은비는 C원을 가지고 있다
# 빵 종류에 상관없이 많은 빵을 원한다. (배가 많이 고파보인다)
# 최대 몇 개의 빵을 살 수 있을까??
# 2 : tc의 개수
# 3 5 6  : A B C
# 6 8 20 : A B C
T = int(input())
for test_case in range(T):
    tc = list(map(int, input().split()))
    # 은비가 가진 C원으로 각 빵만 최대 몆 개 살 수 있는지
    a = tc[2] // tc[0]
    b = tc[2] // tc[1]
    # 예산을 만족하는 경우의 수를 cnt에 각각 저장
    cnt = []
    for i in range(0, a+1):
        for j in range(0, b+1):
            # A*i + B*j <= C 라면, 빵의 개수는 a+b가 된다.
            if tc[0]*i + tc[1]*j <= tc[2]:
                cnt.append(i + j)

    print(f'#{test_case + 1} {max(cnt)}')
                