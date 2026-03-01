Metrónomo Pro: Interfaz Gráfica y Programación Multihilo 

Este proyecto es una aplicación de escritorio desarrollada en Python que implementa un metrónomo funcional con una interfaz gráfica intuitiva. 
El enfoque técnico principal fue la gestión de procesos en paralelo (Multithreading) para asegurar una precisión rítmica constante sin bloquear la respuesta de la interfaz de usuario.

🚀 Características Técnicas
Precisión Rítmica: Implementación de un ciclo de 4 tiempos con sonidos diferenciados (acentuación en el tiempo 1).
Multithreading: Uso de la librería threading para ejecutar el bucle del metrónomo en un hilo independiente, permitiendo que la interfaz siga respondiendo a los comandos del usuario.
Interfaz Gráfica (GUI): Desarrollada con Tkinter, incluyendo personalización estética mediante carga de imágenes externas (Pillow).
Gestión de Audio: Integración con Pygame.mixer para una reproducción de sonido de baja latencia.

🛠️ Tecnologías Utilizadas
Python 3.x
Tkinter: Construcción de la interfaz de usuario.
Threading: Manejo de concurrencia para el bucle de tiempo.
Pygame: Motor de audio para la reproducción de los archivos .wav.
Pillow (PIL): Procesamiento y redimensionamiento de imágenes de fondo.

🧠 Conceptos Avanzados Aplicados
Concurrencia (Hilos): Se utilizó un hilo daemon para que el metrónomo se detenga automáticamente al cerrar la ventana principal, evitando procesos huérfanos.
Lógica de Tiempos: Implementación de un contador modular (i % 4) + 1 para diferenciar auditivamente el primer tiempo de cada compás.
Manejo de Rutas y Archivos: Uso de os.path para garantizar que el programa encuentre los recursos (sonidos e imágenes) independientemente de la carpeta donde se ejecute.

📝 Notas de Desarrollo
Este proyecto fue creado para demostrar la integración de múltiples librerías externas en una solución cohesiva. 
La lógica de sincronización fue refinada mediante desarrollo asistido por IA, asegurando que los intervalos de tiempo (time.sleep) 
fueran lo suficientemente precisos para el uso musical básico.
