""" Merge two sorted lists """
def merge(list_a, list_b):
  c = []
  while list_a and list_b:
    if (list_a[0] < list_b[0]):
      c.append(list_a.pop(0))
    else:
      c.append(list_b.pop(0))
  if list_a:
    c = c + list_a
  elif list_b:
    c = c + list_b
  
  return c
    

def merge_sort(list):
  if len(list) == 1:
    return list
  left_list = list[0:len(list) // 2]
  right_list = list[len(list) // 2:]
  return merge(merge_sort(left_list), merge_sort(right_list))

list = [2, 13, 45, 21, 3, 56, 10, 7, 41, 9]
print(merge_sort(list))