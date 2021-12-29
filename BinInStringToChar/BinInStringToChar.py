a=input().replace('pu','0').replace('pe','1')
for i in range(0,int(len(a)),8):
  print(chr(int(a[i:i+8],2)),end='')