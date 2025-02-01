import os
x = False
y = False
if os.path.exists('C:/WeDu/XVX_Browser/app'):
    x = True
    def remove_folder_recursively(folder_path):
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(folder_path)
    folder_path = 'C:/WeDu/XVX_Browser/app'
    remove_folder_recursively(folder_path)
    print('app folder has been deleted successfully')
if os.path.exists('C:/WeDu/XVX_Browser/unins000.exe'):
    y = True
    a = False
    try:
        os.startfile('C:/WeDu/XVX_Browser/unins000.exe')
    except OSError:
        a = True
        print('process canceled')
    if a is not True:
        print('the system started the normal uninstaller')
if y == False and x == False:
    print('''the compound uninstallation system had done nothing because both of 
main uninstaller and app folder doesn't exist''')