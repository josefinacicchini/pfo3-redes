# Sistema Distribuido Cliente-Servidor con Sockets

Se implementa un modelo básico de cliente-servidor en Python utilizando sockets. 
El objetivo es demostrar cómo un servidor puede manejar múltiples clientes de forma concurrente.

## Para implementar el sistema:

1. Abrir una terminal y ejecutar el servidor: 

```python3 server.py```

2. Abrir tantas terminales como clientes se deseen, ejecutando: 

```python3 client.py "X tarea"```


> Para manejar múltiples clientes a la vez sin bloquearse, el servidor utiliza un Pool de Hilos con un máximo de 5 workers.
> Es decir, que puede procesar hasta 5 tareas de clientes simultáneamentáneamente. Si un sexto cliente se conecta mientras los 5 hilos están ocupados, su tarea quedará en una cola hasta que un hilo se libere.
> Para simular una tarea pesada, cada hilo realiza una pausa de 15 segundos antes de responder.
