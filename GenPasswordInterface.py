import tkinter as tk
import genPassword as passGen#gets the password generator file

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.displayPassOutput = tk.Text(self, height=10,width=32)
        self.genPass16 = tk.Button(self, text="Generate Password 16", command=self.givePass16)
        self.genPass32 = tk.Button(self, text="Generate Password 32", command=self.givePass32)
        self.genPass64 = tk.Button(self, text="Generate Password 64", command=self.givePass64)
        self.displayPassOutput.config(state="disabled")
        
        self.displayPassOutput.grid(row=0, column=0, sticky="new")
        self.genPass16.grid(row=1, column=0, sticky="sew")
        self.genPass32.grid(row=2, column=0, sticky="sew")
        self.genPass64.grid(row=3, column=0, sticky="sew")
        
    def givePass32(self):
        generatedPassword = passGen.genPassword(32)
        self.displayPassOutput.config(state="normal")
        self.displayPassOutput.delete(1.0, tk.END)
        self.displayPassOutput.insert(tk.END, generatedPassword)
        self.displayPassOutput.config(state="disabled")
        
    def givePass64(self):
        generatedPassword = passGen.genPassword(64)
        self.displayPassOutput.config(state="normal")
        self.displayPassOutput.delete(1.0, tk.END)
        self.displayPassOutput.insert(tk.END, generatedPassword)
        self.displayPassOutput.config(state="disabled")
        
    def givePass16(self):
        generatedPassword = passGen.genPassword(16)
        self.displayPassOutput.config(state="normal")
        self.displayPassOutput.delete(1.0, tk.END)
        self.displayPassOutput.insert(tk.END, generatedPassword)
        self.displayPassOutput.config(state="disabled")
               

root = tk.Tk()
root.title("Password Generator")
root.rowconfigure(0, minsize=1000, weight=1)
root.columnconfigure(0, minsize=800, weight=1)
root.configure(background = 'RoyalBlue1')
app = Application(master=root)
app.mainloop()
