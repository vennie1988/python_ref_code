"""
#unpacking a sequence into separate variables
"""
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
_, shares, price, _ = data


"""
#unpacking elements from iterables of arbitrary length
"""
record = ('Dave', 'Dave@example.com', '777-888-9999', '111-222-3333')
name, email, *phone_numbers = user_record
record = ('ACME', 50, 91.1, (12, 12, 2111))
name, *_, (*_, year) = record


"""
#keeping the last N Items
"""
from collections import deque

def search(lines, pattern, history=5):
	previous_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)	

if __name__ == "__main__":
	with open('somefile.txt') as f:
		for line, previous_lines in search(f, 'python', 5):
			for pline in prevlines:
				print(pline, end='')
			print(line, end='')
			print('-'*20)			


"""
# Finding the largest of smallest N items, 堆操作
"""
import heapq

nums = [1,3,4,2901,29123,1182,1283]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
	{'name': 'IBM', 'shares':100, 'price':91.1},
	{'name': 'FB', 'shares':50, 'price':532.22},
	{'name': 'YHOO', 'shares':45, 'price':31.74},
]
cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])

heapq.heapify(nums)
heapq.heappop(heap)

#if the list is not long, we can use
sorted(items)[:N]
sorted(items)[-N:]

