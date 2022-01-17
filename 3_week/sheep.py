T = int(input())

for t in range(1, T+1):
    N = int(input())
    x = 0                           # x*N에 사용
    A = [False for _ in range(10)]  # 빈 문자열, 여기에 xN을 쪼개서 하나씩 더할 예정
    y = 0                           # True가 될 때 마다 1씩 증가
    
    while y != 10 :
        x += 1
        sheep = str(x*N)
        
        for i in sheep:
            if A[int(i)] == False:

              A[int(i)] = True
              y += 1

    print( f'#{t} {int(sheep)}' )
    
# 5 (T)
# 1 (N)
# 2
# 11
# 1295
# 1692