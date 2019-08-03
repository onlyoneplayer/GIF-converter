from tkinter import filedialog
import tkinter as tk
import imageio
import os

root = tk.Tk()
root.title("GIF convertor")

#Functions
def choosing_file():
    global label_1
    global save_path

    save_path =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp4 files","*.mp4"),("all files","*.*")))

    label_1 = tk.Label(root, text=save_path, width=45)
    label_1.grid(row=0, column=0, padx= 3, pady=3)

def choosing_dir():
    global label_2
    global dir_path

    dir_path = filedialog.askdirectory()

    label_2 = tk.Label(root, text=dir_path, width=45)
    label_2.grid(row=1, column=0, padx= 3, pady=3)

def gif_converter(file_path):

    outputPath = os.path.splitext(file_path)[0] + ".gif"

    reader = imageio.get_reader(file_path)
    fps = reader.get_meta_data()['fps']
    
    writer = imageio.get_writer(outputPath, fps=fps)

    for frame in reader:
        writer.append_data(frame)
    
    writer.close()

    label_2 = tk.Label(root, text="Converting done!", width=45)
    label_2.grid(row=1, column=0, padx= 3, pady=3)


#Buttons and Labels
button_1 = tk.Button(root, text="Choose file", command=choosing_file, width=15)
button_2 = tk.Button(root, text="Covert",width=15,command=lambda: gif_converter(save_path))
label_1 = tk.Label(root, text="Choose file to convert", width=45)
label_2 = tk.Label(root, text="", width=45)

#Showing buttons and labels
label_1.grid(row=0, column=0, padx= 3, pady=3)
label_2.grid(row=1, column=0, padx= 3, pady=3)
button_1.grid(row=0, column=1)
button_2.grid(row=1, column=1)


root.mainloop()