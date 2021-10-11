import socket

def logo():
    print('#########  #########  ######### ########## #       # ######### ############ #########')
    print('#       #  #       #  #       #    ###     #       # #       #     ###      #        ')
    print('#########  #       #  #       #    ###     ######### #########     ###      #########')
    print('#       #  #       #  #       #    ###     #       # #       #     ###              #')
    print('#       #  #########  #########    ###     #       # #       #     ###      #########')

    input_func()


def socket_func(ip,first,last):

    try:

        for port in range(first,last):

            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_.settimeout(2)

            response = socket_.connect_ex((ip,port))

            if response == 0:
                print(f'open port : {port}')

    except KeyboardInterrupt:
        print("Scan stopped ( CTRL + C")

    except socket.error:
        print('Connection ERROR!!!!')


def  input_func():

    domain = input('Enter Domain or IP you want to scan : ')
    ip  = socket.gethostbyname(domain)

    first , last = input('Enter ip range ex:1 100 :').split()

    first = int(first.replace("'",""))
    last  = int(last.replace("'",""))

    print(f'Scaning domain : {domain} ip : {ip} in ({first},{last}) range')

    socket_func(ip,first,last)

logo()
