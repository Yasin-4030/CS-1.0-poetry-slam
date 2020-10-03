print()
def get_file_lines(filename):
  infile = open(filename, "r")
  poem_lines = infile.read().splitlines()
  infile.close()
  return poem_lines

def lines_printed_backwards(lines_list):
  # Reverse the list of lines
  lines_list.reverse()

  # Use the len() function
  counter = len(lines_list)

  for line in lines_list:
    print(counter, line)
    counter -= 1

import random
def lines_printed_random(lines_list):
    counter = len(lines_list)
    for _ in range(counter):
        print (random.choice(lines_list))


    


file_lines = get_file_lines('Rumi.txt')
# lines_printed_backwards(file_lines)
lines_printed_random(file_lines) 
# lines_printed_custom(file_lines)