from math import ceil


def sol(mine,rock,high):
  if mine < rock :
    return "Error"
  if mine >= high:
    return 1
  remain  = high - mine
  return 1+ceil(remain/(mine-rock))
  

mine = int(input())
rock = int(input())
high = int(input())

print(sol(mine,rock,high))