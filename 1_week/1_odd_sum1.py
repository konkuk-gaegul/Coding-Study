T = int(input())

for i in range(1, T+1):

  # test 리스트 입력
  test_list = list(map(int, input().split()))

  # list comprehension을 이용해 홀수만 리스트에 넣는다
  odd_num = [j for j in test_list if j % 2 == 1]

  # sum 명령어를 통해 리스트 요소를 전부 합한다.
  print(f'#{i} {sum(odd_num)}')