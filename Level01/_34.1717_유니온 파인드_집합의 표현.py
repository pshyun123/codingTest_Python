# 초기에
# $n+1$개의 집합
# $\{0\}, \{1\}, \{2\}, \dots , \{n\}$이 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.
#
# 집합을 표현하는 프로그램을 작성하시오.


import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n,m = map(int, input().split())
parent = [i for i in range(n + 1)]

# 같은 집합에 속하는지 찾기
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 두 집합 합치기
def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
for _ in range(m):
    opr, a, b = map(int, input().split())
    if opr == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")