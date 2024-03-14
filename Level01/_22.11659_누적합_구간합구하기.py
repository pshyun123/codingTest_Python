# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

#첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다.
# 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다.
# 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

# 1 ≤ N ≤ 100,000
# 1 ≤ M ≤ 100,000
# 1 ≤ i ≤ j ≤ N

# 방법 1. 누적 합(prefix sum) 사용
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

pfs = list(map(int,input().split()))
for i in range(n-1):
    pfs[i+1] += pfs[i]
pfs = [0] + pfs

for _ in range(m):
    a,b = map(int,input().split())
    print(pfs[b]-pfs[a-1])


# 방법 2. 누적합을 미리 구하기
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sum = [0]
tmp = 0

# 누적 합 구하기
for i in numbers:
    tmp = tmp + i
    sum.append(tmp)

# 구간 합 구하기
for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])
