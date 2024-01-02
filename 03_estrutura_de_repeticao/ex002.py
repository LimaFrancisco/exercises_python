"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. """

name = input("enter your name: ")
password = input("enter your password: ")

while name == password:
    print("ERROR: name and password can not be the seme")
    name = input("enter your name: ")
    password = input("enter your password: ")