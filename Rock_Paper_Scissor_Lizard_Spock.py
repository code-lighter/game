#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Import the required libraries :
from tkinter import *
import random
import simpleaudio as sa

root = Tk()
root.configure(bg="#fff")
root.geometry('+0+0')
root.iconbitmap("Game.ico")
root.title("Rock-Paper-Scissor-Lizard-Spock")
root.resizable(width=False,height=False)

#To play sound files : 
start = sa.WaveObject.from_wave_file("Start.wav")
Win = sa.WaveObject.from_wave_file("Win.wav")
Lose = sa.WaveObject.from_wave_file("Lose.wav")
Draw = sa.WaveObject.from_wave_file("Draw.wav")

start.play()

#Hand images :
rockHandPhoto = PhotoImage(file="Rock_1.png")
paperHandPhoto = PhotoImage(file="Paper_1.png")
scissorHandPhoto = PhotoImage(file="Scissor_1.png")
lizardHandPhoto = PhotoImage(file="Lizard_1.png")
spockHandPhoto = PhotoImage(file="Spock_1.png")

#Graphical images :
rockPhoto = PhotoImage(file="Rock_1.png")
paperPhoto = PhotoImage(file="Paper_1.png")
scissorPhoto = PhotoImage(file="Scissor_1.png")
lizardPhoto = PhotoImage(file="Lizard_1.png")
spockPhoto = PhotoImage(file="Spock_1.png")

#Decision image :
decisionPhoto = PhotoImage(file="Decision_Final.png")

#Result images :
winPhoto = PhotoImage(file="G_WIN.png")
losePhoto = PhotoImage(file="G_LOST.png")
tiePhoto = PhotoImage(file="G_DRAW.png")
tagain = PhotoImage(file="T_AGAIN.png")



#Initialize the button variables :
rHandButton = " "
pHandButton = " "
sHandButton = " "
lHandButton= " "
spockHandButton = " "

#Create the result button :
resultButton = Button(root,image=decisionPhoto)


#Set the variable to True
click = True

def play():
    global rHandButton,pHandButton,sHandButton,lHandButton,spockHandButton
     
    #Set images and commands for buttons :
    rHandButton = Button(root,image = rockHandPhoto, command=lambda:youPick("Rock"))
    pHandButton = Button(root,image = paperHandPhoto, command=lambda:youPick("Paper"))
    sHandButton = Button(root,image = scissorHandPhoto, command=lambda:youPick("Scissor"))
    lHandButton = Button(root,image= lizardHandPhoto,command=lambda:youPick("Lizard"))
    spockHandButton = Button(root,image= spockHandPhoto,command=lambda:youPick("Spock"))
    
    #Place the buttons on window :
    rHandButton.grid(row=0,column=0)
    pHandButton.grid(row=0,column=1)
    sHandButton.grid(row=0,column=2)
    lHandButton.grid(row=0,column=3)
    spockHandButton.grid(row=0,column=4)
    
    #Add space :
    root.grid_rowconfigure(1, minsize=50) 
    
    #Place result button on window : 
    resultButton.grid(row=2,column=0,columnspan=5)
   
    

def computerPick():
    choice = random.choice(["Rock","Paper","Scissor","Lizard","Spock"])
    return choice

def reset(mychoice):
    global click
    rHandButton.configure(image=rockHandPhoto)
    pHandButton.configure(image=paperHandPhoto)
    sHandButton.configure(image=scissorHandPhoto,command=lambda:youPick("Scissor"))
    lHandButton.configure(image=lizardHandPhoto)
    spockHandButton.configure(image=spockHandPhoto)
    resultButton.configure(image=decisionPhoto)

    #Get back the deleted buttons :
    sHandButton.grid(row=0,column=2)
    lHandButton.grid(row=0,column=3)
    spockHandButton.grid(row=0,column=4)

    #Set click = True :
    click=True

    #Play the sound file :
    start.play()


