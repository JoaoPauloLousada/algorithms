""" 
If List is empty:
  Report the search has failed
Else:
  Pivot = the middle entry of the list
  If Pivot = item:
    Report the search succeeded
  Else If Pivot > item:
    List = items preceeding Pivot
    Report the List
  Else 
    List = items following Pivot
    Report the List
"""

from math import floor

# iterations variable just for sake of awareness of how many times the function runs to find an item
def binary_search(list, item, iterations = 0):
  iterations += 1
  
  if len(list) == 0:
    return None, iterations
  else:
    pivot_index = floor((len(list) - 1) / 2)
    pivot = list[pivot_index]
    if (pivot == item):
      return pivot, iterations
    elif pivot > item:
      list = list[:pivot_index]
      return binary_search(list, item, iterations)
    else:
      list = list[pivot_index + 1:]
      return binary_search(list, item, iterations)

list = [10,20,30,40,50,60,70,80,90,100]
print(binary_search(list, 40))
print(binary_search(list, 70))
print(binary_search(list, 80))
print(binary_search(list, 90))
print(binary_search(list, 11))