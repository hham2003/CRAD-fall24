This directory contains the vulnerable program and complementary files used to simulate buffer overflow

## File descriptions
**generate-overflow-text.py**:
  creates 100 random lines of input text called _data.txt_. This text file is the input file for _vulnerable-program.c_. Change variables inside Python file to adjust the overflow occurrence rate.
  
**vulnerable-program.c**:
  Core program in which a buffer overflow may occur.
  
**entrypoint.sh**:
  Bash script to "pipe" _data.txt_ into compiled C program.

**Dockerfile**:
  Configuration file for creating the main container in which _vulnerable-program.c_ will run.
