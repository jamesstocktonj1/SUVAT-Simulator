#path calculate

import math





class Projectile:

    def __init__(self):
        self.initAngle = 0
        self.initVelocity = 0
        
        self.hs = 0
        self.hu = 0
        self.hv = 0
        self.ha = 0

        self.vs = 0
        self.vu = 0
        self.vv = 0
        self.va = -9.81

        self.time = 0

    def setInit(self, angle, velocity):
        self.initAngle = angle
        self.initVelocity = velocity

        self.hu = (math.cos(math.radians(self.initAngle)) * self.initVelocity)
        self.vu = (math.sin(math.radians(self.initAngle)) * self.initVelocity)

    def newTime(self, time):
        self.time = time

        #s = ut + 0.5at**2
        self.hs = (self.hu * self.time)# + (0.5 * self.ha * self.time**2)       #if a = 0

        #s = ut + 0.5at**2
        self.vs = (self.vu * self.time) + (0.5 * self.va * self.time**2)

        self.vv = self.vu + (self.time * self.va)

        return self.hs, self.vs

    def getTotalTime(self):
        totalTime = self.vu / 4.905
        return totalTime

    def getRangeXY(self):
        totalTime = self.getTotalTime()
        maxH = (self.hu * totalTime)
        maxV = (self.vu * totalTime) + (0.5 * self.va * totalTime**2)
        return maxH, maxV
        





"""
class Horizontal:

    def __init__(self):
        self.s = 0
        self.uv = 0
        self.a = 0
        self.t = 0


class Vertical:

    def __init__(self):
        self.s = 0
        self.u = 0
        self.v = 0
        self.a = -9.81
        self.t = 0

    def getFromAngle(self, angle, resultant):
        
"""
