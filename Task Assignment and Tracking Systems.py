import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# Initialize main window
root = tk.Tk()
root.title("Task Assignment & Tracking System")
root.geometry("700x550")
root.configure(bg="#f2f4f7")

# Styles for a polished look
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=6)
style.configure("TLabel", background="#f2f4f7", font=("Helvetica", 11))
style.configure("Header.TLabel", font=("Helvetica", 18, "bold"), background="#f2f4f7")

# Task list to store tasks
tasks = []

# Function to add a new task
def add_task():
    title = entry_title.get()
    assignee = entry_assignee.get()
    deadline = entry_deadline.get()
    
    if title and assignee and deadline:
        try:
            datetime.strptime(deadline, "%Y-%m-%d")  # Check date format
            task = {"title": title, "assignee": assignee, "deadline": deadline, "status": "Incomplete"}
            tasks.append(task)
            update_task_list()
            entry_title.delete(0, tk.END)
            entry_assignee.delete(0, tk.END)
            entry_deadline.delete(0, tk.END)
            messagebox.showinfo("Success", "Task added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter the deadline in YYYY-MM-DD format.")
    else:
        messagebox.showwarning("Warning", "Please fill out all fields")

# Function to delete selected task
def delete_task():
    selected_item = task_list.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a task to delete")
        return

    task_index = int(selected_item[0][1:]) - 1
    tasks.pop(task_index)
    update_task_list()
    messagebox.showinfo("Success", "Task deleted successfully")

# Function to mark task as complete
def mark_complete():
    selected_item = task_list.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a task to mark as complete")
        return

    task_index = int(selected_item[0][1:]) - 1
    tasks[task_index]["status"] = "Complete"
    update_task_list()
    messagebox.showinfo("Success", "Task marked as complete")

# Function to update task list display
def update_task_list():
    task_list.delete(*task_list.get_children())
    for i, task in enumerate(tasks, start=1):
        task_list.insert('', 'end', iid=i, values=(task["title"], task["assignee"], task["deadline"], task["status"]))

# Header Label
header_label = ttk.Label(root, text="Task Assignment & Tracking System", style="Header.TLabel")
header_label.pack(pady=(20, 10))

# Task entry form
frame_form = tk.Frame(root, bg="#f2f4f7")
frame_form.pack(pady=10)

ttk.Label(frame_form, text="Task Title:", style="TLabel").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
entry_title = ttk.Entry(frame_form, width=30)
entry_title.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame_form, text="Assignee:", style="TLabel").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
entry_assignee = ttk.Entry(frame_form, width=30)
entry_assignee.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(frame_form, text="Deadline (YYYY-MM-DD):", style="TLabel").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
entry_deadline = ttk.Entry(frame_form, width=30)
entry_deadline.grid(row=2, column=1, padx=10, pady=5)

# Buttons for adding, deleting, and marking tasks as complete
frame_buttons = tk.Frame(root, bg="#f2f4f7")
frame_buttons.pack(pady=10)

btn_add = ttk.Button(frame_buttons, text="Add Task", command=add_task, style="TButton")
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_delete = ttk.Button(frame_buttons, text="Delete Task", command=delete_task, style="TButton")
btn_delete.grid(row=0, column=1, padx=5, pady=5)

btn_complete = ttk.Button(frame_buttons, text="Mark as Complete", command=mark_complete, style="TButton")
btn_complete.grid(row=0, column=2, padx=5, pady=5)

# Task List Display
task_list = ttk.Treeview(root, columns=("Title", "Assignee", "Deadline", "Status"), show='headings', height=10)
task_list.heading("Title", text="Task Title")
task_list.heading("Assignee", text="Assignee")
task_list.heading("Deadline", text="Deadline")
task_list.heading("Status", text="Status")

task_list.column("Title", anchor=tk.CENTER, width=150)
task_list.column("Assignee", anchor=tk.CENTER, width=100)
task_list.column("Deadline", anchor=tk.CENTER, width=100)
task_list.column("Status", anchor=tk.CENTER, width=100)
task_list.pack(pady=20)

root.mainloop()
