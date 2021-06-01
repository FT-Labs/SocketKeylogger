#!/usr/bin/python

import socket
import sys
import os
import signal

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",1235))
s.listen(5)



while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} established!")
    full_msg = ''
    new_msg = True
    while True:
        msg = clientsocket.recv(16)

        try:

            if new_msg:

                print(f"new message length: {msg[:HEADER_SIZE]}")
                msglen = int(msg[:HEADER_SIZE])
                new_msg = False

            full_msg += msg.decode("utf-8")

            if len(full_msg)-HEADER_SIZE == msglen:
                print("Full message received")
                print(full_msg[HEADER_SIZE:])
                new_msg = True
                full_msg = ''
        except Exception as e:
            continue

    print(full_msg)
