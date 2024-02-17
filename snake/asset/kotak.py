import pygame 

class kotak():
    
    
    def __init__(self,arena, posisiAwal, arahX=0, arahY=0, warna=(0,0,0), nama="Ekor") :
        self.nama = nama
        self.posisiAwal = posisiAwal
        self.arahX = arahX
        self.arahY = arahY
        self.warna = warna
        self.surface = arena.get_surface()
        self.lebar = arena.get_jarak_kolom()
        self.tinggi = arena.get_jarak_baris()
        self.arena = arena
        arena.assign(self)
        
    def getPos(self) :
        return self.posisiAwal

    def get_arah_x(self):
        return self.arahX
    
    def get_arah_y(self):
        return self.arahY
        
    def move(self, arahX, arahY) :
        self.arahX = arahX
        self.arahY = arahY
        self.posisiAwal = (self.posisiAwal[0] + self.arahX, self.posisiAwal[1] + arahY)
        
        
        if self.posisiAwal[0] == self.arena.get_jumlah_kolom():
            self.posisiAwal = (0,self.posisiAwal[1])
        elif self.posisiAwal[0] < 0:
            self.posisiAwal = (self.arena.get_jumlah_kolom()-1,self.posisiAwal[1])

        if self.posisiAwal[1] == self.arena.get_jumlah_baris():
            self.posisiAwal = (self.posisiAwal[0],0)
        elif self.posisiAwal[1] < 0:
            self.posisiAwal = (self.posisiAwal[0],self.arena.get_jumlah_baris()-1)
        
    def draw(self) :
        start_x = self.lebar*self.posisiAwal[0]
        start_y = self.tinggi*self.posisiAwal[1]
        pygame.draw.rect(self.surface, self.warna,(start_x,start_y,self.lebar,self.tinggi))
        
    def __repr__(self):
        return f"{self.nama}"
        

