from re import M


T = int(input())
for tc in range(1, T+1):
    
    N = int(input())
    
    #    상, 우, 하, 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    # nr : next row   , nc : next col
    # cr : current row, cc : current col