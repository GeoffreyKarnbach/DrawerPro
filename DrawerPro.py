from tkinter import*
import time
import threading
from tkinter.filedialog import *
from PIL import ImageGrab,ImageTk, Image
import os
from tkinter import ttk
couleur="black"
dedans="red"
truc=[]
x22,y22=0,0
z22=0
taille=475
fullscreen=False
x,y=100,100  
def nouveau():
    global fullscreen   
    fen=Tk()
    fen.title("DrawerPro 3.0")
    fen.attributes("-fullscreen",fullscreen)
    fen.wm_iconbitmap("0_Crayon.ico")
    fen.configure(bg="grey43")
    photo=[]
    move=0
    filepath=""
    photo1=PhotoImage(file="LoadingScreen.png")
    ######################################
    def debut():
        def titlePourcents():
            try:
                fen.title(str(int(pb["value"]))+" % loaded")
                fen.after(50,titlePourcents)
            except:
                pass
        b = Label(fen,image=photo1)
        b.grid(padx=5,pady=5)
        pb = ttk.Progressbar(fen, orient="horizontal",length = 400, mode="determinate")
        pb.grid(padx=5,pady=5)
        pb.start()
        fen.after(50,titlePourcents)
        fen.after(5900,pb.destroy)
        fen.after(5900,b.destroy)
    def partie():
        def move(event):
            move=can.find_closest(event.x, event.y)[0]
            if "image" in can.gettags(move):
                can.coords(move,event.x-50,event.y-50)
        
        def fullscreen(event):
            global taille
            global fullscreen
            if fullscreen:
                fullscreen=False
            else:
                fullscreen=True
            fen.attributes("-fullscreen",fullscreen)
            
        def MyTimer(tempo = 1.0):
            threading.Timer(tempo, MyTimer, [tempo]).start()
            date1 = time.strftime('%H:%M:%S',time.localtime())
            try:
                date.configure(text=date1)
            except:
                pass
        ############################################
        def effecer(event):
            global x22,y22,z22
            x22,y22,z22=0,0,0
        def size(event):
            global taille
            taille+=10
            can.config(height=taille, width=taille)
        def resize(event):
            global taille
            taille-=10
            can.config(height=taille, width=taille)
        def creer(event):
            global x22,y22,z22
            if not x22 and not y22:
                x22,y22=event.x,event.y
                z22=can.create_rectangle(x22,y22,x22,y22,fill=dedans,outline=couleur)
                truc.append(z22)
                return z22
            else:
                can.coords(z22,x22,y22,event.x,event.y)
        def Dedans(x):
            global dedans
            dedans=x
        def effaceDernier(event):
            try:
                can.delete(truc[-1])
                del truc[-1]
            except:
                pass
        def save():
            newpath=asksaveasfilename(title="Sauvegarder")
            n=newpath   
            n=n.split("/")
            n=n[-1]
            try:
                os.makedirs(newpath)
            except:
                pass
            a=newpath+"/"+n+".png"
            b=newpath+"/"+n+".jpg"
            c=newpath+"/"+n+".ps"
            x=can.winfo_rootx()+can.winfo_x()
            y=can.winfo_rooty()+can.winfo_y()
            x1=x+can.winfo_width()
            y1=y+can.winfo_height()
            box=(x-85,y-10,x1-80,y1-25)
            #box=(x-75,y-10,x1-80,y1-10)
            img=ImageGrab.grab(box)
            img.save(a)
            img.save(b)
            can.update()
            can.postscript(file=c, colormode='color')
            
        def change(x):
            global couleur
            couleur=x
        def effacer():
            can.delete("all")
        def cercle():
            global x,y
            x=can.create_oval(x-125,y-125,x+125,y+125,outline=couleur,fill=dedans,width=3)
            truc.append(x)
        def triangle():
            global x,y
            x=can.create_polygon(x,y-125,x-125,y+125,x+125,y+125,outline=couleur,fill=dedans,width=3)
            truc.append(x)
        def endroit(event):
            global x,y
            x=event.x
            y=event.y
        def imagePNG():
            global x,y
            photo.append(PhotoImage(file=askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')]))) 
            x=can.create_image(x,y, anchor=NW, image=photo[-1], tag="image")
            truc.append(x)
        def imageJPG():
            global x,y
            photo.append(Image.open(askopenfilename(title="Ouvrir une image",filetypes=[('JPG files','.jpg'),('all files','.*')])))
            can.image=ImageTk.PhotoImage(photo[-1])
            x=can.create_image(x,y, anchor=CENTER, image=can.image,tag="image")
            truc.append(x)
        def dessin(event):
            global couleur
            x1,y1=(event.x-1),(event.y-1)
            x2,y2=(event.x+1),(event.y+1)
            can.create_oval(x1,y1,x2,y2,outline=couleur,width=5)

        def rect():
            can.bind("<B1-Motion>",creer)
            can.bind("<ButtonRelease-1>",effecer)
        def TraitLibre():
            can.bind("<B1-Motion>",dessin)
        def deplacerForme():
            can.bind("<B1-Motion>",move)
        def click():
            can.bind("<Button-1>",endroit)
        ###########################################
        fen.title("DrawerPro 3.0")
        menu=Menu(fen)
        menu1 = Menu(menu, tearoff=0)
        menu1.add_command(label="Sauvegarder",command=save)
        menu1.add_command(label="Tout effacer",command=effacer)
        menu1.add_command(label="Parametre")
        menu1.add_command(label="Quitter", command=fen.destroy) 
        menu.add_cascade(label="Fichier", menu=menu1)
        
        menu2 = Menu(menu, tearoff=0)
        menu2.add_command(label="Inserer PNG",command=imagePNG)
        menu2.add_command(label="Inserer JPG",command=imageJPG)
        menu.add_cascade(label="Image", menu=menu2)

        menu3 = Menu(menu, tearoff=0)
        menu3.add_command(label="Trait libre",command=TraitLibre)
        menu3.add_command(label="Rectangle",command=rect)
        menu3.add_command(label="Cercle",command=cercle)
        menu3.add_command(label="Triangle",command=triangle)
        menu.add_cascade(label="Dessin", menu=menu3)

        menu4 = Menu(menu, tearoff=0)
        menu4.add_command(label="Deplacer",command=deplacerForme)
        menu4.add_command(label="Click",command=click)
        menu4.add_separator()
        menu4.add_command(label="Zoom +",command= lambda x=None: size(x))
        menu4.add_command(label="Zoom -",command= lambda x=None: resize(x))
        menu.add_cascade(label="Autre", menu=menu4)

        fen.config(menu=menu)
        ##########################################
        frame1=Frame(fen, relief=GROOVE,bg="white")
        frame1.grid(column=0,row=0,pady=5,padx=10)

        blanc=Button(frame1,bg="white",width=2,height=1,command = lambda: change("white"))
        blanc.grid(column=0,row=0,pady=2,padx=2)
        noir=Button(frame1,bg="black",width=2,height=1,command = lambda: change("black"))
        noir.grid(column=0,row=1,pady=2,padx=2)
        #
        gris=Button(frame1,bg="grey",width=2,height=1,command = lambda: change("grey"))
        gris.grid(column=0,row=2,pady=2,padx=2)
        golden=Button(frame1,bg="gold",width=2,height=1,command = lambda: change("gold"))
        golden.grid(column=0,row=3,pady=2,padx=2)
        #
        vertF=Button(frame1,bg="darkgreen",width=2,height=1,command = lambda: change("darkgreen"))
        vertF.grid(column=0,row=4,pady=2,padx=2)
        vertC=Button(frame1,bg="lawngreen",width=2,height=1,command = lambda: change("lawngreen"))
        vertC.grid(column=0,row=5,pady=2,padx=2)
        #
        turquoise=Button(frame1,bg="turquoise",width=2,height=1,command = lambda: change("turquoise"))
        turquoise.grid(column=0,row=6,pady=2,padx=2)
        bleuC=Button(frame1,bg="Steelblue1",width=2,height=1,command = lambda: change("Steelblue1"))
        bleuC.grid(column=0,row=7,pady=2,padx=2)
        #
        bleuF=Button(frame1,bg="blue",width=2,height=1,command = lambda: change("blue"))
        bleuF.grid(column=0,row=8,pady=2,padx=2)
        violet=Button(frame1,bg="purple1",width=2,height=1,command = lambda: change("purple1"))
        violet.grid(column=0,row=9,pady=2,padx=2)
        #
        rougeF=Button(frame1,bg="red4",width=2,height=1,command = lambda: change("red4"))
        rougeF.grid(column=0,row=10,pady=2,padx=2)
        rougeC=Button(frame1,bg="red",width=2,height=1,command = lambda: change("red"))
        rougeC.grid(column=0,row=11,pady=2,padx=2)
        #
        orange=Button(frame1,bg="orange",width=2,height=1,command = lambda: change("orange"))
        orange.grid(column=0,row=12,pady=2,padx=2)
        jaune=Button(frame1,bg="yellow",width=2,height=1,command = lambda: change("yellow"))
        jaune.grid(column=0,row=13,pady=2,padx=2)
        #
        rose=Button(frame1,bg="deeppink",width=2,height=1,command = lambda: change("deeppink"))
        rose.grid(column=0,row=14,pady=2,padx=2)
        rose2=Button(frame1,bg="hotpink",width=2,height=1,command = lambda: change("hotpink"))
        rose2.grid(column=0,row=15,pady=2,padx=2)
        ######################################
        blanc=Button(frame1,bg="white",width=2,height=1,command = lambda: Dedans("white"))
        blanc.grid(column=1,row=0,pady=2,padx=2)
        noir=Button(frame1,bg="black",width=2,height=1,command = lambda: Dedans("black"))
        noir.grid(column=1,row=1,pady=2,padx=2)
        #
        gris=Button(frame1,bg="grey",width=2,height=1,command = lambda: Dedans("grey"))
        gris.grid(column=1,row=2,pady=2,padx=2)
        golden=Button(frame1,bg="gold",width=2,height=1,command = lambda: Dedans("gold"))
        golden.grid(column=1,row=3,pady=2,padx=2)
        #
        vertF=Button(frame1,bg="darkgreen",width=2,height=1,command = lambda: Dedans("darkgreen"))
        vertF.grid(column=1,row=4,pady=2,padx=2)
        vertC=Button(frame1,bg="lawngreen",width=2,height=1,command = lambda: Dedans("lawngreen"))
        vertC.grid(column=1,row=5,pady=2,padx=2)
        #
        turquoise=Button(frame1,bg="turquoise",width=2,height=1,command = lambda: Dedans("turquoise"))
        turquoise.grid(column=1,row=6,pady=2,padx=2)
        bleuC=Button(frame1,bg="Steelblue1",width=2,height=1,command = lambda: Dedans("Steelblue1"))
        bleuC.grid(column=1,row=7,pady=2,padx=2)
        #
        bleuF=Button(frame1,bg="blue",width=2,height=1,command = lambda: Dedans("blue"))
        bleuF.grid(column=1,row=8,pady=2,padx=2)
        violet=Button(frame1,bg="purple1",width=2,height=1,command = lambda: Dedans("purple1"))
        violet.grid(column=1,row=9,pady=2,padx=2)
        #
        rougeF=Button(frame1,bg="red4",width=2,height=1,command = lambda: Dedans("red4"))
        rougeF.grid(column=1,row=10,pady=2,padx=2)
        rougeC=Button(frame1,bg="red",width=2,height=1,command = lambda: Dedans("red"))
        rougeC.grid(column=1,row=11,pady=2,padx=2)
        #
        orange=Button(frame1,bg="orange",width=2,height=1,command = lambda: Dedans("orange"))
        orange.grid(column=1,row=12,pady=2,padx=2)
        jaune=Button(frame1,bg="yellow",width=2,height=1,command = lambda: Dedans("yellow"))
        jaune.grid(column=1,row=13,pady=2,padx=2)
        #
        rose=Button(frame1,bg="deeppink",width=2,height=1,command = lambda: Dedans("deeppink"))
        rose.grid(column=1,row=14,pady=2,padx=2)
        rose2=Button(frame1,bg="hotpink",width=2,height=1,command = lambda: Dedans("hotpink"))
        rose2.grid(column=1,row=15,pady=2,padx=2)
        ##############################################
        can=Canvas(fen,bg="white", height=taille, width=taille)
        can.grid(column=1,row=0,rowspan=2,columnspan=3,pady=10,padx=10)
        ############################################
        date=Label(fen,text=time.strftime("%H:%M:%S"))
        date.grid(column=3,row=2,padx=10,pady=10)
        MyTimer(1.0)
        ##############################################    
        fen.bind("<KeyPress- +>",size)
        fen.bind("<Control-z>",effaceDernier)
        fen.bind("<KeyPress- minus>",resize)
        fen.bind("<Escape>",fullscreen)
        ##############################################
    debut()
    fen.after(5900,partie)
    fen.mainloop()
nouveau()
