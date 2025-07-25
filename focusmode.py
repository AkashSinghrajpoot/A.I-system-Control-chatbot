import time
import datetime
import ctypes
import os
from projectmain import speak

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    current_time = datetime.datetime.now().strftime("%H:%M")
    stop_time = input("Enter time in hour and minute format e.g., 01:20: ")

    host_path = r"//Cwindowpath"
    redirect = "127.0.0.1"
    print(current_time)

    speak("Enter the website name or URL, or for default, press 1")
    website_list = input("Enter website URL: ")
    my_list = []
    my_list.append(website_list)
    if website_list == "1":
        website_list = ["www.facebook.com", "www.youtube.com", "www.instagram.com"]
    else:
        website_list = my_list

    if current_time < stop_time:
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f"{redirect} {website}\n")
                    print("Done")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        website_list
        if current_time >= stop_time:
            with open(host_path, "r+") as file:
                content = file.readlines()
                file.seek(0)

                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
                print("Websites are unblocked")
                break
else:
    print("Cannot open focus mode")
    speak("Cannot open focus mode because you are not admin")
