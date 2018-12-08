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
    
    screen = Tk()
    screen.title("Main Visual")

    screenWidth = 1920
    screenHeight = 1080

    canvas = Canvas(screen, width=screenWidth, height=screenHeight)
    canvas.pack()

    multipX = 0
    multipY = 0
    multip = 3
    

    print("Range: " + str(particle.getTotalTime()))

    for t in range(1, int(particle.getTotalTime() * 100) + 1):
        particle.newTime(t / 100)
        canvas.create_line(prevXY[0] * multip, screenHeight- (prevXY[1] * multip), particle.hs * multip, screenHeight - (particle.vs * multip), fill="black")
        prevXY[0] = particle.hs
        prevXY[1] = particle.vs
        print("Time: " + str(particle.time) + "\tX: " + str(particle.hs) + "\tY: " + str(particle.vs))
        screen.update()

    screen.mainloop()

    

