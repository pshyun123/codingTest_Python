# 2차원 배열, .append
# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
# N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.


N, M = map(int, input().split())
A, B = [], []

# A 행렬의 값 입력 받음
for i in range(N):
    a = list(map(int, input().split()))# 각 행의 값 리스트로 변환, A에 추가
    A.append(a) #리스트 A에 새로운 요소인 리스트 a를 추가
# B 행렬의 값 입력 받음
for i in range(N):
    b = list(map(int, input().split()))# 각 행의 값 리스트로 변환, B에 추가
    B.append(b) #리스트 B에 새로운 요소인 리스트 b를 추가, 2차원 리스트에 입력된 각 행 추가

for i in range(N) :
    for j in range(M):
        # A와 B의 같은 위치에 있는 원소를 더한 값을 result에 저장
        result = A[i][j] + B[i][j]
        # 결과 한줄에 출력, 공백으로 구분
        print(result, end=' ')
    print()