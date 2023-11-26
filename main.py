import socket
import Encryption_Methods as ae

port = 1234

joh = int(input("1 : Host \n2 : Join \nInput : "))    
if joh == 1:
      #!Server Part
    name = input("Enter Your Name : ")
    s = socket.socket()
    host = socket.gethostname()

    print('server will start on host : ',host)

    s.bind((host,port))
    print("server is bound successfully\n")

    s.listen(5)
   
    co,ad = s.accept()
    
    name = name.encode()
    co.send(name)
   
    client_name = co.recv(1024).decode()
    print(f'{client_name} Has Joined')
    
    
    while True :
        responce = input("\nYou : ").encode()
        m5_ha = ae.md5(responce)
        
        co.send(responce)
        co.send(m5_ha)
        print(f'" {responce.decode()} " Is Hashed To : {m5_ha} \n')

        
        responce = co.recv(1024)
        m5_ha = co.recv(1024)
        print(f"Received  Text From ' {client_name} ' Is : ",responce)
        print(f"MD5 Hash Recived From ' {client_name} ' Is : ",m5_ha)
        
else:
     name = input("Enter Your Name : ")
     client = input("Enter host name : ")
     s = socket.socket()
     s.connect((client,port))
    
     name = name.encode()
     s.send(name)
     print("\nconnected to server\n")
    
     client_name = s.recv(1024).decode()
     while True:
         
         responce = s.recv(1024)
         m5_ha = s.recv(1024)
         print(f"Received  Text From ' {client_name} ' Is : ",responce)
         print(f"MD5 Recived From ' {client_name} ' Is : ",m5_ha)
         
         responce = input("\nYou : ").encode()
         m5_ha - ae.md5(responce)
         s.send(responce)
         s.send(m5_ha)
         print(f'" {responce.decode()} " Is Hashed To : {m5_ha} \n')
         