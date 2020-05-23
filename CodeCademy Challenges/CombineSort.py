"""
Write a function named combine_sort that has two parameters named lst1 and lst2.

The function should combine these two lists into one new list and sort the result. Return the new sorted list.
"""

def combine_sort(lst1,lst2):
  new_list=lst1+lst2
  new_list.sort()
  return new_list


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
