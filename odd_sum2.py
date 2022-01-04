T = int(input())
sum = 0

for i in range(1, T+1):

  # test 리스트 입력
  test_list = list(map(int, input().split()))
  
  
  # j = [0, 1, ... , 9]
  for j in range(len(test_list)):
      
      # j번째 요소가 홀수라면 sum과 합한다
      if test_list[j] % 2 == 1:
          sum += test_list[j]
          
print(f'#{i} {sum}')