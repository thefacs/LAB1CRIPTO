#!/usr/bin/env python3
# Uso: python3 descifrar_cesar_pcap.py archivo.pcapng

import sys
from scapy.all import rdpcap, ICMP
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for ch in texto:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            resultado += chr((ord(ch) - base - desplazamiento) % 26 + base)
        else:
            resultado += ch
    return resultado

def es_probable(texto):
    """
    Heurística simple: verificamos si contiene palabras comunes en español
    relacionadas con seguridad y criptografía.
    """
    comunes = ["criptografia", "seguridad", "redes", "clave", "mensaje", "texto", "usach"]
    for palabra in comunes:
        if palabra in texto.lower():
            return True
    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 descifrar_cesar_pcap.py archivo.pcapng")
        sys.exit(1)

    archivo_pcap = sys.argv[1]
    paquetes = rdpcap(archivo_pcap)

    # Reconstruir mensaje a partir de payloads ICMP
    mensaje_reconstruido = ""
    for pkt in paquetes:
        if ICMP in pkt and pkt[ICMP].type == 8:  # Echo Request
            data = bytes(pkt[ICMP].payload)
            if len(data) > 0:
                mensaje_reconstruido += data[0:1].decode(errors="ignore")

    print(f"Mensaje reconstruido (crudo): {mensaje_reconstruido}\n")
    print("Todas las combinaciones posibles:")

    mejor_opcion = None
    mejor_texto = ""

    for shift in range(26):
        descifrado = descifrar_cesar(mensaje_reconstruido, shift)
        if es_probable(descifrado):
            mejor_opcion = shift
            mejor_texto = descifrado
            print(Fore.GREEN + f"[shift={shift}] {descifrado}" + Style.RESET_ALL)
        else:
            print(f"[shift={shift}] {descifrado}")

    if mejor_opcion is not None:
        print("\nPosible mensaje en claro:")
        print(Fore.GREEN + f"[shift={mejor_opcion}] {mejor_texto}" + Style.RESET_ALL)
    else:
        print("\nNo se encontró un candidato claro, revise manualmente las opciones.")
