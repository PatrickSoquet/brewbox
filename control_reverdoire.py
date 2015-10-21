import time
import math
import random
import levelSensorCapacitive

#id list
#   resistance:
#           resistanceReverdoir
#   ev:
#           evEntreeReverdoir
#           evSortieReverdoir
#   pompe:
#           pompeReverdoir

class alarm:
    stateON = False
    def on(self):
        #TODO: lancer l'alarme!!
        self.stateON = True
        print("ALARM ON!!!!!!!!!!")
    def off(self):
        #TODO: arreter l'alarme!!
        if self.stateON:
            print("ALARM off")
        self.stateON = False
        
        
class actuator:
    id
    stateON = False
    delayed_timer = 0
    delayed = False
    def __init__(self,id):
        self.id = id
        return
    def isOn(self):
        return self.stateON
    def isOff(self):
        return not self.stateON
    def on(self):
        return self.operate(True)
    def off(self):
        return self.operate(False)
    def on_delayed(self,delay):
        return self.operate_delayed(True,delay)
    def off_delayed(self,delay):
        return self.operate_delayed(False,delay)
    
class electroVanne(actuator):
    #stateON == True:  open
    #stateON == False: close
    def operate(self,way):
        if way == self.stateON:
            #TODO later: verification of the real state of the EV
            return "NO_STATE_CHANGE"
        elif way == True:
            #open the EV!!!!
            #TODO
            print('**  '+ self.id + ' opened')
        elif way == False:
            #close the EV!!!!
            #TODO
            print('**  '+ self.id + ' closed')
        self.stateON = not self.stateON
        return "OK"
    
    def operate_delayed(self,way,delay):
        if way == self.stateON:
            #TODO later: verification of the real state of the EV
            delayed = False
            return "NO_STATE_CHANGE"
        if self.delayed:
            self.delayed_timer = self.delayed_timer-1
            if self.delayed_timer == 0:
                self.delayed = False
                if way == True:
                    #open the EV!!!!
                    #TODO
                    print('**  '+ self.id + ' opened')
                elif way == False:
                    #close the EV!!!!
                    #TODO
                    print('**  '+ self.id + ' closed')
                self.stateON = not self.stateON
            else:
                print('**  '+ self.id + ' delayed ' + str(self.delayed_timer))
        else:
            self.delayed = True
            self.delayed_timer = delay
            print('**  '+ self.id + ' delayed ' + str(self.delayed_timer))
        return "OK"
  
class resistante(actuator):
    def operate(self,way):
        if way == self.stateON:
            #TODO later: verification of the real state of the actuator
            return "NO_STATE_CHANGE"
        elif way == True:
            #allume la résistance!!!
            #TODO
            print('**  '+ self.id + ' on')
        elif way == False:
            #eteint la résistance!!!
            #TODO
            print('**  '+ self.id + ' off')
        self.stateON = not self.stateON
        return "OK"

class pompe(actuator):
    def operate(self,way):
        if way == self.stateON:
            #TODO later: verification of the real state of the actuator
            return "NO_STATE_CHANGE"
        elif way == True:
            #allume la pompe!!!
            #TODO
            print('**  '+ self.id + ' on')
        elif way == False:
            #eteint la pompe!!!
            #TODO
            print('**  '+ self.id + ' off')
        self.stateON = not self.stateON
        return "OK"
    def operate_delayed(self,way,delay):
        if way == self.stateON:
            delayed = False
            return "NO_STATE_CHANGE"
        if self.delayed:
            self.delayed_timer = self.delayed_timer-1
            if self.delayed_timer == 0:
                self.delayed = False
                if way == True:
                    #allume la pompe!!!
                    #TODO
                    print('**  '+ self.id + ' on')
                elif way == False:
                    #éteint la pompe!!!
                    #TODO
                    print('**  '+ self.id + ' off')
                self.stateON = not self.stateON
            else:
                print('**  '+ self.id + ' delayed ' + str(self.delayed_timer))

        else:
            self.delayed = True
            self.delayed_timer = delay
            print('**  '+ self.id + ' delayed ' + str(self.delayed_timer))
        return "OK"

#ER_1 <= LB_alert < ER_2 <= LB < ER_3 <= LH < ER_4 <= LH_alert < ER_5
# the aim is the state 3 between LB and LH
LB_alert = 20*655
LB = 60*655
LH = 80*655
LH_alert = 90*655

al = alarm()
evER = electroVanne("evEntreeReverdoir")
evSR = electroVanne("evSortieReverdoir")
pomp = pompe("pompeReverdoir")
resist = resistante("resistanceReverdoir")
sensor = levelSensorCapacitive.sensorC("SensorReverdoirSerialCapacitif")

def calculateLevel(vol):
    if vol < LB_alert:
        return 1
    if vol < LB:
        return 2
    if vol < LH:
        return 3
    if vol < LH_alert:
        return 4
    return 5

def initReverdoir(level):
    if level == 1:
        al.on()
        evSR.off()
        evER.on()
        resist.off()
        pomp.off()
    elif level == 2:
        al.off()
        evSR.off()
        evER.on()
        resist.on()
        pomp.off()
    elif level == 3:
        al.off()
        evSR.on()
        evER.on()
        resist.on()
        pomp.on()
    elif level == 4:
        al.off()
        evSR.on()
        evER.off()
        resist.on()
        pomp.on()
    elif level == 5:
        al.on()
        evSR.on()
        evER.off()
        resist.on()
        pomp.on()


def regulateReverdoir(level):
    if level == 1:
        al.on()
        evSR.off()
        evER.on()
        resist.off()
        pomp.off()
    elif level == 2:
        al.off()
        evSR.off_delayed(2)
        evER.on()
        resist.on()
        pomp.off_delayed(2)
    elif level == 3:
        al.off()
        evSR.on_delayed(2)
        evER.on_delayed(3)
        resist.on()
        pomp.on_delayed(2)
    elif level == 4:
        al.off()
        evSR.on()
        evER.off_delayed(2)
        resist.on()
        pomp.on()
    elif level == 5:
        al.on()
        evSR.on()
        evER.off()
        resist.on()
        pomp.on()


def volReverdoirSimul(vol):
#for simulation...
    a = evER.isOn() - evSR.isOn()
    return min(65536,max(0,vol+a*3000+500))
def volReverdoir(sens):
    return sens.read()


volum = 0
level = 0
volum = math.floor(random.random()*65536)
level = calculateLevel(volum)
print("vol = " + str(volum)) 
initReverdoir(level)
timer = 0
while True:
    #volum = volReverdoir(sensor)
    volum = volReverdoirSimul(volum)
    level = calculateLevel(volum)
    print("timer " + str(timer) + "   vol = " + str(volum))  # + "    level = "+ str(level) + "    level_prec = "+ str(level_prev))
    regulateReverdoir(level)
    timer=timer+1
    time.sleep(0.5)


    
