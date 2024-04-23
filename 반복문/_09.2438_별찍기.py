# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 방법1
n = int(input())

for i in range(n):
    for j in range(i+1):
        print('*', end='')
    if i is not n-1:
        print()


# 방법2
n = int(input())

for i in range(1, n+1):
    print("*" * i)

# 방법3
[print('*' * i) for i in range(1, int(input())+1)]