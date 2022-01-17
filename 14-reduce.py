# Reduce
from functools import reduce

my_list = [1,2,3,4,5]

def accumulator(acc, item):
  print(acc, item)
  return acc + item

print(reduce(accumulator, my_list, 0))

# Output :
# 0 1
# 1 2
# 3 3
# 6 4
# 10 5
# 15