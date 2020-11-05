import os
import pip
import platform

try:
    import subprocess
except ImportError:
    pip.main(['install', '--user', 'subprocess'])
    import subprocess

'''
    If condition is match then lock your laptop or desktop screen.
'''

def check_current_status():
    # write your code here
    return None

flag = check_current_status()

if flag:
    if platform.system() == 'Linux':
        out = subprocess.run(
            ['which', 'gnome-screensaver-command'], stdout=subprocess.PIPE, text=True)
        if len(out.stdout) == 0:
            subprocess.run(
                'sudo apt-get install gnome-screensaver-command', shell=True)
        else:
            subprocess.run('gnome-screensaver-command --lock', shell=True)
    elif platform.system() == 'Windows':
        try:
            import ctypes
        except ImportError:
            pip.main(['install', '--user', 'ctypes'])
            import ctypes

        ctypes.windll.user32.LockWorkStation()
    elif platform.system() == 'Darwin':
        print("Not implemented for Mac System")
