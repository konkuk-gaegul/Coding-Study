# 백만 장자 프로젝트
# 다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.
#     1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
#     2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
#     3. 판매는 얼마든지 할 수 있다.
# 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에
# 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.
import itertools
T = int(input())

for tc in range(1, T+1):
    days = int(input())
    lst = list(map(int, input().split()))
    
    money = [ 0 for _ in range( days**2 ) ]
    sale = []
    n = [0, -1]   # 0 : 미구매, -1 : 구매
    pro = list(itertools.product(n, repeat = days))
    
    for i in range( days**2 ):
        wallet = 0  # 각 경우의 수의 내 지갑
        pur_num = 0
        for j in range( days ):
            wallet += lst[j] * pro[i][j]        
            if pro[i][j] != 0: pur_num += 1
        
        money[i] = wallet    # (지출, 구매횟수)로 입력
        sale.append( pur_num * lst[-1] + money[i] )
    print(f'#{tc} {max(sale)}')