import subprocess
w = open('PCC.txt','w')
w.write('True')
w.close()
subprocess.Popen('C:/WeDu/Python312/python.exe main3.py', creationflags=subprocess.CREATE_NO_WINDOW)