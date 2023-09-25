#  i = 1
# select the i-th entry of the list as a pivot entry
# move the pivot entry to a temporary position; leave a hole in the list
# while there is an item above the hole AND item > pivot entry:
# - move the item to the hole, leaving a hole above the item
# move the pivot entry into the hole
# i = i + 1

def insertion_sort(list):
  i = 1 #  i = 1
  
  while i < len(list):
    # select the i-th entry of the list as a pivot entry
    # move the pivot entry to a temporary position;
    pivot = list[i] 
    # leave a hole in the list
    list[i] = None

    # while there is an item above the hole AND item > pivot entry:
    j = i - 1
    while (j > -1 and list[j] > pivot):
      # move the item to the hole
      list[j + 1] = list[j]
      # leaving a hole above the item
      list[j] = None
      j -= 1
    
    # move the pivot entry into the hole
    list[j + 1] = pivot

    # i = i + 1
    i+= 1
  return list

list = [10, 9, 6, 8, 7 ,11 ,5]
print(f"list: {list}")
print(f"sorted list: {insertion_sort(list)}")