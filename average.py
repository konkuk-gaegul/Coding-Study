T = int(input())
sum = 0

for i in range(1, T+1):
    
    test_list = list(map(int, input().split()))
    
    # sum에 test_list의 요소를 하나씩 합한다
    for j in range(len(test_list)):
        sum = sum + test_list[j]
    
    # 소수점 첫 째 자리에서 반올림하여 표시
    avg = round( sum / len(test_list))
    
    print(f'#{i} {avg}')
