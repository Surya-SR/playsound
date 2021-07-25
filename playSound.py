from tkinter import *
import playsound as ps


def click():

    filanme='C://Users//SURYA R//OneDrive//Desktop//tkinter_sound//pleasant_music.mp3'
    ps.playsound(filanme)

window=Tk()
e=Entry(window,)
window.title("text box")



label=Label(window,text="PLAY MUSIC!",font=('comic sans ms',40,'bold'),
            foreground='black',bg='yellow')
label.pack()

window.config(background='yellow')

sa=PhotoImage(file="img_3.png")
A=Button(window,text="A",command=lambda :click(),image=sa,state=ACTIVE,height=400,width=400,
         activeforeground='black',activebackground='yellow')
A.pack()



window.mainloop()