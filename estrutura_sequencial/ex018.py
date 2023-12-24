"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). """

size = float(input("enter the size of a downloadable file in MB: "))
speed = float(input("inform the speed of the internet link in Mbps: "))

time = (size * 8) / speed

minutes = time // 60
seconds = time % 60

print(f"the file download will finish in {minutes:.0f}:{seconds:.0f} minutes")