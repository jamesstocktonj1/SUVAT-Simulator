#SUVAT Simulator Main
#James Stockton


from tkinter import *
from SUVAT import *
import time

part = Projectile()













#get initial velocity and angle
initScreen = Tk()
initScreen.title("Initial Position")

Label(initScreen, text="Initial Angle").grid(column=0, row=0)
Label(initScreen, text="\t\t").grid(column=1, row=0)
angleInput = Scale(initScreen, from_=0, to=89, orient=HORIZONTAL)
angleInput.grid(column = 2, row = 0)

Label(initScreen, text="Initial Velocity").grid(column=0, row=1)
Label(initScreen, text="\t\t").grid(column=1, row=1)
velocityInput = Scale(initScreen, from_=0, to=100, orient=HORIZONTAL)
velocityInput.grid(column=2, row=1)

def startParticleCallback():
    part.setInit(angleInput.get(), velocityInput.get())
    initScreen.quit()
    initScreen.destroy()

    mainCanvas(part)


Label(initScreen, text="\t").grid(column=0, row=2)
Label(initScreen, text="\t\t").grid(column=1, row=2)
goButton = Button(initScreen, text="Start Simulation", command=startParticleCallback)
goButton.grid(column=2, row=2)





def mainCanvas(particle):
    prevXY = [0, 0]
    putCoords = True
    
    screen = Tk()
    screen.title("Main Visual")

    screenWidth = 1280
    screenHeight = 720

    

    if putCoords:
        headerLabel = Label(screen, text="MAX S: 0.0 \t\tT: 0.0 \tHS: 0.0 \tVS: 0.0")
        headerLabel.grid(column=0, row=0)
        
        timeLabel = Label(screen, text="T: ")
        #timeLabel.grid(column=1, row=0)
        
        HSLabel = Label(screen, text="HS: ")
        #HSLabel.grid(column=2, row=0)

        VSLabel = Label(screen, text="VS: ")
        #VSLabel.grid(column=3, row=0)
    

    canvas = Canvas(screen, width=screenWidth, height=screenHeight)
    #canvas.pack()
    #canvas.grid(column=0, row=1)
    canvas.grid()

    multipX = 0
    multipY = 0
    multip = 3

    maxS = particle.getTotalTime()

    print("Range: " + str(maxS))

    for t in range(1, int(maxS * 100) + 1):
        particle.newTime(t / 100)
        canvas.create_line(prevXY[0] * multip, screenHeight- (prevXY[1] * multip), particle.hs * multip, screenHeight - (particle.vs * multip), fill="black")
        prevXY[0] = particle.hs
        prevXY[1] = particle.vs

        if putCoords:
            print("Time: " + str(particle.time) + "\tX: " + str(particle.hs) + "\tY: " + str(particle.vs))

            headerLabel.config(text="MAX S: " + str(maxS) + "\t\tT: " + str(int(t)) + "\tHS: " + str(int(particle.hs)) + "\tVS: " + str(int(particle.vs)))

            #timeLabel.config(text="T: "+str(int(t)))
            #HSLabel.config(text="HS: "+str(int(particle.hs)))
            #VSLabel.config(text="VS: "+str(int(particle.vs)))
            
        screen.update()
        time.sleep(0.01)

    screen.mainloop()

    

