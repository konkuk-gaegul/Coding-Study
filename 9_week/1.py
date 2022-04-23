# 소득 불균형
# 주어진 N개의 소득의 평균을 구한 후
# 평균 이하의 소득을 가진 사람들의 수를 출력하라
# 3 
# 7 
# 15 15 15 15 15 15 15
# 10 
# 1 1 1 1 1 1 1 1 1 100
# 7 
# 2 7 1 8 2 8 4
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    income_list = list(map(int, input().split()))
    income_mean = sum(income_list) / len(income_list)
    
    n = 0
    for i in range( N ):
        if income_list[i] <= income_mean:
            n +=1
    
    print(f'#{T} {n}')