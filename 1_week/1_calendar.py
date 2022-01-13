T = int(input())

for i in range(1, T+1):
    
    test_date = input()
    
    # 연도는 index 0번부터 3번까지
    year = int(test_date[:4])
    
    # 월은 index 4번부터 5번까지
    month = int(test_date[4:6])
    
    # 일은 index 6번부터 끝까지
    day = int(test_date[6:])
    
    # 00월 또는 13월 이상 제거
    if month < 1 or month > 12:
        print('-1')
    
    # 해당 월에 맞는 조건
    if month == 2:
        if day > 28 or day < 1:
            print('-1')
            
    if month == [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            print('-1')
            
    if month == [4, 6, 9, 11]:
        if day < 1 or day > 30:
            print('-1')
            
    print(f'#{i}', end = ' ')
    print('%04d/%02d/%02d'%(year, month, day))
    