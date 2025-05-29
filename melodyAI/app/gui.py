import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Melody AI")
root.geometry("800x500")
label = tk.Label(root, text="Enter Music Notes (ex: C4 D4 E4)", font=('Arial', 18))
label.pack(pady=20)
entry = tk.Entry(root, width=100)
entry.pack()
output_label = tk.Label(root, text="Generated Melody:", font=('Arial',15))
output_label.pack(pady=10)
output = tk.Text(root, height=4, width=100)
output.pack()
def generate_onclick():
    melody = generate()
button = tk.Button(root, text="Generate Melody", command=generate_onclick)
button.pack(pady=10)

root.mainloop()
