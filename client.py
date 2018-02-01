
from socket import socket, AF_INET, SOCK_STREAM

from pickle import dumps,loads



def client_handler():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 1234))
    handshake = client.recv(1024).decode()
    name = input(handshake)
    client.send(name.encode())
    while True:
        code = input('Enter 0 for seeing online list\n1 for sending message\n2 for viewing messages\n~')
        if code == '0':
            print('***refreshing***')
            message = ['0','whos online?']
            client.send(dumps(message))
            print('refresing...')
            online = loads(client.recv(1024))
            for person in online:
                print('(.)'+person)
            print('\n')
        if code == '1':
            print('use all//message for broadcase')
            message = input('enter username//message  :')
            uname,message=message.split('//')
            message = dumps([1, uname, message])
            client.send(message)
            error = client.recv(1024).decode()
            if error == '1':
                print('**message sent**')
        if code == '2':
            new = client.recv(1024).decode()
            print(new)


if __name__ =='__main__':
    client_handler()
