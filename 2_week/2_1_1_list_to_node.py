class Node():
    
    def __init__(self,d=0,p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class link_list:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

# index  0  1  2  3  4
# lst = [1, 2, 3, 4, 5]
# i in 1,2,3,4,5

def make_node(lst, arr):    # N은 수열의 길이
    first = last = Node(arr[0])
    
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new
    
    if lst.head == None:    # 새로 만드는 노드 수열
        lst.head, lst.tail = first, last
    
    else:
        current = lst.head
        
        while current != None:
            # if current.data:



# 3번의 테스트 리스트

# 5 : 수열의 길이(N) / 2 : M회 추가(M) / 5 : L번 인덱스 출력(L)
# 1 2 3 4 5
# 2 : in_dex / 7 : num_ber
# 4          / 8