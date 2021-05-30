from tkinter import *



root=Tk()

PAD_WIDTH=150
PAD_HEIGHT=10
PAD_X1=200
PAD_Y1=600



width=400



c=Canvas(width=400,height=700,bg='red')
c.pack()


c.create_oval(100,100,250,250,)

def moving_x1(dir):
    global PAD_X
    if dir== '+':
     if (PAD_X + PAD_WIDTH / 2) < width:
        PAD_X+=3

    else:
        if(PAD_X - PAD_WIDTH / 2)>0:
         PAD_X-=3




    c.delete('all')

    pad=c.create_rectangle(PAD_X-PAD_WIDTH/2,
                                   PAD_Y-PAD_HEIGHT/2,
                                   PAD_X+PAD_WIDTH/2,
                                   PAD_Y+PAD_HEIGHT/2,
                                   fill='black')





root.bind("<Left>",lambda e :moving_x('-'))
root.bind("<Right>",lambda e :moving_x('+'))
root.mainloop()




