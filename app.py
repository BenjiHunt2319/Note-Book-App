from tkinter import *
from tkinter import messagebox as msg
import datetime
import os

class NoteBook:
	def __init__(self, root):
		self.root = root
		self.root.columnconfigure(0, weight=1)
		self.widgets()
		
	def saveEntry(self):
			date = datetime.datetime.now()
			with open("text.txt", "a") as file:
				if self.entry.get("1.0", "end-1c") != "":
					file.write(f"{date.strftime('%Y-%m-%d %H:%M:%S')}\n")
					file.write(self.entry.get("1.0","end-1c"))
					msg.showinfo("Sucessful", "Entry added sucessfully!.")
				else:
					msg.showerror("Invalid", "Please enter text.")
		
	def viewNotes(self):
		self.viewer = Toplevel(self.root)
		self.viwer.geometry("400x300")
		self.display = Text(self.viwer, width=45, height=20)
		self.display.pack(padx=20, pady=20, fill=BOTH, expand=True)
		
		with open("text.txt", "r") as file:
			content = file.read()
		self.display.insert("1.0", content)
		self.display.config(state=DISABLED)
	
	def widgets(self):
		self.frame = Frame(self.root)
		self.frame.grid(row=0, column=0,padx=10, pady=10)
		
		self.entry = Text(self.frame, width=45, height=15)
		self.entry.grid(row=0, column=0, columnspan=2, pady=(25,0))
		
		self.saveBtn = Button(self.frame, text="Save", padx=150, pady=35, command=self.saveEntry)
		self.saveBtn.grid(row=1, column=0, sticky="nsew")
		
		self.viewBtn = Button(self.frame, text="View", padx=150, pady=35, command=self.viewNotes)
		self.viewBtn.grid(row=1, column=1, sticky="nsew")
		

if __name__ == "__main__":
	root = Tk()
	app = NoteBook(root)
	root.mainloop()