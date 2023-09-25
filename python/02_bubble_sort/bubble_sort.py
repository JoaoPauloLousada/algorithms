# End = length of the List - 1
# While End > 1:
#   i = 1
#   While i does not exceed End:
#     If List[i] > List[i+1]:
#       Swap List[i] and List[i+1]
#     i = i + 1
#   End = End - 1
# return List

def bubble_sort(list):
  end = len(list) - 1
  while end > 0:
    i = 0
    while i < end:
      if list[i] > list[i + 1]:
        tmp = list[i + 1]
        list[i + 1] = list[i]
        list[i] = tmp
      i += 1
    end -= 1
  return list

list = [50, 40, 30, 20, 10, 0]
print(bubble_sort(list))

list2 = [50, 40, 55, 30, 45, 20, 35, 10, 0, 5]
print(bubble_sort(list2))