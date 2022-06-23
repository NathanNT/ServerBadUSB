def client_call(hclient, command):
    hclient.send(command.encode('utf-8'))
    ans = hclient.recv(8192).decode()
    print(ans)
