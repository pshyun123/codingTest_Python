# 오늘은 n의 피보나치 수를 재귀호출과 동적 프로그래밍으로 구하는 알고리즘을 배웠다. 재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자. 아래 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.

# 피보나치 수 재귀호출 의사 코드는 다음과 같다.
# fib(n) {
#     if (n = 1 or n = 2)
#     then return 1;  # 코드1
#     else return (fib(n - 1) + fib(n - 2));
# }

# 피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.
# fibonacci(n) {
#     f[1] <- f[2] <- 1;
#     for i <- 3 to n
#         f[i] <- f[i - 1] + f[i - 2];  # 코드2
#     return f[n];
# }


# 방법 1. 재귀함수 사용하여 피보나치 수열 계산. 시간 복잡도는 O(2^n)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
    return n - 2

n = int(input())
print(fib(n), fibonacci(n))

# 방법 2. 배열을 사용하여 피보나치 수열을 계산.시간 복잡도는 O(n).
# 중간에 계산한 값들을 배열에 저장하고 필요할 때마다 접근하기 때문에 더 나음
def fib(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

def fibonacci(n):
    return n - 2

n = int(input())
print(fib(n), fibonacci(n))

# 방법 3. 반복문을 사용하여 피보나치 수열을 계산. 시간 복잡도 O(n),
# 중간에 계산한 값들을 모두 저장해두어야 하므로 공간 복잡도가 O(n)
def fib(n):
    a, b = 1, 1  # 초기값 설정 (f(1) = 1, f(2) = 1)
    for i in range(3, n+1):  # n까지의 피보나치 수열 계산
        a, b = b, a+b  # a에는 이전 수열 값이, b에는 새로운 수열 값이 할당됨
    return b  # n번째 피보나치 수열 값 반환