def youPick(yourChoice):
    global click
    
    compPick = computerPick()
    
    
    if click==True:
        
        if yourChoice == "Rock":
            
            rHandButton.configure(image=rockPhoto)
            
            if compPick == "Rock":
                pHandButton.configure(image=rockPhoto)
                resultButton.configure(image=tiePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Draw.play()
                click = False
            
            elif compPick == "Paper":
                pHandButton.configure(image=paperPhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                resultButton.configure(image=losePhoto)
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()

                click = False
            
            elif compPick == "Scissor":
                pHandButton.configure(image=scissorPhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                resultButton.configure(image=winPhoto)
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False
                
            elif compPick =="Lizard":
                pHandButton.configure(image=lizardPhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                resultButton.configure(image=winPhoto)
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False
                
            else :
                pHandButton.configure(image=spockPhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                resultButton.configure(image=losePhoto)
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False
                
                
        elif yourChoice == "Paper":
            rHandButton.configure(image=paperPhoto)
            
            if compPick == "Rock":
                pHandButton.configure(image=rockPhoto)
                resultButton.configure(image=losePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False
        
            elif compPick == "Paper":
                pHandButton.configure(image=paperPhoto)
                resultButton.configure(image=tiePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Draw.play()
                click = False
            
            elif compPick == "Scissor":
                pHandButton.configure(image=scissorPhoto)
                resultButton.configure(image=losePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False
                
            elif compPick =="Lizard":
                pHandButton.configure(image=lizardPhoto)
                resultButton.configure(image=losePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False
                
            else :
                pHandButton.configure(image=spockPhoto)
                resultButton.configure(image=winPhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False
                
                
                
        elif yourChoice=="Scissor":
            rHandButton.configure(image=scissorPhoto)
            if compPick == "Rock":
                pHandButton.configure(image=rockPhoto)
                resultButton.configure(image=losePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False
            
            elif compPick == "Paper":
                pHandButton.configure(image=paperPhoto)
                resultButton.configure(image=winPhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False
            
            elif compPick=="Scissor":
                pHandButton.configure(image=scissorPhoto)
                resultButton.configure(image=tiePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Draw.play()
                click = False
                
            elif compPick == "Lizard":
                pHandButton.configure(image=lizardPhoto)
                resultButton.configure(image=winPhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False
            
            else:
                pHandButton.configure(image=spockPhoto)
                resultButton.configure(image=losePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False
                
        elif yourChoice=="Lizard":
            rHandButton.configure(image=lizardPhoto)
            if compPick == "Rock":
                pHandButton.configure(image=rockPhoto)
                resultButton.configure(image=losePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

            elif compPick == "Paper":
                pHandButton.configure(image=paperPhoto)
                resultButton.configure(image=winPhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False

            elif compPick=="Scissor":
                pHandButton.configure(image=scissorPhoto)
                resultButton.configure(image=losePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

            elif compPick == "Lizard":
                pHandButton.configure(image=lizardPhoto)
                resultButton.configure(image=tiePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Draw.play()
                click = False

            else:
                pHandButton.configure(image=spockPhoto)
                resultButton.configure(image=winPhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False
                
        elif yourChoice=="Spock":
            rHandButton.configure(image=spockPhoto)
            if compPick == "Rock":
                pHandButton.configure(image=rockPhoto)
                resultButton.configure(image=winPhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False

            elif compPick == "Paper":
                pHandButton.configure(image=paperPhoto)
                resultButton.configure(image=losePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

            elif compPick=="Scissor":
                pHandButton.configure(image=scissorPhoto)
                resultButton.configure(image=winPhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False

            elif compPick == "Lizard":
                
                pHandButton.configure(image=lizardPhoto)
                resultButton.configure(image=losePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

            else:
                pHandButton.configure(image=spockPhoto)
                resultButton.configure(image=tiePhoto)
                sHandButton.configure(image=tagain,command=lambda:reset(yourChoice))
                lHandButton.grid_forget()
                spockHandButton.grid_forget()
                Draw.play()
                click = False
                
                
    else:
        #To reset the game :
        if yourChoice=="Rock" or yourChoice=="Paper" or yourChoice=="Scissor" or yourChoice=="Lizard" or yourChoice=="Spock":
            rHandButton.configure(image=rockHandPhoto)
            pHandButton.configure(image=paperHandPhoto)
            sHandButton.configure(image=scissorHandPhoto)
            lHandButton.configure(image=lizardHandPhoto)
            spockHandButton.configure(image=spockHandPhoto)
            resultButton.configure(image=decisionPhoto)
            
            #Get back the deleted buttons :
            sHandButton.grid(row=0,column=2)
            lHandButton.grid(row=0,column=3)
            spockHandButton.grid(row=0,column=4)
            
            #Set click = True :
            click=True
            
            #Play the sound file :
            start.play()



#Calling the play function :
play()

#Enter the main loop :
root.mainloop()


# In[ ]:




