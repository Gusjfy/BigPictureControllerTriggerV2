import subprocess
import time
import psutil
import os

TV_AUDIO_NAME = "SAMSUNG"


try:
    def is_steam_running():
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] and 'steam' in proc.info['name'].lower():
                return True
        return False

    def launch_big_picture():
        os.startfile("steam://open/bigpicture")

    def initialize_big_picture():
        subprocess.Popen(["steam", "-bigpicture"])

    def get_audio_device_index_by_name(partial_name):
        command = 'powershell -ExecutionPolicy Bypass -Command "Get-AudioDevice -List | Select-Object Index,Name"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        lines = result.stdout.strip().splitlines()

        for line in lines:
            if partial_name.lower() in line.lower():
                parts = line.strip().split(None, 1)
                if len(parts) == 2 and parts[0].isdigit():
                    return int(parts[0])
        return None

    def switch_audio_output(device_name):
        print("[AÇÃO] Trocando audio para TV. Lista de dispositivos:\n")
        index = get_audio_device_index_by_name(device_name)
        if index is not None:
            command = f'powershell -ExecutionPolicy Bypass -Command "Set-AudioDevice -Index {index}"'
            subprocess.run(command, shell=True)
            print(f"[OK] Saída de áudio trocada para: {device_name} (índice {index})\n")
            time.sleep(1)
        else:
            print("[ERRO] Dispositivo de áudio não encontrado.\n")    


    print("=== Script iniciado ===")
    
    switch_audio_output(TV_AUDIO_NAME)

    if is_steam_running():
        print("[INFO] Steam está aberta.\n")
        time.sleep(1)
        print("[AÇÃO] Abrindo Big Picture...\n")
        time.sleep(2)
        launch_big_picture()
    else:
        print("[INFO] Steam está fechada.\n")
        time.sleep(1)
        print("[AÇÃO] Abrindo Steam em modo Big Picture...\n")
        time.sleep(2)
        initialize_big_picture()
    
    time.sleep(2)

except Exception as e:
    # Captura qualquer erro e mostra no console
    print(f"Ocorreu um erro: {e}")
    input("Pressione qualquer tecla para continuar...")