# Lock Screen

## Subprocess - Subprocess Management

The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This module intends to replace several older modules and functions.

### Lock Screen Code Discussion

**import module**:

```python
try:
    import subprocess
except ImportError:
    pip.main(['install', '--user', 'subprocess'])
    import subprocess
```

Here if `subprocess` module is not install then raise an `ImportError`. If your `Internet` connection is okay then next it install using `pip`, `subprocess` module/package.

```python
pip.main(['install', '--user', 'subprocess']) # install package
```

**check_current_status()**:

```python
def check_current_status():
    # write your code here
    return None

flag = check_current_status()
```

If condition is satisfied then...

```python
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
```

**platform.system()** actually runs `uname` and potentially several other functions to determine the system type at `run time`.

```sh
In [1]: platform.system()
Out[1]: 'Linux' # for Linux system

In [1]: platform.system()
Out[1]: 'Windows' # for Windows system

In [1]: platform.system()
Out[1]: 'Darwin' # for Mac system
```

<details><summary>To know more about os.name, sys.platform and platform.system</summary>

The output of `sys.platform` and `os.name` are determined at `compile time`. `platform.system()` determines the system type at `run time`.

`sys.platform` is specified as a `compiler` define during the `build configuration`.
`os.name` checks whether certain os specific modules are available (e.g. `posix`, `nt`, ...)
`platform.system()` actually runs `uname` and potentially several other functions to determine the system type at `run time`.

My suggestion, use `os.name` to check whether it's a `posix-compliant system`, use `sys.platform` to check whether it's a `linux`, `cygwin`, `darwin`, `atheos`, whatever, and use `platform.system()`, well, if you don't believe the other `sources`.

</details>

**Details those line of code...**

```python
out = subprocess.run(['which', 'gnome-screensaver-command'], stdout=subprocess.PIPE, text=True)
```

`subprocess` is a python module that run shell/terminal command. Here we pass `command` as list first argument.

`stdout=subprocess.PIPE` return the `standard output` to `out` variable and `text=True` for return `string` instead of return `byte string`.

```sh
In [88]: out = subprocess.run(['which', 'gnome-screensaver-command'], stdout=subprocess.PIPE, text=True)
In [89]: out
Out[89]: CompletedProcess(args=['which', 'gnome-screensaver-command'], returncode=0, stdout='/usr/bin/gnome-screensaver-command\n')
In [90]: out.stdout
Out[90]: '/usr/bin/gnome-screensaver-command\n'
In [91]: out.returncode
Out[91]: 0 # return code 0 for success
```

Next we apply based on this `returncode` / `stdout text`. If it is don't raise any error.Then we run our command for `Linux`.

```python
subprocess.run('gnome-screensaver-command --lock', shell=True)
```

For `Windows`:

```python
ctypes.windll.user32.LockWorkStation()
```

If raise an error then for Linux we can solve this issue by running...

```python
subprocess.run('sudo apt-get install gnome-screensaver-command', shell=True)
```

=======================================  @Good Luck@  ============================================
