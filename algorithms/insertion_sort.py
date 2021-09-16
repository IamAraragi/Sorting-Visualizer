import time
from colors import *

def insertion_sort(array, drawData, wait_time):
	for j in range(1, len(array)):
		key = array[j]
		i = j -1

		while i>=0 and array[i]>key:
			array[i+1] = array[i]
			i = i - 1
		array[i+1] = key

		drawData(array, [PURPLE if x == i else YELLOW if x == j else BLUE for x in range(len(array))])
		time.sleep(wait_time)

	drawData(array, [BLUE]*len(array))

	return array