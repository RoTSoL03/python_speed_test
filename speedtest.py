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
