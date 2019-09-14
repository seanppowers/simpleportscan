import socket

#Simple Port Scanner

port_list = [21, 22, 23, 25, 80, 110, 143, 443, 445, 3389, 65432]

TIMEOUT_ERROR = "Server timed out on port "

def port_scanner():

    print("Enter a host name or IP Address: ")

    host = input().rstrip().lstrip()

    if len(host) < 3:
        print("Not a valid hostname or IP address!")

    for port in port_list:
        socket.setdefaulttimeout(2)
        socket.SOCK_STREAM
        s = socket.socket()

        try:
            s.connect((host, port))
            ans = s.recv(1024)
            print("Port " + str(port) + " RESPONDED: " + str(ans))
        except socket.timeout:
            print(TIMEOUT_ERROR + str(port))

port_scanner();
