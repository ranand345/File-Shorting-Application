from tkinter import *
import os
from shutil import move
from tkinter import messagebox as mb

root=Tk()
root.geometry("700x350")
root.title("File Sorting Application")

def show():
    s=un2.get()
    src = s
    imgdest = un4.get()
    docsdest = un5.get()
    ssdest = un6.get()
    excdest = un7.get()
    imgext = ["jpg"] # Add more extensions as per your needs
    ssext = ["png"]
    docsext = ["csv"]
    excext = ["xlsx"] 
    filteredList = []
    dirList = os.listdir(src)

    for z in dirList:
        for i in list(z):
            if i == ".":
                filteredList.append(z)

    print("Entering Sorting Stage")


    for x in filteredList:
        _, ext = x.split('.')
        for y in docsext:
            if ext == y:
                temp1 = os.path.join(src, x)
                move(temp1, docsdest)

    for x in filteredList:
        _, ext = x.split('.')
        for y in imgext:
            if ext == y:
                temp1 = os.path.join(src, x)
                move(temp1, imgdest)
    for x in filteredList:
        _, ext = x.split('.')
        for y in ssext:
            if ext == y:
                temp1 = os.path.join(src, x)
                move(temp1, ssdest)
    for x in filteredList:
        _, ext = x.split('.')
        for y in excext:
            if ext == y:
                temp1 = os.path.join(src, x)
                move(temp1, excdest)
    mb.showinfo('Ok', 'Files Sorted')
    

    #def close_window():
        #mb.showinfo('No', 'Quit has been cancelled')
        #root.destroy()

    #b10=Button(text="Files Sorted, OK",command=close_window)
    #b10.grid()
    #print("Files Sorted")
    root.destroy()


un1= Label(root,text="Enter source folder path",font=("Arial",15),fg="black")
un1.grid(column=1, row=0,pady=10,sticky=W)
x=StringVar()
un2=Entry(root,width="15",font=("Arial",15),textvariable=x) #here textvariable is used to declare input as string value
un2.grid(column=2, row=0,pady=10)
un3= Label(root,text="Type destination folder path here:",font=("Arial",15),fg="black")
un3.grid(column=1, row=1,pady=10)

un4=Entry(root,width="15",font=("Arial",15))
un4.grid(column=2, row=2,pady=10)
un5=Entry(root,width="15",font=("Arial",15))
un5.grid(column=2, row=3,pady=10)
un6=Entry(root,width="15",font=("Arial",15))
un6.grid(column=2, row=4,pady=10)
un7=Entry(root,width="15",font=("Arial",15))
un7.grid(column=2, row=5,pady=10)
l1=Label(root,text="for Image or .jpg files")
l1.grid(column=3, row=2,sticky=W,padx=5)
l1=Label(root,text="for Data or .csv files")
l1.grid(column=3, row=3,sticky=W,padx=5)
l1=Label(root,text="for Screenshot or .png files")
l1.grid(column=3, row=4,sticky=W,padx=5)
l1=Label(root,text="for Excel .xlsx or xls files")
l1.grid(column=3, row=5,sticky=W,padx=5)
b1=Button(text="Sort files",command=show)
b1.grid(column=10, row=16)
un2.focus()
root.mainloop()
