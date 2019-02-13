
class MilClock:
    def __init__(self, h, m):
        self.hours = h
        self.min = m

    def __str__(self):
        if 10 > self.hours >= 0:
            if 10 > self.min >= 0:
                s = "0" + str(self.hours) + ":" + "0" + str(self.min)
            else:
               s = "0" + str(self.hours) + ":" + str(self.min)
        else:
            if 10 > self.min >= 0:
                s = str(self.hours) + ":" + "0" + str(self.min)
            else:
               s = str(self.hours) + ":" + str(self.min)
               
        return s

    def addOne(self):
        if 58 >= self.min >= 0:
            self.min += 1
            
        else: # min = 59
            if 23 > self.hours >= 0:
                self.min = 0
                self.hours += 1
            else:
                self.min = 0
                self.hours = 0
    
