import socket
import sys

HOST = '127.0.0.1'
PORT = 65432

try:
    tarea_a_enviar = " ".join(sys.argv[1:])
    if not tarea_a_enviar:
        tarea_a_enviar = "Tarea por defecto"
except IndexError:
    tarea_a_enviar = "Tarea por defecto"


# crea el socket del cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # conecta al servidor
        print(f"Conectando a {HOST}:{PORT}...")
        s.connect((HOST, PORT))
        
        # envia la tarea 
        print(f"Enviando tarea: '{tarea_a_enviar}'")
        s.sendall(tarea_a_enviar.encode('utf-8'))
        
        # recibe el resultado del servidor 
        data = s.recv(1024)
        
        print(f"[RESPUESTA RECIBIDA] {data.decode('utf-8')}")
        
    except socket.error as e:
        print(f"[ERROR] No se pudo conectar o comunicar: {e}")
    finally:
        print("Conexión cerrada.")