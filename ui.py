import tkinter as tk
from tkinter import ttk, scrolledtext

class EmailApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Email Application")
        master.geometry("600x400")

        # Create main frame
        main_frame = ttk.Frame(master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        # Email list
        self.email_list = tk.Listbox(main_frame, width=30)
        self.email_list.grid(row=0, column=0, rowspan=4, sticky=(tk.N, tk.S, tk.W))
        self.email_list.insert(tk.END, "Email 1")
        self.email_list.insert(tk.END, "Email 2")
        self.email_list.insert(tk.END, "Email 3")

        # Email content
        self.content = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=40, height=10)
        self.content.grid(row=0, column=1, rowspan=3, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Buttons
        ttk.Button(main_frame, text="New Email", command=self.new_email).grid(row=3, column=1, sticky=tk.W)
        ttk.Button(main_frame, text="Reply", command=self.reply).grid(row=3, column=1)
        ttk.Button(main_frame, text="Delete", command=self.delete).grid(row=3, column=1, sticky=tk.E)

        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)

    def new_email(self):
        print("New Email")

    def reply(self):
        print("Reply")

    def delete(self):
        print("Delete")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailApp(root)
    root.mainloop()