li=[1,2,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
n=int(input())
l=0
r=len(li)-1
mid=int((l+r)/2)
while l<r:
  if li[mid]==n:
    break
  elif li[mid]>n:
    r=mid-1
  else :
    l=mid+1
  mid=int((l+r)/2)
print(-1 if li[mid]!=n else mid)

