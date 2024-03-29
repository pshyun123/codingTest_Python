# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다.
# ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다.
# 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다.
# 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

import sys

# 입력으로 리스트의 길이를 받음
n = int(input())

# 리스트의 숫자들을 입력받아 정렬된 리스트로 저장
numbers = sorted(list(map(int, sys.stdin.readline().split())))

# 두 수를 더하여 만들고자 하는 값
x = int(input())

# 결과를 저장할 변수 초기화
answer = 0

# 리스트의 가장 작은 값과 가장 큰 값을 가리키는 포인터 초기화
left, right = 0, n - 1

# left가 right보다 작은 동안 반복
while left < right:
    # 현재 left와 right가 가리키는 두 수의 합 계산
    temp = numbers[left] + numbers[right]

    # 두 수의 합이 목표값과 같으면
    if temp == x:
        # 경우의 수를 하나 증가시키고 left 포인터를 오른쪽으로 이동
        answer += 1
        left += 1

    # 두 수의 합이 목표값보다 작으면
    elif temp < x:
        # left 포인터를 오른쪽으로 이동하여 두 번째로 작은 수를 더함
        left += 1

    # 두 수의 합이 목표값보다 크면
    else:
        # right 포인터를 왼쪽으로 이동하여 큰 수를 줄임
        right -= 1

# 결과 출력
print(answer)
