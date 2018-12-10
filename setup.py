# Run the build process by running the command 'python setup.py build'
import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
        name = "MouseFollow",
        version = "0.1",
        description = "A Laser Pointer For Presenter View",
        executables = [Executable("MouseFollow.py",
                                  icon = "pointer.ico",
                                  base = base)])

# You have to include the cpyHook.py file manually from the pyHook library
