# 모음을 인식할 수 없는 사람은 단어를 어떻게 볼까?
# congratulation 이라는 단어를 보게 되면 “cngrtltn”
# synthetic  synthtc
# fluid      fld

T = int(input())

mo_eum = ['a', 'e', 'i', 'o', 'u']
num = 0

for tc in range(1,T+1):
    
    W = list(input())
    length = len( W )
    word = []
    
    for i in range(length):
        for j in mo_eum:
            if W[i]== j:    num += 1
            
        if num == 0:
            word.append( W[i] )
        
        num = 0
    
    words = ''.join(word)
        
    print(f'#{tc} {words}')