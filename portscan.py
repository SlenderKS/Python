import socket
#Baseado no do Guilherme Junqueira :D 


print("BEM VINDO A UM TESTADOR DE PORTAS !! \n")

ip = raw_input("Ip que desejas checar: ") 
port = int(raw_input("Porta:  "))



cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.settimeout(0.5)
codigo = cliente.connect_ex((ip,port))

if codigo == 0:
    print  port, "OPEN"
else:
    print  port, "CLOSE"
