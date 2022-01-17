# Parameters
# Default Parameters
def say_hello(name='Hana',emoji='Anger'): # Define
  print(f'Hello {name}, {emoji}')

# Positional Arguments
say_hello('Mark','Fun') # Call
say_hello('Sua','Fun')

# Keyword Arguments
say_hello(emoji='Care',name='Amar')
say_hello()

# Output :
# Hello Mark, Fun
# Hello Sua, Fun
# Hello Amar, Care
# Hello Hana, Anger