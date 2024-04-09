# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때
# (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

# 문자열
A = int(input())
B = input()

print(A * int(B[2]))
print(A * int(B[1]))
print(A * int(B[0]))
print(A * int(B))


# 문자열(반복문 O)
A = int(input())
B = input()

for i in range(3, 0, -1):
    print(A * int(B[i - 1]))

print(A * int(B))


