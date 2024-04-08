# 간선에 가중치와 방향성이 없는 임의의 루트 있는 트리가 주어졌을 때, 아래의 쿼리에 답해보도록 하자.
# 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력한다.
# 만약 이 문제를 해결하는 데에 어려움이 있다면, 하단의 힌트에 첨부한 문서를 참고하자.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def countPoint(x):
    count[x]=1
    for i in tree[x]:
        if not count[i]:
            countPoint(i)
            count[x] += count[i]



n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
count = [0]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

countPoint(r)

for i in range(q):
    u = int(input())
    print(count[u])
