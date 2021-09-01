import tkinter

def main():
    #Create a root window
    root = tkinter.Tk()
    #Call the event loop
    root.mainloop()
    #create a button widget
    button = Button(root, text = "Click Me")
    button.pack()

#Call the function main
main()