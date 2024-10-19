import tkinter as tk


def phrase0():
    print('1st GUI Development Trial')


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame,
                   text='QUIT',
                   fg='red',
                   command=quit)
button.pack(side=tk.LEFT)
Phrase1 = tk.Button(frame,
                    text='Hello',
                    command=phrase0)
Phrase1.pack(side=tk.LEFT)
root.mainloop()
