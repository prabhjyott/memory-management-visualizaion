import tkinter as tk
from tkinter import messagebox

class MemoryManager:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.memory = [None] * num_frames

    def allocate_page(self, page_number):
        for i in range(self.num_frames):
            if self.memory[i] is None:
                self.memory[i] = page_number
                return True
        return False  # Memory full

    def deallocate_page(self, page_number):
        for i in range(self.num_frames):
            if self.memory[i] == page_number:
                self.memory[i] = None
                return True
        return False  # Page not found

class MemoryVisualization(tk.Tk):
    def __init__(self, memory_manager):
        super().__init__()
        self.memory_manager = memory_manager
        self.title("Memory Management Visualization")
        self.geometry("800x400")
        self.configure(bg="#e0e0e0")
        
        # Styling
        self.header_label = tk.Label(self, text="Memory Management Visualization", font=("Arial", 18), bg="#2196F3", fg="white")
        self.header_label.pack(fill=tk.X)

        self.frames = []
        self.setup_memory_frames()

        self.entry = tk.Entry(self, font=("Arial", 14), width=10, borderwidth=2)
        self.entry.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        self.allocate_button = tk.Button(button_frame, text="Allocate", command=self.allocate_page,
                                          bg="#4CAF50", fg="white", font=("Arial", 12), width=10)
        self.allocate_button.grid(row=0, column=0, padx=10)

        self.deallocate_button = tk.Button(button_frame, text="Deallocate", command=self.deallocate_page,
                                            bg="#f44336", fg="white", font=("Arial", 12), width=10)
        self.deallocate_button.grid(row=0, column=1, padx=10)

        self.info_label = tk.Label(self, text="Enter Page Number:", bg="#e0e0e0", font=("Arial", 12))
        self.info_label.pack(pady=5)

    def setup_memory_frames(self):
        memory_frame = tk.Frame(self)
        memory_frame.pack(pady=20)

        for i in range(self.memory_manager.num_frames):
            frame = tk.Frame(memory_frame, width=80, height=80, borderwidth=2, relief="groove", bg="lightgray")
            frame.grid(row=0, column=i, padx=10)
            label = tk.Label(frame, text="", font=("Arial", 14))
            label.pack(expand=True)
            self.frames.append((frame, label))

    def allocate_page(self):
        page_number = self.entry.get()
        if not page_number.strip():
            messagebox.showwarning("Input Error", "Please enter a page number.")
            return

        if self.memory_manager.allocate_page(page_number):
            self.update_memory_display()
        else:
            messagebox.showerror("Error", "Memory full!")

    def deallocate_page(self):
        page_number = self.entry.get()
        if not page_number.strip():
            messagebox.showwarning("Input Error", "Please enter a page number.")
            return

        if self.memory_manager.deallocate_page(page_number):
            self.update_memory_display()
        else:
            messagebox.showerror("Error", "Page not found!")

    def update_memory_display(self):
        for i, (frame, label) in enumerate(self.frames):
            if self.memory_manager.memory[i] is None:
                frame.config(bg="lightgray")
                label.config(text="")
            else:
                frame.config(bg="lightgreen")
                label.config(text=self.memory_manager.memory[i])

if __name__ == "__main__":
    num_frames = 5  # Change as needed
    memory_manager = MemoryManager(num_frames)
    app = MemoryVisualization(memory_manager)
    app.mainloop()
#what
