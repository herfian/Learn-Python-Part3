def is_num(num):
  if num % 2 == 0:
    return True
  elif num % 2 != 0:
    return False

print(is_num(50)) # True

# Clean Code
# def is_num(num):
#   return num % 2 == 0
# print(is_num(51)) # False