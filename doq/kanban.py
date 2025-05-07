import tkinter as tk
from tkinter import messagebox

class KanbanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kanban To Do App")
        self.root.geometry("900x500")
        self.root.config(bg="#2b2d42")  # dark background for contrast

        # create frames
        self.todo_frame = self.create_frame("To Do", 0, "#ef233c")
        self.doing_frame = self.create_frame("Doing", 0, "#ffd166")
        self.done_frame = self.create_frame("Done", 0, "#06d6a0")

        # input field
        self.entry = tk.Entry(self.root, width=40, font=("Arial", 14), bg="#8d99ae", fg="#edf2f4")
        self.entry.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        # add_button
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#3a86ff", fg="white", font=("Arial", 12, "bold"), activebackground = "#00509e")
        self.add_button.grid(row=1, column=2, pady=10, padx=10)

        # frame, label, listbox
    def create_frame(self, title, col, bg_color):
        frame = tk.Frame(self.root, bg = bg_color, bd=2, relief= tk.RIDGE)
        frame.grid(row=0, column = col, padx=10, pady=10, sticky="nsew")

        # label
        label = tk.Label(frame, text=title, font=("Arial", 16, "bold"), bg=bg_color, fg="white")
        label.pack(side= tk.TOP, fill= tk.X, pady=5)

        # listbox for tasks
        listbox = tk.Listbox(frame, height=15, width=25, font=("Arial", 12), bg="#edf2f4", fg="#2b2d42")
        listbox.pack(pady=5, padx=5, fill= tk.BOTH, expand= True)
        frame.listbox = listbox

        # buttons for moving tasks
        if col == 0: # To Do column
            move_button = tk.Button(frame, text="Move to Doing", bg="#06d6a0", command=lambda: self.move_task(self.doing_frame, self.done_frame))
        else: # Done column
            move_button = tk.Button(frame, text="Delete Task", bg="#ef233c", command=lambda: self.delete_task(self.done_frame))
        
        move_button.pack(side=tk.BOTTOM, pady=10)

        return frame

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.todo_frame.listbox.insert(tk.END, task)
            # self.entry.deleted(first=0, tk.END)     # SyntaxError: positional argument follows keyword argument
        else:
            messagebox.showerror(title="Error", message= "Task cannot be empty!")

    def delete_task(self, frame):
        selected = frame.listbox.curselection()
        if selected:
            task = frame.listbox.get(selected)
            frame.listbox.delete(selected)
            messagebox.showinfo(title="Task Deleted", message= f"Task '{task}' has been deleted!")
        else:
            messagebox.showerror(title="Error", message="No task selected to delete!")

# # initialize the app
if __name__ == "__main__":
    root = tk.Tk()
    # root.grid_columnconfigure(index=0, 1, 2), weight=1   # make columns resize evenly   # SyntaxError: Positional argument cannot appear after keyword arguments
    # root.grid_rowconfigure(index=0, weight=1)   # make row resize
app = KanbanApp(root)
root.mainloop()