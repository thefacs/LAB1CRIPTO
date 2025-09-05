#!/usr/bin/env python3
# Requiere: scapy
# Uso: sudo python3 act2.py <IP_DESTINO> "mensaje_a_enviar"

import sys
import time
from scapy.all import IP, ICMP, send

def enviar_stealth(ip_destino, mensaje, ip_id=0x1000, icmp_id=0x1234, seq_start=1, iface=None):
    """
    Envía un mensaje carácter por carácter en paquetes ICMP Echo Request
    simulando un ping normal de 56 bytes (8 ICMP + 48 payload).
    Mantiene coherencia en:
      - timestamp (delay entre envíos)
      - Identification (IP.id incremental)
      - Seq number (ICMP.seq incremental)
      - ICMP.id constante
      - Payload ICMP (mantiene primeros 8 bytes y área de datos)
    """
    if len(mensaje) == 0:
        print("El mensaje está vacío")
        return
    
    for i, ch in enumerate(mensaje):
        # Payload de 48 bytes: 1 byte del carácter + 47 bytes de relleno
        payload = ch.encode('latin1') + b'\x00' * 47
        
        ip = IP(dst=ip_destino, id=ip_id + i)
        icmp = ICMP(type=8, id=icmp_id, seq=seq_start + i) / payload
        
        pkt = ip / icmp
        send(pkt, iface=iface, verbose=False)
        
        print(f"Enviado paquete: IP.id={ip_id+i} ICMP.id={icmp_id} seq={seq_start+i} char='{ch}'")
        
        # Delay para simular tráfico natural y no levantar sospechas
        time.sleep(0.2)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: sudo python3 act2.py <IP_DESTINO> \"mensaje\"")
        sys.exit(1)
    
    ip_destino = sys.argv[1]
    mensaje = sys.argv[2]
    
    enviar_stealth(ip_destino, mensaje)
