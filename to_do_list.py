

import tkinter as tk
from tkinter import messagebox

# Functions
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_task():
    try:
        selected_task = tasks_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            tasks_listbox.delete(selected_task)
            tasks_listbox.insert(selected_task, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except:
        messagebox.showwarning("Warning", "Please select a task to update!")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Input box
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Buttons
add_btn = tk.Button(root, text="Add Task", command=add_task, width=15, bg="lightgreen")
add_btn.pack(pady=5)

update_btn = tk.Button(root, text="Update Task", command=update_task, width=15, bg="lightblue")
update_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task, width=15, bg="tomato")
delete_btn.pack(pady=5)

# Task List
tasks_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
tasks_listbox.pack(pady=10)

# Run app
root.mainloop()
