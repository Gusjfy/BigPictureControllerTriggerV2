import ctypes
import os
import time
import psutil
import subprocess
import sys
import tempfile

XINPUT_DLL_NAMES = ["xinput1_4.dll", "xinput1_3.dll", "xinput9_1_0.dll"]

try:
    # Verifica se o script está sendo executado a partir de um pacote PyInstaller
    if hasattr(sys, '_MEIPASS'):
        # Caminho temporário para os arquivos extraídos
        base_path = sys._MEIPASS
    else:
        # Caminho normal (para desenvolvimento)
        base_path = os.path.dirname(os.path.abspath(__file__))

    xinput = None
    for dll_name in XINPUT_DLL_NAMES:
        try:
            xinput = ctypes.windll.LoadLibrary(dll_name)
            break
        except OSError:
            continue

    if not xinput:
        raise ImportError("Não foi possível carregar a DLL do XInput.")

    class XINPUT_GAMEPAD(ctypes.Structure):
        _fields_ = [
            ("wButtons", ctypes.c_ushort),
            ("bLeftTrigger", ctypes.c_ubyte),
            ("bRightTrigger", ctypes.c_ubyte),
            ("sThumbLX", ctypes.c_short),
            ("sThumbLY", ctypes.c_short),
            ("sThumbRX", ctypes.c_short),
            ("sThumbRY", ctypes.c_short),
        ]

    class XINPUT_STATE(ctypes.Structure):
        _fields_ = [
            ("dwPacketNumber", ctypes.c_ulong),
            ("Gamepad", XINPUT_GAMEPAD),
        ]

    def is_controller_connected():
        state = XINPUT_STATE()
        result = xinput.XInputGetState(0, ctypes.byref(state))
        return result == 0

    already_triggered = False

    # Função para encontrar o caminho correto do arquivo 'visible_action.py'
    def get_visible_action_path():
        script_path = os.path.join(base_path, "visible_action.py")
        return script_path.replace("\\", "\\\\")

    while True:
        if is_controller_connected() and not already_triggered:
            # Extraímos o script e executamos ele
            script_path = get_visible_action_path()
            subprocess.Popen(["python", script_path])  # Executando o script visível
            already_triggered = True
        elif not is_controller_connected():
            already_triggered = False
        time.sleep(2)

except Exception as e:
    # Captura qualquer erro e mostra no console
    print(f"Ocorreu um erro: {e}")
    input("Pressione qualquer tecla para continuar...")
