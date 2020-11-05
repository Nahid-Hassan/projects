import urllib.request
import requests
import socket
import os

try:
    import http.client as httplib
except ImportError:
    import pip
    pip.main('install', '--user', 'http')

# method - 1


def checkInternetHttplib(url="www.google.com", timeout=3):
    conn = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False


# method - 2
def checkInternetSocket(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False


# method - 3
def checkInternetRequests(url='http://www.google.com/', timeout=3):
    try:
        #r = requests.get(url, timeout=timeout)
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        print(ex)
        return False


# method - 4
def checkInternetUrllib(url='http://google.com', timeout=3):
    try:
        urllib.request.urlopen(url, timeout=timeout)
        return True
    except Exception as e:
        print(e)
        return False
