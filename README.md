# SocketKeylogger
A simple socket keylogger with Python. Listens to client computer, and if the keylogger is on it will send every 10 words written. Just for educational purposes only.


### Server Side

Note that this program is designed for local  networks only. If you want to try from an outside network, router port forwarding needs te be configured carefully. If you want to be your own client and computer, just write hostname for both of client and server side scripts. 

###  Client Side

Client side is a little bit more complex. Since this is for educational purposes, you can open and close the keylogger by key presses. Press 'Esc' to view interaction window. After that 
that, there are 3 options. 's' to start keylogger, 'S' to stop it, and finally 'q' to close the program. There is also a placeholder 'C' open chatroom button, but i didnt implemented it 
because of incompatibility between input output when using pynput keyboard listener module. Also, on windows, there is a commented line to break out from the program, uncomment that line 
and comment the Linux one. Otherwise it won't close when 'q' is pressed. If writeLogs parameter has been passed as true to keyogger class, it will also write all the input to a text. 
This is a good options since packet loss can happen between socket connections if there are some connection problems. Maybe i will write a simple email module later on to send log.txt 
to designated email. 


### Message Sizes

By default, a global HEADER_SIZE value has been set. Also, byterate has been chosen as 16. However byterate doesnt mean too much, because of header usage. HEADER_SIZE removes the limit from 
bit/byterates.

#### Feel free to ask any questions.
