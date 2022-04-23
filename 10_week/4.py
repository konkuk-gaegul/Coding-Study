# 직사각형의 변의 길이 찾기
# 네 변 중, 세 변만 제공한다.
# 3
# 1 1 2
# 4 3 4
# 5 5 5
T = int(input())
for tc in range(1, T+1):
    itr = []
    rec = list(map(int, input().split()))
    
    for i in range(3):
        itr.append( rec.count(rec[i]) )
    
    if 1 in itr:
        # print(f'한 번만 나온 수는 {rec[itr.index(1)]}')
        print(f'#{tc} {rec[itr.index(1)]}')
        
    if 3 in itr:
        print(f'#{tc} {rec[1]}')