from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
import datetime

class NotePad:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.root.title("Note Pad Pro")
        self.root.resizable(False, False)
        self.current_file = ""
        
        # call all widgets
        self.widgets()
        
    # create the base frame
    def widgets(self):
        self.frame = Frame(self.root, padx=20, pady=20)
        self.frame.grid_columnconfigure(0, weight=1, uniform="equal_cols")
        self.frame.grid_columnconfigure(1, weight=1, uniform="equal_cols")
        self.frame.grid(row=0, column=0)
        
        self.title = Label(self.frame, text="Note Pad PRO", font=("Verdana", 16, "bold"))
        self.title.grid(row=0, column=0, sticky="w")
        
        # entry box for addint new text to a file
        self.textBox = Text(self.frame, width=65, height=20, padx=15, pady=15)
        self.textBox.grid(row=1, column=0, columnspan=2, pady=(0, 15))
        
        # =======================================
        # buttons
        # =======================================
        
        # save the current edit to the current file
        self.saveBtn = Button(self.frame, text="Save", font=("Verdana", 12), width=12, pady=10, command=self.saveFile)
        self.saveBtn.grid(row=2, column=0, sticky="nsew", padx=(0, 5), pady=(0, 5))
        
        # view the current file
        self.viewBtn = Button(self.frame, text="View", font=("Verdana", 12), width=12, pady=10, command=self.viewFile)
        self.viewBtn.grid(row=2, column=1, sticky="nsew", pady=(0, 5))

        # add a new text file
        self.newBtn = Button(self.frame, text="New", font=("Verdana", 12), width=12, pady=10, command=self.newFile)
        self.newBtn.grid(row=3, column=0, sticky="nsew", padx=(0, 5))
        
        # browse files to select a exsisting file        
        self.browseBtn = Button(self.frame, text="Browse", font=("Verdana", 12), width=12, pady=10, command=self.browseFiles)
        self.browseBtn.grid(row=3, column=1, sticky="nsew")
        
    
    # browse for file
    def browseFiles(self):
        self.file_path = filedialog.askopenfilename(
            title="Select a text file",
            filetypes=[("Text Files", "*.txt"),("All Files", "*.*")]
        )
        if self.file_path:
            self.current_file = self.file_path
    
    # save the current file when done editing
    def saveFile(self):
        
        # check if a current file exsist already
        if self.current_file == "":
            msg.showerror("Error", "Please create a new file or select a exsisting file before saving")
            return
        
        # get current date and time
        self.date = datetime.datetime.now()
        self.timestamp = self.date.strftime("%d.%m.%y - %H:%M:%S \n\n")
        
        # append the current text edit to the file
        with open(self.current_file, "a") as file:
            file.write(self.timestamp)
            file.write(self.textBox.get("1.0", END))
        msg.showinfo("Success", "File saved Successfully")
    
    # create a file text file
    def newFile(self):
        self.frame = Toplevel(self.root, pady=20, padx=20)
        self.frame.geometry("300x150")
        self.frame.title("New File")
        
        self.fileName = Label(self.frame, text="File Name", font=("Verdana", 14, "bold"))
        self.fileName.pack()
        
        self.entry = Entry(self.frame, width=30)
        self.entry.pack(pady=10)
        
        self.btn = Button(self.frame, text="Save", font=("Verdanna", 12), pady=5, padx=50, command=self.addFile)
        self.btn.pack()
    
    # function to add the new file to the fodler
    def addFile(self):
        self.current_file = self.entry.get() + ".txt"
        with open(self.current_file, "w") as file:
            file.write("")
        msg.showinfo("Success", "File Created")
        
    
    def viewFile(self):
        self.viewBox = Toplevel(self.root, padx=20, pady=20)
        
        with open(self.current_file, "r") as file:
            self.content = file.read()
            self.viewEntry = Text(self.viewBox)
            self.viewEntry.pack()
            self.viewEntry.insert("1.0", self.content)


# run the app
if __name__ == "__main__":
    root = Tk()
    app = NotePad(root)
    root.mainloop()