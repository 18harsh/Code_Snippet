# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:55:20 2020

@author: Harsh
"""

from tkinter import*

def _quit():
        global screen
        screen.quit()     # stops mainloop
        screen.destroy()
#=====================================================/////tkinter window\\\\\\=============================================================
def adjustWindow(window):
    w = 800  # width for the window size
    h = 600  # height for the window size
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    window.resizable(True, True)    # disabling the resize option for the window
    window.configure(background='white')    # making the background white of the window
    
#=================================================================================================================================    
root=Tk()
root.title("Insight of Google App's")
width_value=root.winfo_screenwidth()
height_value=root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(width_value, height_value))
root.configure(background='#102131')
root.iconbitmap(r"C:\\InternshipFinal\\google.ico")

#====================================================/////label, button, frame\\\\\\\==============================================    
Label(root, text='Tic Tac Toe',font=("Lucida",25,'bold'),fg='#ffffff',bg='black',).place(x=20,y=550)
      
big_frame = Frame(root)
big_frame.pack()

X=Button(big_frame,text='Player-1 is X',width=12,anchor=CENTER)
X.grid(row=0, column=0 ,padx=5,pady=5)   
X.config(state='normal/disable')
# --------------canvas----------------
canvas.create_oval(a,b,a+50,b+50,outline="white",fill=colours[m],width=2)

canvas=Canvas(width = 500,height=500,bg='#87ceeb')
canvas.place(x=20,y=20) 

val=Label(mcanvas,width=600,height=8,font=("Lucida",30,'bold'),fg='black',bg='#102131')
mcanvas.create_window(300,250, window=val)

canvas.delete("all")
#--------------------------text------------
displayText = Text(feed, height=10, width=20)
displayText.pack()


#----------------input--------------------
reg_number=StringVar()
regNumEntry=Entry(mainframe,width=20,textvariable=reg_number)
regNumEntry.grid(row=0, column=1 ,padx=5, pady=5)
regNumEntry.bind("<Return>", lambda event: validate(event, "Registration number"))
regNumEntry.bind("<Tab>", lambda event: validate(event, "Registration number"))

#-----------------------combobox-------------------------
birthFrame = Frame(mainframe)
yearBirth = StringVar()
choices = list(range(1950,2020))
Combobox(birthFrame , width=5, values = choices ,textvariable = yearBirth).grid(row=0, column=1, padx=5, pady=5)
monthBirth = StringVar()
choices = list(range(1,13))
Combobox(birthFrame , width=5, values = choices ,textvariable = monthBirth).grid(row=0, column=2, padx=5, pady=5)
dayBirth = StringVar()
choices = list(range(1,32))
Combobox(birthFrame , width=5, values = choices ,textvariable = dayBirth).grid(row=0, column=3, padx=5, pady=5)
birthFrame.grid(row=6, column=1, padx=5, pady=5)

#------------radiobutton-------------------
genderValue = StringVar()
genderFrame = Frame(mainframe)
Radiobutton(genderFrame, text="Male" ,variable=genderValue, value="Male").grid(row=0, column=1, padx=5, pady=5)
Radiobutton(genderFrame, text="Female" ,variable=genderValue,value="Female").grid(row=0, column=2, padx=5, pady=5)
genderFrame.grid(row=9, column=1, padx=5, pady=5)
genderValue.set("Male")
#----------------optionMenu-----------------
Label(screen4, text="Select Sem:", font=("Open Sans", 12, 'bold'), fg='white', bg='#174873').grid(row=rowNo,column=0, pady=(15,0))
list1 = ['1','2','3','4','5','6','7','8']
droplist = OptionMenu(screen4, semester, *list1)
semester.set('--0--')
droplist.config(width=5)
droplist.grid(row=rowNo, column=1, pady=(15,0)) 

#-------------------message box---------------
tk.messagebox.showwarning('Successful','Please click on save')
# -----------------------calendar----------------------
Calendar(mainframe,font="Arial 14", selectmode='day',cursor="hand1", year=2018, month=2, day=5).grid(
    row=7, column=1, padx=5, pady=5)

yearBirth.set("2019")
monthBirth.set("1")
dayBirth.set("1")
# Date picker for start date , end date
startDate = StringVar()
endDate = StringVar()
DateEntry(mainframe , textvariable = startDate , date_pattern='dd/mm/y').grid(row=7, column=1, padx=5, pady=5)
DateEntry(mainframe , textvariable = endDate , date_pattern='dd/mm/y' ).grid(row=8,column=1, padx=5, pady=5)

# -----------------------------tkinter graph-----------------
canvas = FigureCanvasTkAgg(figure1,big_frame)
canvas.draw()
canvas.get_tk_widget().pack( fill=BOTH, expand=True)
toolbar = NavigationToolbar2Tk(canvas,big_frame)
toolbar.update()

#--------------------------image----------------------
photocanvas=Canvas(root,width =1355,height=177,bg='#102131')
photocanvas.place(x=0,y=0) 
myimg=PhotoImage(file="C:\\InternshipFinal\\predictive_analytics_banner.png")
photocanvas.create_image(0,0,anchor=NW,image=myimg)
photocanvas.image =myimg
   



         
         
     
         
