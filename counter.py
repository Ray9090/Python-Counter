# Automatic Counter
import tkinter as tk

counter = 0
def counter_function(label): # declaring a function 
    counter = 0
    def count():    # fucnciton for count 
        global counter # global veriable 
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()
    
count = tk.Tk()
count.title("Counting in Seconds")
label = tk.Label(count, fg="dark green", width=50, height=10)   # Label widgets are used to display text or images
label.pack()  # The pack() geometry manager organizes widgets in blocks before placing
counter_function(label)
#   A button that can contain text and can perform an action when clicked
button = tk.Button(count, text='Stop', width=50, height=1, bg='purple', fg='red', command=count.destroy)
button.pack()
count.mainloop()