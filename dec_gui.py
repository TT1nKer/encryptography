import sys
import os
import tkinter as tk

def open_output_file():
    path = output_entry.get()
    if path and os.path.isfile(path):
        folder = os.path.dirname(path)
        if sys.platform == 'win32':
            os.startfile(folder)
        elif sys.platform == 'darwin':
            os.system(f'open "{folder}"')
        else:
            os.system(f'xdg-open "{folder}"')

# ... in GUI setup ...
output_label = tk.Label(frame, text='Output file:')
output_label.grid(row=3, column=0, sticky='e')
output_entry = tk.Entry(frame, width=50)
output_entry.grid(row=3, column=1, padx=5)
output_browse = tk.Button(frame, text='Browse...', command=lambda: browse_save_file(output_entry))
output_browse.grid(row=3, column=2)
output_open = tk.Button(frame, text='Open', command=open_output_file)
output_open.grid(row=3, column=3, padx=5) 