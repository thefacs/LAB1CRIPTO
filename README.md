# LAB1CRIPTO

# Laboratorio 1 – Cifrado César, Stealth ICMP y MitM

## Descripción
Este repositorio contiene todos los códigos y archivos utilizados para el Informe del Laboratorio 1 de Criptografía y Seguridad en Redes.  
Se implementaron las siguientes actividades:

1. **Cifrado César (Actividad 1)**  
   - Script en Python que cifra texto usando el algoritmo César con un desplazamiento configurable.

2. **Transmisión Stealth mediante ICMP (Actividad 2)**  
   - Script en Python que envía un mensaje cifrado carácter por carácter en paquetes ICMP simulando un ping normal.
   - Se mantiene coherencia en timestamp, ID, sequence number y payload.

3. **Recuperación del mensaje mediante MitM (Actividad 3)**  
   - Script en Python que captura los paquetes ICMP enviados en la Actividad 2, genera todas las combinaciones posibles de descifrado y resalta el mensaje más probable.

## Estructura del repositorio

