import tkinter as tk
import time

# Setting up the environment
root = tk.Tk()
root.title("DIGITAL CLOCK")
root.geometry("400x100")
root.resizable(True, True)

# List of background colors to cycle through
bg_colors = ["black", "blue", "purple", "green", "orange", "red", "navy", "pink"]

# Adding a label for the clock
time_label = tk.Label(root, font=('Times New Roman', 50, 'bold'), background='black', foreground='white')
time_label.pack(anchor='center')

# Function to update the time and background color
def update_time():
    current_time = time.strftime('%H:%M:%S %p')
    
    # Update background color
    bg_color = bg_colors[int(time.time()) % len(bg_colors)]
    root.configure(bg=bg_color)
    
    # Update time and background color of label
    time_label.config(text=current_time, background=bg_color)
    
    time_label.after(1000, update_time)

# Initial call to update the time
update_time()

# Run the application
root.mainloop()
