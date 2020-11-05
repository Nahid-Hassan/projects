# Session Logout

Same as [Lock Screen][1]

```python
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
```

[1]: https://github.com/Nahid-Hassan/projects/blob/main/python-mini-scripts/lockscreen/README.md