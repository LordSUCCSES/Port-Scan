from time import sleep
from os import system
import socket

class color ():
    PURPLE = "\033[0;35m"
    RED = "\033[0;31m"
    BLUE = "\033[0;34m"
    END = "\033[0m"

file_save = False
banner = color.BLUE + ("""   _ \               |         ___|                                         
  |   |  _ \    __|  __|     \___ \    __|   _` |  __ \   __ \    _ \   __| 
  ___/  (   |  |     |             |  (     (   |  |   |  |   |   __/  |    
 _|    \___/  _|    \__|     _____/  \___| \__,_| _|  _| _|  _| \___| _|    
                                   GitHub: https://github.com/LordSUCCSES
                                                                            """) + color.END

ports = []
bulunan = 0

def soruu():
    global file_save
    soru = str(input("Bulunan Port Dosya'ya Kaydedilsin Mi? (Ör: Y/N): ")).upper()
    if soru == "Y":
        file_save = True
    elif soru == "N":
        file_save = False
    else:
        print("Lütfen Geçerli Harf Giriniz")
        soruu()

def scan():
    system('clear')
    print(banner)
    global bulunan
    ip = input("IP Girin: ")
    soruu()
    for port in range(65535):
        try:
            addr = (ip, port)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.settimeout(0.000001)
            server.connect(addr)
            print(color.BLUE + "[+] Port Bulundu: " + color.PURPLE + f"{port}" + color.END)
            ports.append(port)
            bulunan += 1
            if file_save == True:
                with open("bulundu.txt", "a") as file:
                    file.write(str(port) + "\n")
        except:
            print(color.RED + "[-] Port Bulunamadı: " + color.BLUE + f"{port}" + color.END)
    if bulunan > 0:
        print(color.BLUE + f"[+] {bulunan} Tane Port Bulundu")
        print(color.BLUE + "*****************Portlar*****************")
        print("""Port | Protokol | Açık|Kapalı""")
        leng = len(ports)
        for i in ports:
            print(str(i) + "      TCP " + "        Açık")
        print("*****************************************" + color.END)
        sleep(10)
    else:
        print(color.RED + "[-] Hiçbir Port Bulunamadı" + color.END)
        sleep(10)

scan()