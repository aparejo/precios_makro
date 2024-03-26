import subprocess
import time
import multiprocessing

def run_server():
    subprocess.Popen(['python', 'manage.py', 'runserver', '8001'])

def run_extraction_scripts():
    subprocess.Popen(['python', 'extrac.py']).wait()
    subprocess.Popen(['python', 'extrac1.py']).wait()
    subprocess.Popen(['python', 'extrac2.py']).wait()
    subprocess.Popen(['python', 'extrac3.py']).wait()
    subprocess.Popen(['python', 'extrac4.py']).wait()
    subprocess.Popen(['python', 'extrac_bcv.py']).wait()

if __name__ == '__main__':
    while True:
        # Crear los procesos para ejecutar las tareas en segundo plano
        server_process = multiprocessing.Process(target=run_server)
        extraction_process = multiprocessing.Process(target=run_extraction_scripts)

        # Iniciar los procesos en segundo plano
        server_process.start()
        extraction_process.start()

        # Esperar 45 minutos antes de volver a ejecutar las tareas
        time.sleep(2700)  # 2700 segundos = 45 minutos

        # Terminar los procesos actuales
        server_process.terminate()
        extraction_process.terminate()
        server_process.join()
        extraction_process.join()