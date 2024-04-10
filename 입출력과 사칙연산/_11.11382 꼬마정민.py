# 꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!

# 방법1
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a + b + c)

# 방법2
a, b, c = map(int, input().split())
print(a+b+c)

# 방법3
ls = list(map(int, input().split()))
print(sum(ls))

# 방법4
print(sum(list(map(int, input().split()))))