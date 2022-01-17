# zip
my_list = [1,2,3,4,5]
your_list = [10,11,12,13,14,15]
their_list = [21,22,23,24,25]

print(list(zip(my_list, your_list, their_list)))
print(my_list)
print(your_list)
print(their_list)

# Output :
# [(1, 10, 21), (2, 11, 22), (3, 12, 23), (4, 13, 24), (5, 14, 25)]
# [1, 2, 3, 4, 5]
# [10, 11, 12, 13, 14, 15]
# [21, 22, 23, 24, 25]