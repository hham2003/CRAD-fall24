FROM gcc:latest

COPY read-with-gets.c /read-with-gets.c

RUN gcc -o read-data read-with-gets.c -std=c99

COPY data.txt /data.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

