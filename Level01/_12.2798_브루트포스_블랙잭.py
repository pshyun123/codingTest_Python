# 변형된 블랙잭
# N장의 카드에 써져 있는 숫자가 주어졌을 때,
# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

# for 문 중첩(이게 조금 더 나은 방법)

N, M = map(int, input().split())
ls = list(map(int, input().split()))

arr = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            card = ls[i] + ls[j] + ls[k]
            if card > M:
                continue
            else:
                ls.append(card)
print(max(ls))


# itertools 모듈의 combinations 이용

# combinations함수 : 주어진 반복 가능한 객체에서 지정된 길이의 가능한 조합을 생성
# 중복된 요소를 허용하지 않으며, 순서는 고려하지 않음
from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
nlst = []

for three in combinations(lst, 3):
    if sum(three) > M:
        continue
    else:
        nlst.append(sum(three))
print(max(nlst))