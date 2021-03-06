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


"""
Implementing a Priority Queue
using heapq module
"""
class PriorityQueue:
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1

	def pop(self):
		return heapq.heaqpop(self._queue)[-1]


"""
Mapping Keys to Multiple Values in a Dictionary
"""
#list: preserve the insertion order of the items
d = {
	'a' : [1, 2, 3]
	'b' : [4, 5]
}

#set: eliminate duplicates
e = {
	'a' : {1, 2, 3}
	'b' : {4, 5}
}

#Implement
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
...

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(3)
...

#or
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
...

# compare, the late is more better
d = {}
for key, value in pairs:
	if key not in d:
		d[key] = []
    d[key].append(value)

d = defaultdict(list)
for key, value in pairs:
	d[key].append(value)


"""
Keeping Dictionaries in Order
using OrderedDict, pls note the performance issue, 2 times than the normal dictionary
"""
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4


"""
Calculating with Dictionaries
"""
prices = {
	'ACME': 45.23,
	'AAPL': 612.78,
	'IBM': 205.55
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))

# need to aware that zip() create an iterator that can only be comsumed once
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
print(max(prices_and_names))  # valueError: max() arg is an empty sequence


"""
Finding Commonalities in Two Dictionaries
"""
a = {
	'x' : 1,
	'y' : 2,
	'z' : 3
}

b = {
    'w' : 10,
	'x' : 11,
	'y' : 2
}

#Find keys in comman
a.keys() & b.keys()  # {'x', 'y'}
#Find keys in a that are not in b
a.keys() - b.keys()  # {'z'}
#Find (key, value) pairs in common
a.items() & b.items() # {('y', 2)}

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.key() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}


"""
Removing Duplicates from a sequence while maintaining order
"""
# for hashable sequence
def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)

#for not hashable sequence
def dedupe(items, key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)

#usage
a = [{'x':1, 'y':2}, {'x':1, 'y':3}]
list(dedupe(a, key=lambda d: (d['x'],d['y'])))
list(dedupe(a, key=lambda d: d['x']))

#simple usage
a = [1, 5, 2, 1, 9, 1]
set(a)

#eliminate duplicate lines
with open(somefile, 'r') as f:
	for line in dedupe(f):
		...

"""
Naming a slice
"""
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
#items[2:4] == items[a]
items[a] = [10, 11]
#items = [0, 1, 10, 11, 4, 5, 6]
del items[a]
#items = [0, 1, 4, 5, 6]
#other usage
a = slice(10, 50, 2)
a.start
a.stop
a.step


"""
Determing the most frequently occuring items in a sequence
using collections.Counter Class
"""
words = [
     'look', 'into', "look", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
#output [('look', 3), ('into', 1), ('under', 1)]
word_counts['look']

#increment the count manually, simply use addtion or update() method
morewords = ['why', 'are', 'you']
for word in morewords:
	word_counts[word] += 1
#or
word_counts.update(morewords)

#Counter instance can be easily combined using various mathematical operations
a = Counter(words)
b = counter(morewords)
#Combine counts
c = a + b
#subtract counts
d = a - b

"""
Sorting a list of Dictionaries by a common key
"""
