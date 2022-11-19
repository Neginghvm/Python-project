"""
Negin Ghavami
4012061032
"""
def EX3_1(N):
  i = 0
  while N != 1:
    if N % 2 == 0:
      N = N / 2
      i = i + 1
    elif N % 2 == 1:
      N = N*3 + 1
      i = i + 1
  return i
