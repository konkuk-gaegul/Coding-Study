# N원을 받았을 때, 거스름돈을 계산해보자

T = int(input())
# a, b, c, d, e, f, g, h
A = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
B = [0]*8   # 각 지폐 및 동전의 개수
for tc in range(1,T+1):
    N = int(input())
    
    for i in range(len(A)):
        a = N // A[i]   # a는 몫
        B[i] = a
        N = N % A[i]  # N에는 나머지를 다시 할당
        
    print(*B)   # 괄호와 컴마 없이 출력