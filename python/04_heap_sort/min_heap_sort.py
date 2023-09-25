""" 
1 - represent the list in the form of a complete binary tree 
1.1 - each node has two children except possibly the nodes in the last level
1.2 - All leaves in the last level are placed as far to the left as possible
2 - heapify the tree
"""

"""

"""
def parent_index(index):
  return int((index - 1) / 2)


def left_index(index):
  return 2 * index + 1


def right_index(index):
  return 2 * index + 2


def swap(heap, index_1, index_2):
  heap[index_1], heap[index_2] = heap[index_2], heap[index_1]

def minHeapfyUp(heap, index):
  while index > -1:
    if (heap[parent_index(index)] > heap[index]):
      swap(heap, parent_index(index), index)
    index -= 1

def insert(heap, item):
  heap.append(item)
  minHeapfyUp(heap, len(heap) - 1)

def extract_min(heap):
  heap[0], heap[-1] = heap[-1], heap[0]
  min = heap.pop()
  minHeapfyUp(heap, len(heap) - 1)
  return min

list = [14, 3, 7, 18, 2, 16, 25, 11]

min_heap = []

for item in list:
  insert(min_heap, item)

print(min_heap)
sorted = []
while min_heap:
  sorted.append(extract_min(min_heap))
print(sorted)


