# 함수
class Node():
    
    def __init__(self):
        self.data = None
        self.link = None

def Node_1(a, my_li):
    
    node1 = Node()
    node1.data = my_li[0]

# 전역변수
T = int(input())

# 메인
for i in range(1, T+1):
    
    N, M, L = map(list, input().split())  
    li_st = map(list, input().split())
    memory = []
    head, current, pre = None, None, None
    
    for _ in range(M):
        
        in_dex, num_ber = map(int, input().split())   #in_dex 번 인덱스에 num_ber 추가
        newNode = Node()
        newNode.data = 
        

# 3번의 테스트 리스트

# 5 : 수열의 길이(N) / 2 : M회 추가(M) / 5 : L번 인덱스 출력(L)
# 1 2 3 4 5
# 2 : in_dex / 7 : num_ber
# 4 8

# 5 5 4
# 13787 32221 32402 32498 4169
# 3 5902
# 3 9752
# 3 27737
# 1 14133
# 0 16547

# 10 10 8
# 16243 26767 22174 25277 17456 13398 29850 22297 1382 31246
# 9 23198
# 7 17514
# 11 24247
# 0 25306
# 2 9104
# 6 28112
# 12 7491
# 10 26972
# 17 22639
# 12 28722