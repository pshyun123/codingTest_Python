# 준규가 가지고 있는 동전은 총 N종류이고,
# 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())
coin_lst = list()
for i in range(N):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K//coin_lst[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K%coin_lst[i] # K는 동전으로 나눈 나머지로 계속 반복

print(count)