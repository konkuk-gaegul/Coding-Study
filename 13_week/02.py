# 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV2b-QGqADMBBASw&categoryId=AV2b-QGqADMBBASw&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

# 점 (x,y)에 할당된 수는 #(x,y)로 나타낸다.
# 예를 들어 #(1,1) = 1, #(2,1)=3, #(2,2) = 5, #(4,4) = 25이다.
# 반대로 수 p가 할당된 점을 &(p)로 나타낸다.
# 예를 들어 &(1) = (1,1), &(3) = (2,1), &(5) = (2,2), &(25) = (4,4)이다.
# 두 점에 대해서 덧셈을 정의한다. 점 (x,y)와 점 (z,w)를 더하면 점 (x+z, y+w)가 된다.
# 즉, (x,y) + (z,w) = (x+z, y+w)로 정의한다.
# 우리가 해야 할 일은 수와 수에 대한 새로운 연산 ★를 구현하는 것으로, p★q는 #(&(p)+&(q))으로 나타난다.
# 예를 들어, &(1)=(1,1), &(5) = (2,2)이므로, 1★5 = #(&(1)+&(5)) = #((1,1)+(2,2)) = #(3,3) = 13이 된다.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 정수 p,q(1 ≤ p, q ≤ 10,000)가 주어진다.

# [출력]
# 각 테스트 케이스마다 ‘#t’(t는 테스트 케이스 번호를 의미하며 1부터 시작한다)를
# 출력하고, 각 테스트 케이스마다 p★q의 값을 출력한다.
# ----------
# (1,1) = 1
# ----------
# (1,2) = 2
# (2,1) = 3
# ----------
# (1,3) = 4
# (2,2) = 5
# (3,1) = 6
# ----------
# (1,4) = 7
# (2,3) = 8
# (3,2) = 9
# (4,1) = 10
# ----------
# # T = int(input())
for test_case in range(1, 2):
    cordinate = [ ['x','y','j'] ]
    i = 1   # 현재 x, y좌표의 최대값
    j = 1   # 현재 좌표에 할당된 번호
    max_num = 1
    while j < 7:
        # x, y좌표
        X, Y = range(1, i+1), range(i, 0, -1)
        for k in range(i):
            cordinate.append( [ X[k] , Y[k] , j ] )
            j += 1
            if k == i-1:
                i += 1
    print(cordinate)