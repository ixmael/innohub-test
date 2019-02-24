# Producir y consumir mensajes encriptados
Este ejercicio cuenta con productor de mensajes cifrados y un consumidor que descifra estos mensajes.

Sólo se implementó para ser utilizado con una REST API (se agrega el ejemplo básico de esta). La función de cifrado integrada es el cifrado César.

## Instalación
El archivo *requeriments.txt* tiene todos los requerimientos de Python para ejecutar este proyecto.

El proyecto require un archivo *.env* que sirve para proporcionar la configuración del productor y consumidor. Un ejemplo se encuentra en el archivo ".env.example".

Para instalar los módulos necesarios se ejecuta la siguiente instrucción:
```bash
pip -r requeriments.txt
```

## Producir mensajes
Para producir mensajes se utliza el siguiente comando:
```bash
python produce.py "MENSAJE A CIFRAR"
```

## Consumir mensajes
Para consumir de la REST API el mensaje (sólo se consulta el último mensaje existente) se utiliza el siguiente comando:
```bash
python consume.py
```
