# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

n, m = map(int, input().split())

case = []
def recursive():
  if len(case) == m:
    print(' '.join(map(str, case)))
    return

  for i in range(1, n + 1):
    if i in case:
      continue
    case.append(i)
    recursive()
    case.pop()

recursive()
