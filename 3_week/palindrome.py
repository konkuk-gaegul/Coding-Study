T = int(input())

for i in range(1, T+1):
    lists = list(input())       # hello => 'h','e','l','l','o'
    length = len(lists)         # length = 5
    lists__ = []                # '__' 주의
    
    for j in range(length-1, -1, -1):
        lists__.append(j)
        
    if lists == lists__:
        print(1)
    else:
        print(0)