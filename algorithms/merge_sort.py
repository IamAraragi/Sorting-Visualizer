import time
from colors import *
import sys

def merge_sort(array, p, r, drawData, wait_time):
	if p<r:
		q = (p + r) // 2
		merge_sort(array, p, q, drawData, wait_time)
		merge_sort(array, q+1, r, drawData, wait_time)
		merge(array, p, q, r)

		drawData(array, [PURPLE if x >= p and x < q else YELLOW if x == q 
                        else DARK_BLUE if x > q and x <=r else BLUE for x in range(len(array))])

		time.sleep(wait_time)

	drawData(array, [BLUE]*len(array))
	return array

def merge(array, p, q, r):
	import sys
	n1 = q - p + 1
	n2 = r - q
	L = []
	R = []

	for i in range(n1):
		L.append(array[p+i])

	for j in range(n2):
		R.append(array[q+j+1])
	L.append(sys.maxsize)
	R.append(sys.maxsize)

	i = 0
	j = 0
	for k in range(p, r+1):
		if L[i] < R[j]:
			array[k] = L[i]
			i+=1
		else:
			array[k] = R[j]
			j+=1