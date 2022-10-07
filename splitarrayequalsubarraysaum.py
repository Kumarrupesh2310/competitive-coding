def findPivot(arr):
  l=0
  r=len(arr)-1
  lsum=arr[l]
  rsum=arr[r]

  while l<r:
    if lsum==rsum and l+2==r:
      return l+1
    elif lsum<rsum:
      l += 1
      lsum+=arr[l]
    else:
      r -= 1
      rsum+=arr[r]

  return -1
 
print(findPivot([2, 4, 5, 1, 2, 3]))
