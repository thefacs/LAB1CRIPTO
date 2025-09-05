#!/usr/bin/env python3

import sys

def caesar_encrypt(texto, desplazamiento):
    resultado = []
    for ch in texto:
        if 'a' <= ch <= 'z':  # solo minúsculas
            nuevo = (ord(ch) - ord('a') + desplazamiento) % 26
            resultado.append(chr(nuevo + ord('a')))
        else:
            resultado.append(ch)  # deja los caracteres que no son minúsculas
    return ''.join(resultado)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 cesar.py \"texto\" desplazamiento")
        sys.exit(1)
    
    texto = sys.argv[1]
    desplazamiento = int(sys.argv[2])
    
    cifrado = caesar_encrypt(texto, desplazamiento)
    print(cifrado)
