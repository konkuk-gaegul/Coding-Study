# Perfect Shuffle
# 짝수인 경우 : 한 번 씩 번갈아 가며 쌓는다
# 홀수인 경우 : 먼저 쌓은 쪽을 한 번 더 넣으면 된다
# 3
# 6
# A B C D E F
# 4
# JACK QUEEN KING ACE
# 5
# ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    suffle_off = list(input().split(' '))
    suffle_on = []
    if n % 2 == 0:
        stk_1 = suffle_off[:int(n/2)]
        stk_2 = suffle_off[int(n/2):]
    else:
        stk_1 = suffle_off[:int(n/2)+1]
        stk_2 = suffle_off[int(n/2)+1:]
        
    for i in range(len(stk_1)):
        suffle_on.append(stk_1[i])
        if n % 2 == 1 and i == int(n/2):
            break
        else:
            suffle_on.append(stk_2[i])