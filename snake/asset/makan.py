import pygame
from numpy import random as rnd
class makan():
    
    def __init__(self,arena, warna=(220,20,60), nama="Ekor") :
        posisi_x_makan = rnd.random_integers(0,arena.get_jumlah_kolom()-1)
        posisi_y_makan = rnd.random_integers(0,arena.get_jumlah_baris()-1)

        self.nama = nama
        self.posisiAwal = (posisi_x_makan, posisi_y_makan)
        self.warna = warna
        self.surface = arena.get_surface()
        self.lebar = arena.get_jarak_kolom()
        self.tinggi = arena.get_jarak_baris()
        self.arena = arena
        arena.assign(self)
    
    def getPos(self) :
        return self.posisiAwal
    
    def set_pos(self) :
        posisi_x_makan = rnd.random_integers(0,self.arena.get_jumlah_kolom()-1)
        posisi_y_makan = rnd.random_integers(0,self.arena.get_jumlah_baris()-1)
        self.posisiAwal = (posisi_x_makan, posisi_y_makan)
        
    def draw(self) :
        start_x = self.lebar*self.posisiAwal[0]
        start_y = self.tinggi*self.posisiAwal[1]
        pygame.draw.rect(self.surface, self.warna,(start_x,start_y,self.lebar,self.tinggi))
        
    