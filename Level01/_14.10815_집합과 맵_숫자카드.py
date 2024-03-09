# 숫자 카드는 정수 하나가 적혀져 있는 카드이다.
# 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때,
# 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# dictionary 활용
import sys
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split)) # 카드 숫자 공백기준으로 분리해 리스트로 받기
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split)) # 체크할 숫자들을 공백기준으로 분리해 리스트로 받기

_dict = {} # 빈 딕셔너리 생성
for i in range(len(cards)):
    _dict[cards[i]] = 0 # 0으로 초기화

# 체크 리스트를 순회하면서 각 숫자가 딕셔너리의 키로 존재하는지 확인
# 숫자가 카드들 중에 존재하면 1을 출력, 그렇지 않으면 0을 출력
for j in range(M):
     if checks[j] not in _dict:
         print(0, end='')
     else: print(1, end='')


# 이진 탐색 -1
import bisect
N = int(input())
card = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))
card.sort()
answer = [0] * M
for o in checks:
    l = bisect.bisect_left(card, o)
    r = bisect.bisect_right(card, o)
    print(r - l, end=' ')

# 이진 탐색 -2
import sys

N = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

for check in checks:
    low, high = 0, N-1  # cards의 이진 탐색 index
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] > check:  # 중간 값보다 작다면
            high = mid - 1  # 중간보다 왼쪽 한 칸 옆까지 탐색
        elif cards[mid] < check:  # 중간 값보다 크다면
            low = mid + 1  # 중간보다 오른쪽 한 칸 옆부터 탐색
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')


