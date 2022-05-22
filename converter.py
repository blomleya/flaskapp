from pkg_resources import declare_namespace


def binary():
     binary = input("Please input your denery number to convert to binary : ")
     binary = int(binary)
     binary = bin(binary)[2:]
     print(binary)

def denery():
     denery = input("Please input your binary number to convert to denery : ")
     denery = int(denery, 2)
     print(denery)

def hexadecimal():
     hex1 = input("Please input your hex number to convert to denery : ")
     hex1 = int(hex1, 16)
     print(hex1)

def  dentohex():
     hexadecimal = input("Please input your denery number to convert to hex : ")
     hexadecimal = int(hexadecimal)
     hexadecimal = hex(hexadecimal)[2:]    
     print(hexadecimal)

 
 
 
answer = int(input()) 
 
if answer >= 1:
      denery() and denery() and hexadecimal() and dentohex()
