#!/usr/bin/env python3
import sys
import time
import os
import urllib
import logging
import requests


try:
    import clipboard
except ImportError:
    import pip
    pip.main(['install', '--user', 'clipboard'])
    import clipboard

# set basicConfig
logging.basicConfig(filename='app.log', filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')


def get_current_script_path():
    return os.path.abspath(__file__)


def append_file_path(file_path):
    sys.path.append(file_path)


def check_internet():
    url = 'http://google.com'
    timeout = 3
    try:
        urllib.request.urlopen(url, timeout=timeout)
        return True
    except Exception as e:
        # time.asctime( time.localtime(time.time()))
        logging.error(str(time.asctime(time.localtime(time.time()))) + "  " + str(e))
        return False


def check_url_validity(url):
    if check_internet():
        # random video id
        r = requests.get(url)

        if "Video unavailable" in r.text:
            return False
        else:
            return True
    else:
        return None


def copy_id_into_clipboard(url, message='Ready for paste'):
    # split the url and get the youtube-video id
    youtube_video_id = url.split('/')[3]

    # this line of text copy id portion of your youtube video id  into clipboard
    clipboard.copy(youtube_video_id)
    print(f'{message}: {clipboard.paste()}')


if __name__ == "__main__":
    url = sys.argv[1]
    script_path = get_current_script_path()
    append_file_path(script_path)

    ret = check_url_validity(url)

    if ret is None:
        print('I don\'t sure this url is valid or not, check your internet connection.')
        copy_id_into_clipboard(url, "Probably your id is")
    elif ret:
        copy_id_into_clipboard(url)
    else:
        print("Your url is not valid.")
