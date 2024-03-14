# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

#첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다.
# 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다.
# 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

# 1 ≤ N ≤ 100,000
# 1 ≤ M ≤ 100,000
# 1 ≤ i ≤ j ≤ N

# 방법 1. 누적 합(prefix sum) 사용
import sys
input = sys.stdin.readline()
n,m = map(int, input().split()) # n은 pfs 리스트의 길이, m은 쿼리의 개수
pfs = list(map(int,input().split())) # 부분합을 저장하는 리스트
# 부분합 리스트 pfs를 구성 - pfs 리스트의 각 요소는 해당 인덱스까지의 누적값 가짐(이전 값 + 현재 값)

for i in range(n-1):
    pfs[i+1] += pfs[i]
pfs = [0] + pfs # pfs 리스트의 맨 앞에 0 추가, 인덱스 0부터 시작하도록 조정

for _ in range(m): # m번 반복. 반복할 때마다 하나의 쿼리를 처리
    a, b = map(int.input().split()) # 각 쿼리마다 시작 인덱스 a와 끝 인덱스 b를 입력받음
    print(pfs[b]-pfs[a-1]) # b번째 인덱스의 값을 시작 인덱스 a-1번째 인덱스의 값으로 나누어 해당 범위의 부분합을 계산하여 출력



# 방법 2. 누적합을 미리 구하기
n, m = map(int, input().split())
numbers = list(map(int, input().split())) # 리스트에 담음
sum = [0] # 리스트 초기화, 처음엔 합 없으므로 0 추가
tmp = 0 # 임시변수 0으로 초기화, 누적 합 저장하는 것

 # 누적 합 구하기
for i in numbers:
    tmp = tmp + i
    sum.append(tmp)

 # 구간 합 구하기
for _ in range(m):
    i, j = map(int, input().split()) # 각 쿼리마다 시작 인덱스 i와 끝 인덱스 j를 입력음
    print(sum[j] - sum[i-1])
    # i-1을 하는 이유는 i번째부터 j번째까지의 구간 합을 계산하기 위해서
