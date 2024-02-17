import pygame
from asset import kotak
    
class ular() :
    badan = []
    belok = {}
    
    def __init__(self, arena, start, arahX=1, arahY=0, warna=(0,0,0)) :
        self.arena = arena
        self.arahX = arahX
        self.arahY = arahY
        self.start = start
        self.warna = warna
        self.kepala = kotak(arena,start, arahX, arahY, warna, nama="Kepala")
        self.badan.append(self.kepala)
        
    def getPos(self) :
        return self.kepala.getPos()
    
    def tambahKotak (self) :
        ekor = self.badan[-1]
        arahX_Ekor = ekor.get_arah_x()
        arahY_Ekor = ekor.get_arah_y()
        pos_ekor = ekor.getPos()
        pos_ekor_x = pos_ekor[0]
        pos_ekor_y = pos_ekor[1]
        
        if arahX_Ekor == 1 and arahY_Ekor == 0:
            # lagi kekanan
            ekor_baru = kotak(self.arena,(pos_ekor_x-1,pos_ekor_y),arahX_Ekor,arahY_Ekor)
            self.badan.append(ekor_baru)
            
        elif arahX_Ekor == -1 and arahY_Ekor == 0:
            # lagi kekiri
            ekor_baru = kotak(self.arena,(pos_ekor_x+1,pos_ekor_y),arahX_Ekor,arahY_Ekor)
            self.badan.append(ekor_baru)

        elif arahX_Ekor == 0 and arahY_Ekor == 1:
            # lagi kebawah
            ekor_baru = kotak(self.arena,(pos_ekor_x,pos_ekor_y-1),arahX_Ekor,arahY_Ekor)
            self.badan.append(ekor_baru)

        elif arahX_Ekor == 0 and arahY_Ekor == -1:
            # lagi keatas
            ekor_baru = kotak(self.arena,(pos_ekor_x,pos_ekor_y+1),arahX_Ekor,arahY_Ekor)
            self.badan.append(ekor_baru)
        
    def reset(self) :
        self.kepala = kotak(self.arena, self.start, arahX=1, warna=self.warna, nama="kepala")
        self.badan =[]
        self.badan.append(self.kepala)
        self.belok ={}
        self.arahX = 1
        self.arahY = 0
        
    def move(self) :
        print(self.belok)
        #user input
        keys = pygame.key.get_pressed()
        
        for key in keys :
            if keys[pygame.K_RIGHT] and self.arahX != -1 :
                self.arahX = 1
                self.arahY = 0
                self.belok[self.kepala.posisiAwal] = (self.arahX, self.arahY)
            if keys[pygame.K_LEFT] and self.arahX != 1 :
                self.arahX = -1
                self.arahY = 0
                self.belok[self.kepala.posisiAwal] = (self.arahX, self.arahY)
            if keys[pygame.K_UP] and self.arahY != 1 :
                self.arahY = -1
                self.arahX = 0
                self.belok[self.kepala.posisiAwal] = (self.arahX, self.arahY)
            if keys[pygame.K_DOWN] and self.arahY != -1:
                self.arahY = 1
                self.arahX = 0   
                self.belok[self.kepala.posisiAwal] = (self.arahX, self.arahY)
        
        for data in self.belok:
            print(f"pos :{data} arah :{self.belok[data]}\n")
            
        for index,kotak in enumerate(self.badan):
            pos_kotak = kotak.getPos()
            if pos_kotak in self.belok:
                arah = self.belok[pos_kotak]
                arah_x = arah[0]
                arah_y = arah[1]
                kotak.move(arah_x,arah_y)
                if index == len(self.badan)-1:
                    self.belok.pop(pos_kotak)
            else:
                kotak.move(kotak.get_arah_x(),kotak.get_arah_y())
            
    
    def is_collide(self):
        pos_kepala = self.kepala.getPos()
        is_collide = False;
        for index,kotak in enumerate(self.badan):
            if index > 0 and pos_kepala == kotak.getPos():
                is_collide = True
                break
        
        return is_collide
    
    def draw(self) :
        for anggotaBadan in self.badan :
            anggotaBadan.draw()
            
   
        
            