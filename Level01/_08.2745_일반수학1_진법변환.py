# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35



# 1. 이론적인 방법
N, B = input().split()
ls = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = N[::-1]
b = int(B)
answer = 0
for index, num in enumerate(a):
   answer += (ls.index(num)*(b**index))

print(answer)


# 2.
# N, B = input().split()
# B = int(B)
# result = 0
#
# for i, j in enumerate(N):
#     try:
#         if int(j):
#             result += int(j) * B ** (len(N) - i - 1)
#     except:
#         result += (ord(j) - 55) * B ** (len(N) - i - 1)
#
# print(result)




# 4. int 함수 사용, 36진법 변환 가장 쉬움
n,b=input().split()
print(int(n,int(b)))


