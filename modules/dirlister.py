import os

def run(**args):
    print("[*] In dirlister module.")
    files = os.listdr(".")
    return str(files)