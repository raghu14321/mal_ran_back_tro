import subprocess
import os
a = subprocess.check_output("whoami",shell=True)
if a == b'root\n':
    print("root found")
    print("installing requriements........................!")
    command = "python3 --version"
    abc = subprocess.check_output(command,shell=True)
    version = (abc[0:-7])
    try:
        if version == b'Python ':
            print("python3 found........!")
            os.system("apt install python3")
        else:
            subprocess.call("apt install python3",shell=True)
            print("python installed successfull.............!")
    except:
           print("python3 not installed :|")
           os.system("apt isntall python3")

    os.system("clear")
    os.system("""python3 -m venv myenv
    source myenv/bin/activate
    pip install opencv-python numpy
    pip install tkinter 
    pip install cryptography pyautogui pickle-mixin pillow""")
    print("ok")
    os.system("clear")
    os.system("sudo apt install python3-cryptography python3-pyautogui python3-pil")
    os.system("""sudo apt install pipx
    pipx install some-python-cli-tool""")
    os.system("sudo apt install python3-opencv python3-numpy")
else:
    print("operation not permitted\nrun as root ")

with open("zerofile.txt",mode='w') as file:
    file.write("0")

