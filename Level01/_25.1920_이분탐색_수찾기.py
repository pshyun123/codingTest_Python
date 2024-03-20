# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때,
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 방법1. 이분탐색

N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()			# A 정렬

# arr의 각 원소별로 이분탐색
for num in arr:
    lt, rt = 0, N - 1		# lt는 맨 앞, rt는 맨 뒤
    isExist = False		# 찾음 여부

    # 이분탐색 시작
    while lt <= rt:		# lt가 rt보다 커지면 반복문 탈출
        mid = (lt + rt) // 2	# mid는 lt와 rt의 중간값

        if num == A[mid]:	# num(목표값)이 A[mid]값과 같다면
            isExist = True
            print(1)		# 1 출력
            break

        elif num > A[mid]:	# 찾으려는 숫자가 중간값보다 크면 오른쪽 부분리스트 탐색
            lt = mid + 1

        else:			# 찾으려는 숫자가 중간값보다 작으면 왼쪽 부분리스트 탐색
            rt = mid - 1

    if not isExist:		# 찾지 못한 경우
        print(0)		# 0 출력



# 방법2. set 자료구조 사용
N = int(input())
A = set(map(int, input().split()))	# 탐색 시간을 줄이기 위해 set으로 받음
M = int(input())
arr = list(map(int, input().split()))

for num in arr:				# arr의 각 원소별로 탐색
    print(1) if num in A else print(0)	# num이 A 안에 있으면 1, 없으면 0 출력


# 방법3. 이분탐색- 첫번째는 런타임 에러/ 더 효율적인 코드(이분탐색 중에서는)
from sys import stdin, stdout
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l,N,start,end))



# 방법4. 이분탐색 - bisect_left() 함수 사용
from bisect import bisect_left

# 리스트 A의 길이와 요소들 입력받기
N = int(input())
A = sorted(map(int, input().split()))

# 리스트 arr의 길이와 요소들 입력받기
M = int(input())
arr = list(map(int, input().split()))

# 리스트 A에서 이분 탐색으로 숫자가 존재하는지 확인하는 함수
def binary_search(num):
    index = bisect_left(A, num)
    if index < len(A) and A[index] == num: # num 이랑 작거나 같으면 리스트 안에 존재, 아니면 false 반환
        return True
    return False

# arr의 각 원소별로 이분 탐색을 수행하여 결과 출력
for num in arr:
    if binary_search(num):
        print(1)
    else:
        print(0)
