import numpy as np
from asset import Ular

class Enemy(Ular) :
    
    def __init__(self, arena, start, arahX=0, arahY=1, warna=(220,20,60), user="enemy",):
        super().__init__(arena, start, arahX, arahY, warna,user)
        self.time = 0
        self.arahX = arahX
        self.arahY = arahY
        
    def randomDirection(self) :
        if self.time % 5 == 0:
            self.arah = np.random.choice([1, 2, 3, 4])  
        self.time += 1
    
    def getDirection(self) :
        self.randomDirection()
        
        if self.arah == 1 and self.arahY != 1:  # Atas
            self.arahY = -1
            self.arahX = 0
            self.belok[self.kepala.posisiAwal] = (self.arahX, self.arahY)
        elif self.arah == 2 and self.arahX != -1:  # Kanan
            self.arahX = 1
            self.arahY = 0
            self.belok[self.kepala.posisiAwal] = (self.arahX, self.arahY)
        elif self.arah == 3 and self.arahY != -1:  # Bawah
            self.arahX = 0
            self.arahY = 1
            self.belok[self.kepala.posisiAwal] = (self.arahX, self.arahY)
        elif self.arah == 4 and self.arahX != 1:  # Kiri
            self.arahX = -1
            self.arahY = 0
            self.belok[self.kepala.posisiAwal] = (self.arahX, self.arahY)
                
    def reset(self) :
        self.badan =[]
        self.belok ={}
        self.arahX = 1
        self.arahY = 0
            
   
        
            