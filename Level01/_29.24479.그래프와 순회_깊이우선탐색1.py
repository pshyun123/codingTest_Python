# 깊이 우선 탐색(DFS,Depth-First Search)

# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다.
# 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다.
# 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.
# 깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

#dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);
# }

# 방법1. stack
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
# 그래프 구성을 위한 인접 리스트 생성
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 내림차순인 인접 그래프를 스택에 하나씩 넣어주면, 나중에 스택에서
# 꺼낼때는 이들을 오름차순으로 꺼내게 됨
for i in range(1, len(graph)):
    graph[i].sort(reverse=True)

def DFS(start):
    stack = [start] # 스택을 활용한 DFS를 위한 초기화
    visited = [-1] * (N + 1) # 방문 여부를 기록하는 배열
    result = [0] * (N + 1)  # 방문 순서를 기록하는 배열
    cnt = 1   # 방문 순서 값 초기화

    # DFS 탐색
    while stack:
        cnt_node = stack.pop()# 스택에서 노드 추출

        # 이미 방문한 노드라면 스킵
        if visited[cnt_node] == 1:
            continue

        visited[cnt_node] = 1 # 방문 표시
        result[cnt_node] = cnt # 방문 순서 기록
        cnt += 1 # 방문 순서 값 증가



        for adj_node in graph[cnt_node]:
            if visited[adj_node] == -1: # 아직 방문 이력 없으면(=스택에서 뽑은 적 없으면)
                stack.append(adj_node)   # 스택에 추가

    return result

# DFS 수행 결과 출력
result = DFS(R)
print(*result[1:], sep="\n")  # 첫 번째 노드는 제외하고 출력


# 방법2. 재귀

import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 재귀 제한 해제
sys.setrecursionlimit(10 ** 9)

# 정점의 개수(N), 간선의 개수(M), 시작 노드(R) 입력
N, M, R = map(int, input().split())

# 그래프 구성을 위한 인접 리스트 생성
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력 및 인접 리스트 구성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 정점에 대해 오름차순으로 인접 노드를 정렬
for i in range(1, len(graph)):
    graph[i].sort()

# DFS 함수 정의
def DFS(start):
    visited = [-1] * (N + 1)  # 방문 여부를 기록하는 배열
    path = []  # 방문 경로를 기록하는 배열

    # 재귀를 통한 DFS 탐색
    def recursive_DFS(node):
        visited[node] = 1  # 방문 표시
        path.append(node)  # 방문 경로에 추가

        # 인접 노드에 대해 재귀적으로 탐색
        for adj_node in graph[node]:
            if visited[adj_node] == -1:  # 방문하지 않은 노드인 경우에만 재귀 호출
                recursive_DFS(adj_node)

    # 시작 노드부터 DFS 호출
    recursive_DFS(start)

    return path  # 방문 경로 반환

# DFS 수행 결과 처리
path = DFS(R)
result = [0] * (N + 1)

# 방문 순서를 결과에 기록
for idx, node in zip(range(1, len(path) + 1), path):
    result[node] = idx

# 결과 출력
print(*result[1:], sep="\n")  # 첫 번째 노드는 제외하고 출력