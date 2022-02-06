# N = int(input())    # N=10
N = 13
# lst = range(1,N+1)  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
num = []
for i in range(1,N+1):
    
    a = list(str(i))    # 문자열로 변환 후, 각 자릿수 분리
    # print(a)
    b = 0
    for j in range(len(a)):
        
        
        if a[j] == str(3) or a[j] == str(6) or a[j] == str(9):
            b += 1
        
        num.append('-'*b)
    
    print(num, end=' ')