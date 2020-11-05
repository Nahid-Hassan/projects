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
            ['which', 'gnome-session-quit'], stdout=subprocess.PIPE, text=True)
        if len(out.stdout) == 0:
            subprocess.run(
                'sudo apt-get install gnome-session-quit', shell=True)
        else:
            subprocess.run('gnome-session-quit --no-prompt', shell=True)
    elif platform.system() == 'Windows':
        os.system("shutdown -l")
    elif platform.system() == 'Darwin':
        print("Not implemented for Mac System")
