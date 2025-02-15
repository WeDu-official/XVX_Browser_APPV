import tkinter as tk
from tkinter import messagebox
import os
import shutil
import subprocess
import urllib.request
verify_req:bool = True
verify_rep:bool = True
fixed_false_keys = []
fixed_true_keys =  []
appname = "XVX Browser"
aboutapp = """it's a very basic and minimal Browser 
that its creators don't track you
because we don't track anyone, 
the source code is open, 
and we didn't hide anything
that tracks people or anything like that."""
apppath:str = "C:\\WeDu\\XVX_Browser\\app\\app\\XVX_Browser.exe"
unipath:str = "compound.exe"
repname:str = "Browser repairing"
repcheck:str = "C:\\WeDu\\XVX_Browser\\app"
reppath:str = ""
reppara:list = [0, 'C:\\WeDu\\XVX_Browser\\app.zip', '', '', 1, 'C:\\WeDu\\XVX_Browser\\app\\app\\XVX_Browser.exe', 0]
items:dict = {'WSBE': "this is an environment made for WeDu's software"}
right_items:dict = {}
falled_items:dict = {}
items_in_list:list = list(items.keys())
items_in_value:list = list(items.values())
paths_to_check:list = ['C:\\WeDu\\Python312']
wintitle:str = "XVX Browser - AAM"
right_list:list = []
falled_list:list = []
falled_list_paths:list = []
items_para = {'WSBE': [0, 'C:\\WeDu\\Python312.zip', '', 'https://github.com/WeDu-official/WeDu-Software-Base-Environment/releases/download/1.1b/Python312.zip', 1, 'C:\\WeDu\\Python312\\XBRI.exe', 1]}
icon:str = "logo.ico"
def create_ui():
    global paths_to_check,items_in_list, n
    window = tk.Tk()
    window.title(wintitle)
    if os.path.exists(icon):
        window.wm_iconbitmap(icon)
    # Calculate window size based on content (adjust as needed)
    window_width = 500  # Example width
    window_height = 300 # Example height
    window.geometry(f"{window_width}x{window_height}")
    window.minsize(500,300)
    # Define relative positions and sizes (using fractions of window size)
    listbox_x = 0.0
    listbox_y = 0.0
    listbox_width = 0.2
    listbox_height = 0.6
    listbox2_x = 0.2
    listbox2_y = 0
    listbox2_width = 0.2
    listbox2_height = 0.6
    iteminfo_x = 0.4
    iteminfo_y = 0.0
    iteminfo_width = 0.6
    iteminfo_height = 0.3
    appinfo_x = 0.4
    appinfo_y = 0.3
    appinfo_width = 0.6
    appinfo_height = 0.4
    log_x = 0.0
    log_y = 0.6
    log_width = 0.4
    log_height = 0.4
    buttons_y = 0.7 # common y for all buttons
    buttons_height = 0.3
    buttons_width = 0.20
    button_x_start = 0.4
    def log_message(message):
        log_text.config(state=tk.NORMAL)  # Make the Text widget editable temporarily
        log_text.insert(tk.END, message + "\n")  # Add newline for each message
        log_text.see(tk.END)  # Scroll to the bottom
        log_text.config(state=tk.DISABLED)  # Make it uneditable again
    def update_app_info(event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            selected_index = int(selection[0])  # Get the index of the selected item
            selected_item = widget.get(selected_index)
            if selected_item[:-3] in items:
                item_info_label.config(state=tk.NORMAL)  # Make the Text widget editable temporarily
                item_info_label.delete('1.0', tk.END)
                item_info_label.insert(tk.END, items[selected_item[:-3]])  # Add newline for each message
                item_info_label.config(state=tk.DISABLED)  # Make it uneditable again
            else:
                item_info_label.config(state=tk.NORMAL)  # Make the Text widget editable temporarily
                item_info_label.delete('1.0', tk.END)
                item_info_label.insert(tk.END, "No info is available for this item.")  # Add newline for each message
                item_info_label.config(state=tk.DISABLED)  # Make it uneditable again
    # Create widgets with relative positioning
    listbox = tk.Listbox(window, bg="red2")
    listbox2 = tk.Listbox(window, bg="spring green")
    log_frame = tk.Frame(window)
    log_text = tk.Text(log_frame, wrap=tk.NONE,bg="black",fg="green")
    log_message("Application started.")
    log_message("paths checking...")
    if len(items_in_list) == 0 and len(fixed_false_keys) == 0 and len(fixed_true_keys) == 0:
        log_message("NO PATHS TO BE CHECKED")
        log_message("'req. checker' case...")
        log_message('JOB ENDED')
    def check(path):
        if os.path.exists(path) and os.path.isdir(path):
            return True
        else:
            return False
    if verify_req is True:
        for item in range(len(items_in_list)):
            R = check(paths_to_check[item])
            if R is True:
                n = '(T)'
                right_list.append(items_in_list[item])
                log_message(f"'{items_in_list[item]}' path exists")
            if R is False:
                n = '(F)'
                falled_list.append(items_in_list[item])
                falled_list_paths.append(paths_to_check[item])
                log_message(f"'{items_in_list[item]}' path doesn't exist to install it hit 'Enter' while selecting the item")
                for ite_m in range(len(items)):
                    if items_in_list[ite_m] in falled_list:
                        falled_items.update({items_in_list[ite_m]: items_in_value[ite_m]})
                for ite_m2 in range(len(items)):
                    if items_in_list[ite_m2] in right_list:
                        right_items.update({items_in_list[ite_m2]: items_in_value[ite_m2]})
                        listbox2.insert(tk.END, items_in_list[ite_m2] + '(T)')
    else:
        for st1 in range(len(fixed_true_keys)):
            n = '(T)'
            right_list.append(fixed_true_keys[st1])
            log_message(f"'{fixed_true_keys[st1]}' exists")
        for st2 in range(len(fixed_true_keys)):
            n = '(F)'
            falled_list.append(fixed_false_keys[st2])
            log_message(f"'{fixed_false_keys[st2]}' doesn't exist")
    for ite_m in range(len(items)):
        if items_in_list[ite_m] in falled_list:
           falled_items.update({items_in_list[ite_m]: items_in_value[ite_m]})
    for ite_m2 in range(len(items)):
        if items_in_list[ite_m2] in right_list:
            right_items.update({items_in_list[ite_m2]: items_in_value[ite_m2]})
    for right in right_list:
            listbox2.insert(tk.END, right + '(T)')
    for fall in falled_list:
        listbox.insert(tk.END, fall + '(F)')
    def inst(option:int,name:str):
        if option == 0:
            listo = items_para.get(name)
        else:
            listo = reppara
        way = listo[6]
        if way == 1:
            log_message(f"'{name}(F)' is going to be installed via a .zip file from the Internet")
            url = listo[3]
            def download_file(url, filename):
               log_message(f"'{name}(F)' downloading the .zip file via the Internet...")
               try:
                   with urllib.request.urlopen(url) as response, open(filename, 'wb') as f:
                       f.write(response.read())
                       log_message(f"the .zip file({filename}) downloadation process for '{name}(F/T)' went successfully")
               except Exception as e:
                   log_message(f"ERROR!!, the .zip file({filename}) downloadation process for '{name}(F)' went unsuccessfully")
            # Example usage
            download_file(url, listo[1])
        if way == -1:
            log_message(f"'{name}(F)' is going to be installed via a .exe file from the Internet")
            url = listo[3]
            def download_file(url, filename):
               log_message(f"'{name}(F)' downloading the .exe file via the Internet...")
               try:
                   with urllib.request.urlopen(url) as response, open(filename, 'wb') as f:
                       f.write(response.read())
                       log_message(f"the .exe file({filename}) downloadation process for '{name}(F/T)' went successfully")
               except Exception as e:
                   log_message(f"ERROR!!, the .exe file({filename}) downloadation process for '{name}(F)' went unsuccessfully")
            # Example usage
            download_file(url, listo[1])
        if listo[0] == 1:
            try:
                shutil.move(listo[2], listo[1])
            except PermissionError:
                log_message(
                    f'ERROR!!, Permission denied for moving {listo[2]} from {os.path.dirname(os.path.abspath(listo[2]))} to {os.path.dirname(os.path.abspath(listo[1]))}')
        if way != -2 and way != -1:
            some_command = f'start cmd /k "cd {os.path.dirname(listo[1])} & powershell Expand-Archive {listo[1]} & echo the UNZIPPING IS successful IF the upper log showed that there aren\'t any problems or it was simply empty & timeout 5 & exit"'.replace('\\', '/')
            p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate() # This makes the wait possible
            p_status = p.wait()
            log_message(f"'{name}(F/T)' folder has been installed via a local .zip file")
        else:
            os.system(f'cmd /c "cd {os.path.dirname(listo[1])} & {listo[1]}"')
            while True:
                if messagebox.askyesno("NOTE",
                                       "ONLY WHEN THE OPENED FILE MISSION IS COMPLETE CLICK ON OK,NOTE: NO IS NEGLECTED AND MESSAGE WOULD SHOW AGAIN"):
                    log_message(f"'{name}(F/T)' folder has been installed via a local .exe file")
                    break
        def virf():
            log_message(f"'starting verification for {name}(F/T)' ...")
            if option == 0:
                RR = check(falled_list_paths[falled_list.index(name)])
            else:
                RR = check(repcheck)
            if RR is True:
                for i in range(listbox.size()):
                    if listbox.get(i)[:-3] == name:
                        right_list.append(listbox.get(i)[:-3])
                        right_items.update({listbox.get(i)[:-3]: falled_items.get(listbox.get(i)[:-3])})
                        falled_list.remove(listbox.get(i)[:-3])
                        falled_items.pop(listbox.get(i)[:-3])
                        listbox2.insert(tk.END, listbox.get(i)[:-3] + '(T)')
                        listbox.delete(i)
                        break
                log_message(f"'{name}(T)' installation has been verified")
            if RR is False:
                log_message(f"verification for '{name}(F)' has falled")
        if listo[4] == 1:
            os.system(f'cmd /c "cd {os.path.dirname(listo[5])} & {listo[5]}"')
            while True:
                if messagebox.askyesno("NOTE","ONLY WHEN THE OPENED FILE MISSION IS COMPLETE CLICK ON OK,NOTE: NO IS NEGLECTED AND MESSAGE WOULD SHOW AGAIN"):
                    if option == 0 and verify_req == True:
                        virf()
                    elif option == 1 and verify_rep == True:
                        virf()
                    else:
                        for i in range(listbox.size()):
                            if listbox.get(i)[:-3] == name:
                                right_list.append(listbox.get(i)[:-3])
                                right_items.update({listbox.get(i)[:-3]: falled_items.get(listbox.get(i)[:-3])})
                                falled_list.remove(listbox.get(i)[:-3])
                                falled_items.pop(listbox.get(i)[:-3])
                                listbox2.insert(tk.END, listbox.get(i)[:-3] + '(T)')
                                listbox.delete(i)
                                break
                        log_message(f"'{name}(T)' installation has been done")
                    break
        else:
            if option == 0 and verify_req == True:
                virf()
            elif option == 1 and verify_rep == True:
                virf()
            else:
                for i in range(listbox.size()):
                    if listbox.get(i)[:-3] == name:
                        right_list.append(listbox.get(i)[:-3])
                        right_items.update({listbox.get(i)[:-3]: falled_items.get(listbox.get(i)[:-3])})
                        falled_list.remove(listbox.get(i)[:-3])
                        falled_items.pop(listbox.get(i)[:-3])
                        listbox2.insert(tk.END, listbox.get(i)[:-3] + '(T)')
                        listbox.delete(i)
                        break
                log_message(f"'{name}(T)' installation has been done")
    def on_select_and_enter(event):
        if listbox.curselection():
            for i in listbox.curselection():
                inst(0,listbox.get(i)[:-3])
    listbox.bind('<Return>', on_select_and_enter)
    listbox.bind("<<ListboxSelect>>", update_app_info)
    listbox2.bind("<<ListboxSelect>>", update_app_info)
    listbox.place(relx=listbox_x, rely=listbox_y, relwidth=listbox_width, relheight=listbox_height)
    listbox2.place(relx=listbox2_x, rely=listbox2_y, relwidth=listbox2_width, relheight=listbox2_height)
    item_info_frame = tk.Frame(window, bg="maroon")
    item_info_frame.place(relx=iteminfo_x, rely=iteminfo_y, relwidth=iteminfo_width, relheight=iteminfo_height)
    item_info_label = tk.Text(item_info_frame, wrap=tk.NONE)
    item_info_label.insert(tk.END, "select any item to show it's info")
    xscrollbar1 = tk.Scrollbar(item_info_frame, orient=tk.HORIZONTAL, command=item_info_label.xview)
    xscrollbar1.pack(side=tk.BOTTOM, fill=tk.X)
    yscrollbar1 = tk.Scrollbar(item_info_frame, command=item_info_label.yview)
    yscrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
    item_info_label.config(xscrollcommand=xscrollbar1.set, yscrollcommand=yscrollbar1.set)
    item_info_label.pack(fill=tk.BOTH, expand=True)
    item_info_label.config(state=tk.DISABLED)# Make it initially uneditable
    app_info_frame = tk.Frame(window, bg="lightpink")
    app_info_frame.place(relx=appinfo_x, rely=appinfo_y, relwidth=appinfo_width, relheight=appinfo_height)
    app_info_label = tk.Text(app_info_frame, wrap=tk.NONE,bg="lightgray")
    app_info_label.insert(tk.END, aboutapp)
    xscrollbar2 = tk.Scrollbar(app_info_frame, orient=tk.HORIZONTAL, command=app_info_label.xview)
    xscrollbar2.pack(side=tk.BOTTOM, fill=tk.X)
    yscrollbar2 = tk.Scrollbar(app_info_frame, command=app_info_label.yview)
    yscrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
    app_info_label.config(xscrollcommand=xscrollbar2.set, yscrollcommand=yscrollbar2.set)
    app_info_label.pack(fill=tk.BOTH, expand=True)
    app_info_label.config(state=tk.DISABLED)# Make it initially uneditable
    log_frame.place(relx=log_x, rely=log_y, relwidth=log_width, relheight=log_height)
    # Create and configure scrollbars separately
    xscrollbar3 = tk.Scrollbar(log_frame, orient=tk.HORIZONTAL, command=log_text.xview)
    xscrollbar3.pack(side=tk.BOTTOM, fill=tk.X)
    yscrollbar3 = tk.Scrollbar(log_frame, command=log_text.yview)
    yscrollbar3.pack(side=tk.RIGHT, fill=tk.Y)
    log_text.config(xscrollcommand=xscrollbar3.set, yscrollcommand=yscrollbar3.set)
    log_text.pack(fill=tk.BOTH, expand=True)
    log_text.config(state=tk.DISABLED)# Make it initially uneditable
    greenbg = tk.Label(window,bg='lightgreen')
    greenbg.place(relx=button_x_start, rely=buttons_y, relwidth=1.0, relheight=buttons_height)
    def Open():
        os.system(f'cmd /c "cd {os.path.dirname(apppath)} & {apppath}"')
    def Uninstall():
        if messagebox.askyesno("confirmation", "Are you sure you want to close?"):
            os.system(f'cmd /c "cd {os.path.dirname(unipath)} & {unipath}"')
            exit()
        else:
            pass
    def Repair():
        inst(1,repname)
    def makebutton():
        button1 = tk.Button(window, text="Open",command=Open, bg="darkgreen", font=('Helvetica', 12, 'bold'))
        button1.place(relx=button_x_start, rely=buttons_y, relwidth=buttons_width, relheight=buttons_height)
        button2 = tk.Button(window, text="Repair",command=Repair, bg="yellow", font=('Helvetica', 12, 'bold'))
        button2.place(relx=button_x_start + buttons_width, rely=buttons_y, relwidth=buttons_width, relheight=buttons_height)
        button3 = tk.Button(window, text="Uninstall",command=Uninstall, bg="red", font=('Helvetica', 12, 'bold'))
        button3.place(relx=button_x_start + 2*buttons_width, rely=buttons_y, relwidth=buttons_width, relheight=buttons_height)
    makebutton()
    window.mainloop()
create_ui()