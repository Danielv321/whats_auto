import sys, os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": [
    "pyautogui",
    "pyperclip",
    "webbrowser",
    "threading",
    "time",
    "os",
    "sys",
    "socket",
    "random",
    "selenium",
    "sqlalchemy"],
    "includes": ["PySimpleGUI"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="whats_auto",
    version="0.1",
    description="Enviador de mensagem",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py", base=base)]
)