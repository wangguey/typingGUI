from cx_Freeze import setup, Executable
import sys
pyfile = "Typing.py"
base = None
if sys.platform == "win32":
    base = "Win32GUI" 

options = {
    'build_exe': {
        'packages':["os"],
        'include_files': [],
        "optimize" : 2
    },
}

setup(
    name = "typing",
    options = options,
    version = "2.0",
    description = 'My typing',
    executables = [Executable(pyfile, base=base, icon = "type.ico",shortcutName="typing",shortcutDir="StartMenuFolder" )],
    author = 'spring'
) 