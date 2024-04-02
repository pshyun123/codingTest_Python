# 루트 없는 트리가 주어진다.
# 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.


# DFS 방식


# BFS 방식
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
vertices = [[0] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    vertices[a].append(b)
    vertices[b].append(a)

parent[1] = 0
q = deque()
q.append(1)

while q:
    current = q.popleft()
    for v in vertices[current]:
        if parent[v] == 0:
            parent[v] = current
            q.append(v)

print('\n'.join(map(str, parent[2:])))
