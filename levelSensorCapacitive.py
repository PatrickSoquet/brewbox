class levelSensorCapacitive:
    id
    level = 0 #range : (0-0xFFFF)
    def __init__(self,idd):
        self.id = idd
class sensorC(levelSensorCapacitive):
    def read(self):
        dataIn = '$!RY0151\r\n'
        #call of the serial method to write and read!!
        dataOut ='*CFV0100AAAAB6'
        self.level = int(dataOut[8:10], 16)*256+int(dataOut[10:12], 16)
        return self.level
##ASCII:  $!RY0151 
##Hex: 24 21 52 59 30 31 35 31 0D 0A
##is $! is header, RY is command, 01 is sensor id, 51 is end
##
##device to sensor From Reply:
##ASCII: *CFV0100XXXXB6 
##Hex: 2A 43 46 56 30 31 30 30 XX XX XX XX 42 36 0D 0A
##* is header, CFV is reply command, 01 is sensor id, OO is padding, XX XX XX XX equals 0%~100% Level value
##

##scale of 65536 / 100 => x655!

ss = sensorC("test")
print(ss.read())

