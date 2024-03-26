# 상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

# 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다.
# 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
# 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
# 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
# 상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다.
# 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.
#
# 폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.
#
# 입력
# 첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.
# 둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.
# 두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.

# 방법1
import sys
x = list(sys.stdin.readline().strip())
M = list(sys.stdin.readline().strip())
m = len(M)
stack = []
for i in x:
    stack.append(i)
    # 스택의 끝부터 폭발 문자열의 길이만큼을 비교하여 제거
    if stack[len(stack)-m:len(stack)] == M: #스택의 끝부터 M의 글자열 크기까지 자른게 M과 같다면
        for _ in range(m): # m의 길이만큼
            stack.pop() # stack에서 꺼내준다!
if stack:
    print(*stack, sep='')
else:
    print("FRULA")


# 방법2
def main():
    string = input()  # 전체 문자열
    bomb = input()  # 폭발 문자열

    lastChar = bomb[-1]  # 폭발 문자열의 마지막 글자
    stack = []
    length = len(bomb)  # 폭발 문자열의 길이

    # 문자열을 한 글자씩 처리하면서 폭발 문자열 제거
    for char in string:
        stack.append(char)
        # 스택의 끝 부분에서 폭발 문자열 확인하여 제거
        if char == lastChar and ''.join(stack[-length:]) == bomb:
            del stack[-length:]

    answer = ''.join(stack)
    if answer == '':
        print("FRULA")
    else:
        print(answer)


if __name__ == '__main__':
    main()
