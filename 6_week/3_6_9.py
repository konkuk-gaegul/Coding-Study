# N = int(input())    # N=10
N = 33
# lst = range(1,N+1)  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
num = [0]*N
for i in range(1,N+1):
    
    a = list(str(i))    # 문자열로 변환 후, 각 자릿수 분리
    b = 0               # 해당 숫자에 3 or 6 or 9의 개수 만큼 증가
    
    for j in range(len(a)):
        if a[j] == str(3) or a[j] == str(6) or a[j] == str(9):
            b += 1
        else:
            num[i-1] = i
        
        # 흠..이걸 어떻게 처리해야할까..
        if a[j] == str(3) or a[j] == str(6) or a[j] == str(9):
            num[i-1] = '-'*b
        
print(num)
