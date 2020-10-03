print()
# defining a function to open our txt file and read our lines of text on the file.
def get_file_lines(filename):
  infile = open(filename, "r")
  poem_lines = infile.read().splitlines()
  infile.close()
  return poem_lines
# .................................................................................

# creating function to print out text lines in a reverse order.
def lines_printed_backwards(lines_list):
  # Reverse the list of lines
  lines_list.reverse()

  # Use the len() function
  counter = len(lines_list)

  for line in lines_list:
    print(counter, line)
    counter -= 1
# ..................................................................................

# using function to print our lines in a random order.
import random
def lines_printed_random(lines_list):
    counter = len(lines_list)
    for _ in range(counter):
        print (random.choice(lines_list))

# ..................................................................................

# printing our poetry lines in alphabetical order.
def lines_printed_custom(lines_list):
    order = lines_list
    for alph_order in sorted(order):
        print(alph_order)

# ..................................................................................


file_lines = get_file_lines('Rumi.txt')
lines_printed_backwards(file_lines)
# lines_printed_random(file_lines) 
# lines_printed_custom(file_lines)