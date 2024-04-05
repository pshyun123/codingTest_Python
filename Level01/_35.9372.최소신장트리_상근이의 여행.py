# 상근이는 겨울방학을 맞아 N개국을 여행하면서 자아를 찾기로 마음먹었다.
#
# 하지만 상근이는 새로운 비행기를 무서워하기 때문에, 최대한 적은 종류의 비행기를 타고 국가들을 이동하려고 한다.
#
# 이번 방학 동안의 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주자.
#
# 상근이가 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도(심지어 이미 방문한 국가라도) 된다.

# 방법1
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    for _ in range(m):
        input() # 무조건 연결그래프이므로 입력 값 무시
    print(n - 1)

# 방법2
t = int(input())
for l in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    visited = [False] * n
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    print(dfs(graph, 0, visited, 0))