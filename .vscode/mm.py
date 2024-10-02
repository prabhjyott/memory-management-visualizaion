from flask import Flask, render_template, request, redirect, url_for
from collections import deque

app = Flask(__name__)

class MemoryManager:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.memory = deque(maxlen=num_frames)  # Use a deque for efficient FIFO
        self.page_faults = 0

    def access_page(self, page_number):
        if page_number in self.memory:
            # Page hit: do nothing
            return True
        else:
            # Page fault: need to replace a page
            self.page_faults += 1
            self.memory.append(page_number)  # Add the new page
            return False  # Page fault occurred

@app.route("/", methods=["GET", "POST"])
def index():
    memory_manager = MemoryManager(num_frames=4)  # Define the number of frames
    if request.method == "POST":
        try:
            pages = request.form["pages"].split(",")
            pages = [int(page.strip()) for page in pages]  # Convert to integers
            for page in pages:
                memory_manager.access_page(page)
            return render_template("index.html", memory=list(memory_manager.memory), page_faults=memory_manager.page_faults)
        except ValueError:
            # Handle invalid input
            return "Invalid input. Please enter a comma-separated list of integers."
    return render_template("index.html", memory=[], page_faults=0)

if __name__ == "__main__":
    app.run(debug=True)  # Disable debug mode in production