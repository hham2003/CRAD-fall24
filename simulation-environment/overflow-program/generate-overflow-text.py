import string
import random

# create list of characters to choose from when generating each line of input text
chars = list(string.ascii_letters)
for i in range(10):
    chars.append(str(i))
    
buffer_size = 16    # size of input buffer in "vulnerable-program.c"

overflow_rate = 0.66    # approximate proportion of character strings that will be larger than buffer_size

# randomly generate 100 character strings of variable length
entries = []
for _ in range(100):
    entry = ""
    size = int( (buffer_size-1)*random.random() )   # randomly generated length < buffer_size for current character string
    if random.random() < overflow_rate:
        size += int(30*random.random()) # randomly increase the length of the current character string to > buffer_size (30 is an arbitrary choice here)
    
    # randomly generate the character string
    for _ in range(size):
        chars_index = int(len(chars)*random.random())
        entry += chars[chars_index]
    
    entries.append(entry)


# write each character string to a text file    
with open("data.txt", "w") as file:
    file.writelines([entry + "\n" for entry in entries])
    
    
