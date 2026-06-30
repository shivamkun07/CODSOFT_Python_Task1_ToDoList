
import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x550")
        self.root.configure(bg="#f2f2f2")

        title = tk.Label(
            root,
            text="TO-DO LIST",
            font=("Arial", 22, "bold"),
            bg="#f2f2f2",
            fg="darkblue"
        )
        title.pack(pady=15)

        self.task_entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.task_entry.pack(pady=10)

        button_frame = tk.Frame(root, bg="#f2f2f2")
        button_frame.pack()

        tk.Button(
            button_frame,
            text="Add Task",
            width=12,
            bg="#4CAF50",
            fg="white",
            command=self.add_task
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Delete Task",
            width=12,
            bg="#f44336",
            fg="white",
            command=self.delete_task
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Mark Done",
            width=12,
            bg="#2196F3",
            fg="white",
            command=self.mark_done
        ).grid(row=0, column=2, padx=5)

        self.task_listbox = tk.Listbox(
            root,
            width=50,
            height=18,
            font=("Arial", 13),
            selectbackground="lightblue"
        )
        self.task_listbox.pack(pady=20)

    def add_task(self):
        task = self.task_entry.get().strip()

        if task == "":
            messagebox.showwarning("Warning", "Please enter a task.")
            return

        self.task_listbox.insert(tk.END, "☐ " + task)
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
        except:
            messagebox.showwarning("Warning", "Please select a task.")

    def mark_done(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)

            if task.startswith("☑"):
                return

            task = task.replace("☐", "☑", 1)

            self.task_listbox.delete(index)
            self.task_listbox.insert(index, task)

        except:
            messagebox.showwarning("Warning", "Please select a task.")


root = tk.Tk()
app = TodoApp(root)
root.mainloop()