from tkinter import *



root=Tk()

PAD_WIDTH=150
PAD_HEIGHT=10
PAD_X1=200
PAD_Y1=600

PAD_X2=200
PAD_Y2=100


width=400



c=Canvas(width=400,height=700,bg='red')
c.pack()


c.create_oval(100,100,250,250,)

def moving_x(dir):
    global PAD_X1
    if dir== '+':
     if (PAD_X1 + PAD_WIDTH / 2) < width:
        PAD_X1+=3

    else:
        if(PAD_X1 - PAD_WIDTH / 2)>0:
         PAD_X1-=3
    drawing()






    pad=c.create_rectangle(PAD_X1-PAD_WIDTH/2,
                                   PAD_Y1-PAD_HEIGHT/2,
                                   PAD_X1+PAD_WIDTH/2,
                                   PAD_Y1+PAD_HEIGHT/2,
                                   fill='black')


def moving_x2(dir):
    global PAD_X2
    if dir== '+':
     if (PAD_X2 + PAD_WIDTH / 2) < width:
        PAD_X2+=3

    else:
        if(PAD_X2 - PAD_WIDTH / 2)>0:
         PAD_X2-=3
    drawing()


def drawing():
 c.delete('all')
 pad = c.create_rectangle(PAD_X1 - PAD_WIDTH / 2,
                          PAD_Y1 - PAD_HEIGHT / 2,
                          PAD_X1 + PAD_WIDTH / 2,
                          PAD_Y1 + PAD_HEIGHT / 2,
                          fill='black')

 pad2=c.create_rectangle(PAD_X2-PAD_WIDTH/2,
                                   PAD_Y2-PAD_HEIGHT/2,
                                   PAD_X2+PAD_WIDTH/2,
                                   PAD_Y2+PAD_HEIGHT/2,
                                   fill='black')

root.bind("<Left>",lambda e :moving_x('-'))
root.bind("<Right>",lambda e :moving_x('+'))
root.bind("<A>",lambda e :moving_x2('-'))
root.bind("<D>",lambda e :moving_x2('+'))
root.mainloop()




