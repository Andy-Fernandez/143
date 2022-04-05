import sys

"https://jv.umsa.bo/problem.php?cid=2404&pid=0"

def binarySearchTruncated(l,r,n):
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
        down = (mid-1)*(mid)/2
        up = n*(n+1)/2 - mid*(mid+1)/2
 
        # If element is present at the middle itself
        if down == up:
            return mid
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif down<up:
            return binarySearchTruncated(mid + 1, r, n)
        else:
            return binarySearchTruncated(l, mid - 1, n)
 
    else:
        # Element is not present in the array
        return "NO"


for h in sys.stdin:
    n = int(h)
    print(binarySearchTruncated(0,n,n))
