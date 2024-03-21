# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
#
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

import sys
import heapq as hq

n = int(input())
heap = []
for i in range(n):
    # 정수 입력 받음
    x = int(sys.stdin.readline())
    # 정수 x가 0이 아닌 경우
    if x:
        hq.heappush(heap,(-x, x))
    # 입력된 정수가 0인 경우
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)

