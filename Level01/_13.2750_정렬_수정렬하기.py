# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# sorted() 함수 사용 : 원본 리스트를 변경하지 않고 새로운 정렬된 리스트를 반환
N = int(input())
M = []
for i in range(N):
    M.append(int(input()))
M = sorted(M)
for i in range(len(M)):
    print(M[i])


# sort() 함수 사용 : 리스트를 제자리에서(in-place) 정렬. 즉, 원본 리스트 자체를 변경함
N = int(input())
M = set()
for i in range(N):
    M.add(int(input()))
M = list(M)
M.sort()
for i in range(len(M)):
    print(M[i])


