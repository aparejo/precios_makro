import subprocess
import time
import multiprocessing

def run_server():
    subprocess.Popen(['python', 'manage.py', 'runserver', '8001'])

def run_extraction_scripts():
    subprocess.Popen(['python', 'extrac.py'])
    subprocess.Popen(['python', 'extrac_bcv.py'])

if __name__ == '__main__':
    # Crear los procesos para ejecutar las tareas en segundo plano
    server_process = multiprocessing.Process(target=run_server)
    extraction_process = multiprocessing.Process(target=run_extraction_scripts)

    # Iniciar los procesos en segundo plano
    server_process.start()
    extraction_process.start()

    # Continuar con el código del programa principal sin bloquear
    # ...

    # Esperar una hora antes de finalizar el programa
    time.sleep(3600)  # 3600 segundos = 1 hora

    # Opcionalmente, esperar a que los procesos finalicen antes de salir del programa
    server_process.join()
    extraction_process.join()