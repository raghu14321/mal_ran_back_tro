import os
try:
    with open("zerofile.txt",mode='r')as file:
        files = file.read()
    if files == "0":
        print("already installed.................!")
        #os.system("rm -rf req.py")
        exit()
    else:
        os.system("sudo python3 req.py")

except FileNotFoundError:
    os.system("sudo python3 req.py")
#os.system("rm -rf req.py")