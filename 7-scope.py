# Scope - what variables do i have access to?

a = 1 # Global Scope

def parent(): # Parent Scope
  a = 10
  def confusion(): # Local Scope
    return a
  return confusion()

# Output :
print(parent()) # 10
print(a) # 1

# 1 - Start with local scope
# 2 - Parent local scope
# 3 - Global Scope
# 4 - Built in python functions.