import tkinter

class MyGUI:
    def __init__(self, root):
        self.root = root
        self.close = tkinter.Button(root, text="close", command=root.quit).pack()

root = tkinter.Tk()
closebt = MyGUI(root)
root.mainloop()