""" 
def quick_sort(List)
  if len(list) == 1
  Return List[0]
  Pivot = middle term of the List
  Right_list
  Left_list
  for i in items in the list
    if i > Pivot
      append i to Right_list
    else
      append i to Left_list
  return[quick_sort[Left_list], Pivot, quick_sort[Right_list]]
"""

def quick_sort(list):
  if len(list) <= 1:
    return list
  pivot = list[(len(list) - 1) // 2]
  
  left, middle, right = [], [], []

  for x in list:
    if x < pivot:
      left.append(x)
    elif x == pivot:
      middle.append(x)
    else:
      right.append(x)

  return quick_sort(left) + middle + quick_sort(right)


list = [45, 21, 3, 10, 56, 7, 41, 9]
# quick_sort(list)
print(quick_sort(list))