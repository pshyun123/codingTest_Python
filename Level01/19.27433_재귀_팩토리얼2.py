# 0보다 크거나 같은 정수 N이 주어진다.
# 이때, N!을 출력하는 프로그램을 작성하시오.

# n!은 (n-1)!에 n을 곱한 값과 같기 때문에 재귀함수로 표현, 0! = 1 임

def factorial(n):
    if n <= 1:
        ans = 1
    else:
        ans = factorial(n-1) * n
    return ans

print(factorial(int(input())))
