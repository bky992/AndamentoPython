#Arquivo de estudo python da minha evolução na linguagem, alterado constantemente.

import pyfiglet
import os

ascii_banner = pyfiglet.figlet_format("Central do estudo")
print(ascii_banner)

#O começo
print("Selecione algo:")
print("[1] Registro de Palavras")
print("[2] Calculadora da Adição")

#Registro de Palavras
valor = int(input(' > '))
if valor == 1:
     os.system('clear')
ascii_banner2 = pyfiglet.figlet_format("Registro")
print(ascii_banner2)
palavra = input('Digite qualquer coisa para ser registrada abaixo: ')
print("[+] Resultado:", palavra)
input('Aperte Enter para voltar ao início')
os.system("clear")

#Volta do começo após execução da tarefa desejada
ascii_banner = pyfiglet.figlet_format("Central do estudo")
print(ascii_banner)

print("Selecione algo:")
print("[1] Registro de Palavras")
print("[2] Calculadora da Adição")
valor = int(input(' > '))

#Calculadora da Adição
if valor == 2:
    os.system('clear')
ascii_banner3 = pyfiglet.figlet_format("Calculadora de Adicao")
print(ascii_banner3)
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print("[+] O resultado da soma é:")
print(num1 + num2)
input("Aperte ENTER para voltar ao início.")
