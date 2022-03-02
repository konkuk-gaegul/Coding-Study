# 재귀함수를 이용하여 거듭제곱을 만들어보자
# def fac(num, cnt):
#     if cnt <= 1:
#         print('1 반환')
#         return 1
#     print("%d * %d 호출" % (num, num))
#     retVal = fac(num)
    
#     print("%d * %d 반환" % (num, num, retVal))
#     return num * retVal

# print("\n5! = ", fac(2, 3))

def power(num, cnt):
    global answer
    if cnt == 0:
        print(answer)
    else :
        answer = num * num
        cnt -= 1
        power(num, cnt)
        
power(2, 3)