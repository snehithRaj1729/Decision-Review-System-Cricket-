import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import imutils
import time

stream = cv2.VideoCapture('cricket.mp4')
flag = True
def play(speed):
    global flag
    #print(f"clicked on play . Speed is {speed}")
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed,frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame,width = SET_WIDTH,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame,anchor = tkinter.NW)
    if flag:
        canvas.create_text(120,25,fill = "Black",font = "Times 20 italic bold",text = "Decision Pending")
    flag = not flag




def out():
    thread = threading.Thread(target = pending , args = ("Out",))
    thread.daemon = 1
    thread.start()
    print("player is out")


def pending(decision):
    # Display decision pending image
    frame = cv2.cvtColor(cv2.imread("decisionpending.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame)) #converted frame to photo image object
    canvas.image = frame
    canvas.create_image(0,0,image = frame,anchor = tkinter.NW)
    #Wainting for a second
    time.sleep(1)
    if decision=="Out":
        decisionimage = "out.png"
    else:
        decisionimage = "notout.png"
    frame = cv2.cvtColor(cv2.imread(decisionimage), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))  # converted frame to photo image object
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)






def notout():
    thread = threading.Thread(target=pending, args=("Not out",))
    thread.daemon = 1
    thread.start()
    print("player is Not out")




SET_WIDTH = 1200
SET_HEIGHT = 500

window = tkinter.Tk()
window.title("snehith DRS")
canvas = tkinter.Canvas(window, width = SET_WIDTH, height = SET_HEIGHT)
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"),cv2.COLOR_BGR2RGB)
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img)) #reading an image
image_on_canvas = canvas.create_image(0,0,ancho = tkinter.NW,image = photo)
canvas.pack()

#Buttons

btn = tkinter.Button(window,text = "<< Previous(fast)",width = 50,bg = "Black",fg = "White",command = partial(play,-25))
btn.pack()

btn = tkinter.Button(window,text = "<< Previous(slow)",width = 50,bg = "Black",fg = "White",command = partial(play,-2))
btn.pack()

btn = tkinter.Button(window,text = " Next(slow)>>",width = 50,bg = "Black",fg = "White",command = partial(play,2))
btn.pack()

btn = tkinter.Button(window,text = " Next(fast)>>",width = 50,bg = "Black",fg = "White",command = partial(play,25))
btn.pack()

btn = tkinter.Button(window,text = " Give Out",width = 50,bg = "Black",fg = "White",command = out)
btn.pack()

btn = tkinter.Button(window,text = " Give NotOut",width = 50,bg = "Black",fg = "White",command = notout)
btn.pack()




window.mainloop()

