import tkinter as tk
import subprocess
import fontstyle
window = tk.Tk()

window.title("Disability Abuser")
window.geometry("500x300")
window.configure(bg="#BDE0FE")

text = tk.Label(window, text="WELCOME!", bg="#BDE0FE", font=('arial black', 20))
text.pack(pady=20)

text = tk.Label(window, text="Welcome To Disability Suite", bg="#BDE0FE", font=('century', 15))
text.pack(pady=5)


def button1_clicked():
    subprocess.Popen(["python", "main.py"])


def button2_clicked():
    subprocess.Popen(["python", "test.py"])


button1 = tk.Button(window, text="Eye Movement Cursor Controller", font=("century", 10), bg="#457B9D", command=button1_clicked)
button1.place(width=500, height=100)
button1.config(width=30, height=2)
button1.pack(pady=10)
button2 = tk.Button(window, text="Hand Signs", font=("century", 10), bg="#457B9D", command=button2_clicked)
button2.place(width=500, height=100)
button2.config(width=30, height=2)
button2.pack(pady=10)

window.mainloop()
