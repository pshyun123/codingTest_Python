#  “만약, 입출력이
# $N$바이트 크기의 정수라면 프로그램을 어떻게 구현해야 할까요?”
#
# 책에는 long int는 4바이트 정수까지 저장할 수 있는 정수 자료형이고 long long int는
# 8바이트 정수까지 저장할 수 있는 정수 자료형이라고 적혀 있었다. 혜아는 이런 생각이 들었다.
# “int 앞에 long을 하나씩 더 붙일 때마다 4바이트씩 저장할 수 있는 공간이 늘어나는 걸까?
# 분명 long long long int는 12바이트, long long long long int는 16바이트까지 저장할 수 있는 정수 자료형일 거야!”
# 그렇게 혜아는 당황하는 면접관의 얼굴을 뒤로한 채 칠판에 정수 자료형을 써 내려가기 시작했다.
# N바이트 정수까지 저장할 수 있다고 생각해서 칠판에 쓴 정수 자료형의 이름은 무엇일까?

# 방법1
for i in range(int(input())//4):
    print('long', end="")
print('int')

# 방법2
n = int(input())
answer = 'int'
for i in range(n//4):
    answer = 'long ' + answer
print(answer)