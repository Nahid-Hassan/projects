# clip.py

If clipboard is already not installed then first install it then import.

```py
try:
    import clipboard
except ImportError:
    import pip
    pip.main('install', '--user', 'clipboard')
    import clipboard
```

Return current script absolute path.

```py
os.path.abspath(__file__)
```

For globally run Python path.

```python
sys.path.append(file_path)
```

Logging error massage.

```py
logging.warning(str(time.asctime(time.localtime(time.time()))) + "  " + str(e))
```

Copy the id part into the clipboard.

```py
clipboard.copy(youtube_video_id)
```