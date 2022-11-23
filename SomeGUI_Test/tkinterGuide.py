import tkinter as tk
from tkinter import ttk

def main():
    
    root = tk.Tk()
    root.title('tkinter window demo')
    
    # geometry methods accept a string following the format: "whidthxheight±x±y"
    # whidthxweight is the dimension of the window
    # ±x±y is the offset where the window will be placed starting from top left of the screen
    root.geometry('600x400+50+50')

    root.mainloop()

if __name__ == '__main__':
    main()