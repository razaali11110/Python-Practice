from tkinter import *
from PIL import Image, ImageTk

# root = Tk()
# # label is anything to be written or widget
# mylabel = Label(root, text="Hello Aaqib \nHow are you doing")
# # now placing the label on the window
#
# # pack function is going to place the label where it gets place by itself
# mylabel.pack()
#
# # to hold the screen we use the mainloop fucntion
# root.mainloop()

# root = Tk()
# # this is the upper frame
# topframe = Frame(root)
#
# topframe.pack()
#
# # for the lower frame we will create one and pass the parameter in pack function
# bottomframe = Frame(root)
# bottomframe.pack(side=BOTTOM)
#
# # for creating buttons for each frame
# # fg means foreground, which is not compulsory
# button1 = Button(topframe, text="Button1", fg="Blue")
# button2 = Button(topframe, text="Button2", fg="red")
# button3 = Button(bottomframe, text="Button3", fg="green")
# button4 = Button(bottomframe, text="Button4", fg="brown")
#
# # by default they are made on the top of other
#
# button1.pack(side=LEFT)
# button2.pack(side=RIGHT)
# button3.pack(side=LEFT)
# button4.pack(side=RIGHT)
#
# root.mainloop()

# for the widgets

# root = Tk()

# bg means background and fg means foreground which means color of font
# we will use fill paramter to make the labels grow inside the main window
# fill = X means left and right and fill = Y means up and down

# first label

# label1 = Label(root, text="One", bg="Pink", fg="Blue")
# label1.pack(side=TOP, fill=X)
#
# label2 = Label(root, text="Two", bg="Black", fg="white")
# label2.pack(side=LEFT, fill=Y)
#
# label3 = Label(root, text="Three", bg="White", fg="Blue")
# label3.pack(side=RIGHT, fill=X)
#
# root.mainloop()

# root = Tk()

# trying our the grid method with the input fields or entry fields
# label1 = Label(root, text="Name:")
# label2 = Label(root, text="Password:")

# for creating entry field
# entry1 = Entry(root)
# entry2 = Entry(root)

# now we will use the grid function to place these entries and labels by using rows and columns
# if i were to align the label we use sticky parameters with north, south, east, west
# label1.grid(row=0, sticky=E)  # E means east
# label2.grid(row=1, sticky=E)

# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)

# for creating a check box
# checkbox = Checkbutton(root, text="Keep me logged in :)")
# checkbox.grid(columnspan=2)   # columnspan parameter is used to adjust.
# root.mainloop()

# binding function to a GUI program

# root = Tk()


# def printname():
#     print("Have a good day :)")


# to call a function by pressing the GUI button we will use command parameter inside button function
# make sure to not to use the parenthesis

# button1 = Button(root, text="Click Me!", command=printname)

# button1.pack()

# root.mainloop()

# by using bind function and events

# def printname(event):
#     print("Have a nice day!!")
#
#
# button = Button(root, text="Click me!!")
#
# button.bind("<Button-1>", printname)
# button.pack()
# root.mainloop()

# mouse click events

# root = Tk()


# def leftclick(event):
#     """ Action on left mouse click """
#     print("Left button clicked.")
#
#
# def middleclick(event):
#     """ Action on middle mouse click """
#     print("Scroll button clicked.")
#
#
# def rightclick(event):
#     """ Action on right mouse click """
#     print("Right button clicked.")


# creating a frame, which is gonna be invisible
# mylabel = Label(root, text="Please use any mouse button.")
# mylabel.pack()
# myframe = Frame(root, width=300, height=250)
# myframe.bind("<Button-1>", leftclick)
# myframe.bind("<Button-2>", middleclick)
# myframe.bind("<Button-3>", rightclick)

# for placing the frame into the root window

# myframe.pack()
# root.mainloop()

# root = Tk()

# myframe = Frame(root, width=700, height=300)
# myframe.pack()
# label1 = Label(root, text="Enter your petition")
# label1.grid(row=0, column=0)
# entry1 = Entry(root)
# entry1.grid(row=0, column=1)
# label2 = Label(root, text="Enter your question")
# label2.grid(row=1, column=0)
# entry2 = Entry(root)
# entry2.grid(row=1, column=1)
#
# root.mainloop()

# root = Tk()
#
#
# entry1 = Entry(root, bg="Black", fg="White", borderwidth=5, width=50)
# entry1.pack()
# entry1.insert(0, "Enter your name: ")
# # to use the things typed in the entry label we can use get function
# def greet():
#     mylabel = Label(root, text="Hello " + entry1.get())
#     mylabel.pack()
#
#
# mybutton = Button(root, text="Click me!!", padx=50, pady=50, command=greet, bg="Black", fg="White")
#
#
# mybutton.pack()
# root.mainloop()

# to add any icon on the top of the GUI application we used the image and function of root.iconbitmap("path")

# to exit any program we use the root.quit on any button command

# for working with images we use pillow module in python

# root = Tk()
#
# my_image = ImageTk.PhotoImage(Image.open('/home/aaqib/Downloads/aaqib.jpg'))
# mylabel = Label(image=my_image)
# mylabel.pack()
#
# root.mainloop()