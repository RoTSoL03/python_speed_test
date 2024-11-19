import tkinter as tk
import speedtest
from tkinter import *
from tkinter import messagebox, filedaialog, ttk

root = tk.Tk()
root.title("Python Speed Tester")

def speed_test():
  try:
    st = speedtest.Speedtest()
    st.get_best_server()
    #Perform download and upload test
    download_speed = st.download() / 1_000_000 #comvert from bits to megabits
    upload_speed = st.upload() / 1_000_000 #Convert from bits to megabits
    down_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
    up_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
  except Exception as e:
    messagebox.showerror("Error", f"An error occured {str(e)}")

title_label = tk.Label(root, text="Speed Test", font("Times", 30), bg="aliceblue")
title_label.place(x=170, y=20)

down_label = tk.Label(root, text="Download Speed: ", font=("Helvetica", 15), bg="aliceblue")
down_label.place(x=100, y=120)
up_label = tk.Label(root, text="Upload Speed: ", font=("Helvetica", 15), bg="aliceblue")
up_label.place(x=100, y=150)

test_btn = tk.Button(root, width=10, height=1, text='Test', border=1, bg='blue', cursor='hand2', fg='white', font=("Helvetica", 20), command=speed_test)
test_btn.place(x=180, y=270)

root.mainloop()
