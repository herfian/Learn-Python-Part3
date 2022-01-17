# Filter

my_list = [1,2,3,4,5,6,7,8,9,10]

def only_odd(item):
  return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(my_list)

# Output :
# [1, 3, 5, 7, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]