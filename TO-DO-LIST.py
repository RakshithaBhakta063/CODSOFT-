import tkinter as tk
from tkinter import messagebox

def add_task(entry_task, listbox_tasks):
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task(listbox_tasks):
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    # Create the main window
    window = tk.Tk()
    window.title("To-Do List")

    # Task Entry
    entry_task = tk.Entry(window, width=40)
    entry_task.grid(row=0, column=0, padx=10, pady=10)

    # Add Task Button
    btn_add = tk.Button(window, text="Add Task", width=15, command=lambda: add_task(entry_task, listbox_tasks))
    btn_add.grid(row=0, column=1, padx=10, pady=10)

    # Task List
    listbox_tasks = tk.Listbox(window, selectmode=tk.SINGLE, width=50)
    listbox_tasks.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Delete Task Button
    btn_delete = tk.Button(window, text="Delete Task", width=15, command=lambda: delete_task(listbox_tasks))
    btn_delete.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    main()
