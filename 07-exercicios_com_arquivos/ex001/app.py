"""Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
    O arquivo de entrada possui o seguinte formato: 
    
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato: 

[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""

def check_ip(ip):
    octet = ""
    ip += "."

    for item in ip:
        if item.isdigit():
            octet += item
        else:
            octet = int(octet) 
            if octet < 0 or octet > 255:
                return False
            else:
                octet = ""
    
    return True

file = open("ex001/ip.txt","r")

ips_list = list(file)

file.close()

for index in range(0, len(ips_list)):
    ips_list[index] = ips_list[index].replace("\n","")

valid = open("ex001/valid_ips.txt", "x")
invalid = open("ex001/invalid_ips.txt", "x")

valid.write("[valid addresses:]\n")
invalid.write("[invalid addresses:]\n")

for ip in ips_list:
    if check_ip(ip):
        valid.write(ip + "\n")
    else:
        invalid.write(ip + "\n")

valid.close()
invalid.close()
