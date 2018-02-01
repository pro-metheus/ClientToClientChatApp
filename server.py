#!/usr/bin/env python3.6


'''
simple client-to-client messenger server written in python

'''

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from pickle import dumps,loads
threads = []
connections = {}



def server_handler(client):
    client.send('enter your name'.encode())
    name = client.recv(1024).decode()
    connections[name] = client
    #updated dictionary
    print('*** user {0} has entered the application***'.format(name))
    while True:
        command = loads(client.recv(1024))
        code = str(command[0])
        print('code {0} recieved from {1}'.format(code, name))
        if code == '0': #client wants to know whos online
            online = list(connections.keys())
            client.send(dumps(online))
        elif code == '1': #client wants to send a message
            print('***entered sender***')
            print('sending')
            text = name+' : '+command[2]
            message = text.encode()
            if name == 'all':
                for person in connections:
                    connections[person].send(message)
            else:
                reciever = connections[command[1]]
                reciever.send(message)
            client.send('1'.encode())
            
        
        
    


if __name__ =='__main__':
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('127.0.0.1', 1234))
    server.listen(5)
    while True:
        client, addr = server.accept()
        t = Thread(target=server_handler, args=(client,))
        threads.append(t)
        t.start()
