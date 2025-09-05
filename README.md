# LAB1CRIPTO

# Laboratorio 1 – Cifrado César, Stealth ICMP y MitM

## Descripción
Este repositorio contiene todos los códigos y archivos utilizados para el Informe del Laboratorio 1 de Criptografía y Seguridad en Redes.  
Se implementaron las siguientes actividades:

1. **Cifrado César (Actividad 1)**  
   - Script en Python que cifra texto usando el algoritmo César con un desplazamiento configurable.  
   - Comando para ejecutar el programa:  
     ```bash
     sudo python3 act1_cesar.py "criptografia y seguridad en redes" 9
     ```

2. **Transmisión Stealth mediante ICMP (Actividad 2)**  
   - Script en Python que envía un mensaje cifrado carácter por carácter en paquetes ICMP simulando un ping normal.  
   - Se mantiene coherencia en timestamp, ID, sequence number y payload.  
   - Comando para ejecutar el programa:  
     ```bash
     sudo python3 act2_stealth.py 8.8.8.8 "larycxpajorj h bnpdarmjm nw anmnb"
     ```

3. **Recuperación del mensaje mediante MitM (Actividad 3)**  
   - Script en Python que captura los paquetes ICMP enviados en la Actividad 2, genera todas las combinaciones posibles de descifrado y resalta el mensaje más probable.  
   - Comando para ejecutar el programa:  
     ```bash
     sudo python3 act3_mitm.py lab1v2.pcapng
     ```



