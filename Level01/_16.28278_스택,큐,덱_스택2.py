#정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 다섯 가지이다.
# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

import sys
N = int(sys.stdin.readline()) # 명령의 수 입력받기
ST = [] # 스택 초기화
for i in range(N) : # N번 반복하며 명령을 처리
    op = sys.stdin.readline().split()
    if op[0] == '1':  # '1' 명령: 스택에 정수 x를 push
        ST.append(int(op[-1]))
    elif op[0] == '2': # '2' 명령: 스택에서 원소를 pop하고 그 값을 출력
        if ST: # 스택이 비어있지 않으면
            print(ST.pop(-1))
            continue
        print(-1) # 스택이 비어있으면 -1 출력
    elif op[0] == '3':
        print(len(ST))
    elif op[0] == '4': # '4' 명령: 스택이 비어있으면 1 출력, 아니면 0 출력
        if ST:
            print(0)
            continue
        print(1)
    elif op[0] == '5': # '5' 명령: 스택이 비어있지 않으면 스택의 top 원소를 출력, 비어있으면 -1 출력
        if ST:
            print(ST[-1])
            continue
        print(-1) # 스택이 비어있으면 -1 출력

