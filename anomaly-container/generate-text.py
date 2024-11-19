import string
import random

chars = list(string.ascii_letters)
for i in range(10):
    chars.append(str(i))
    
entries = []
for _ in range(100):
    entry = ""
    size = int(15*random.random())
    # if random.random() < 0.05:
    #     size += int(30*random.random())
    
    for _ in range(size):
        chars_index = int(len(chars)*random.random())
        entry += chars[chars_index]
    
    entries.append(entry)


    
with open("/Users/henryham/Desktop/f24/Capstone/Docker/testing/overflow-program/data.txt", "w") as file:
    file.writelines([entry + "\n" for entry in entries])
    