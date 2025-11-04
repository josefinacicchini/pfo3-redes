import socket
import concurrent.futures
import time

# funcion que maneja el cliente en un hilo separado
def manejar_cliente(conn, addr):
    """
    Recibe la conexión (conn) y la dirección (addr) de un cliente.
    Procesa la tarea y envía una respuesta.
    """
    print(f"[NUEVA CONEXIÓN] {addr} conectado.")
    
    try:
        # recibe la tarea del cliente
        data = conn.recv(1024)
        if not data:
            print(f"[DESCONEXIÓN] {addr} se desconectó prematuramente.")
            return

        tarea_recibida = data.decode('utf-8')
        print(f"[TAREA RECIBIDA] de {addr}: {tarea_recibida}")

        # procesa la tarea
        print(f"[PROCESANDO] Tarea de {addr}...")
        time.sleep(15) # simulo de 15 segundos de trabajo
        resultado = f"'{tarea_recibida}' fue procesada."
        
        # envia el resultado de vuelta al cliente
        conn.sendall(resultado.encode('utf-8'))
        print(f"[RESPUESTA ENVIADA] a {addr}")
        
    except socket.error as e:
        print(f"[ERROR] Error con {addr}: {e}")
    finally:
        # cierra la conexión con este cliente
        conn.close()
        print(f"[CONEXIÓN CERRADA] {addr}.")

# configuracion del servidor
HOST = '127.0.0.1' 
PORT = 65432        
MAX_WORKERS = 5  #tamaño del pool de hilos

print("[INICIANDO] El servidor está arrancando...")

# ThreadPoolExecutor distribuye las tareas a los workers
with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))
        s.listen()
        print(f"[ESCUCHANDO] Servidor escuchando en {HOST}:{PORT}...")
        
        while True:
            conn, addr = s.accept()
            
            executor.submit(manejar_cliente, conn, addr)