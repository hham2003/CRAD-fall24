# Dockerfile to containerize the vulnerable C program

# use gcc compiler
FROM gcc:latest

# copy C file into container root
COPY vulnerable-program.c /vulnerable-program.c

# compile vulnerable program into an executable called "read-data"
# -std=c99 flag tells gcc to compile according to the 1999 C standard (gcc will complain about the gets() method otherwise)
RUN gcc -o read-data vulnerable-program.c -std=c99

# copy the input text file into container root
COPY data.txt /data.txt

# copy bash script into container root
COPY entrypoint.sh /entrypoint.sh

# enable execution of bash script which executes the "read-data" to read "data.txt" from standard input
RUN chmod +x /entrypoint.sh

# set bash script as default executable for the container
ENTRYPOINT [ "/entrypoint.sh" ]

