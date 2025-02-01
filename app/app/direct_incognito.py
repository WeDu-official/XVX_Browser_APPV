import subprocess
w = open('PCC.txt','w')
w.write('True')
w.close()
subprocess.Popen('C:/WeDu/Python312/python.exe maincognito.py', creationflags=subprocess.CREATE_NO_WINDOW)