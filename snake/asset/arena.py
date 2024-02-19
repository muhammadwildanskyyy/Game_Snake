import pygame

class arena () :
    
    def __init__(self, arenaLebar, arenaTinggi, jumlahBaris, jumlahColom):
        pygame.init()
        self.arenaLebar = arenaLebar
        self.arenaTinggi = arenaTinggi
        self.jumlahBaris = jumlahBaris
        self.jumlahColom = jumlahColom
        self.jarakBaris = self.arenaTinggi // self.jumlahBaris
        self.jarakColom = self.arenaLebar // self.jumlahColom
        
        self.objects = []
        
        self.surface = pygame.display.set_mode((self.arenaLebar,self.arenaTinggi))
        
        self.clock = pygame.time.Clock()

    def assign(self,object):
        self.objects.append(object)
        
    def getSurface(self) :
        return self.surface
    
    def get_surface(self):
        return self.surface

    def get_jarak_baris(self):
        return self.jarakBaris
    
    def get_jarak_kolom(self):
        return self.jarakColom

    def get_jumlah_kolom(self):
        return self.jumlahColom

    def get_jumlah_baris(self):
        return self.jumlahBaris

    def drawGrid(self) :
        # Gambar kolom
        for kolomke in range(self.jumlahColom):
            x = self.jarakColom * kolomke
            pygame.draw.line(self.surface, (128, 128, 128), (x, 0), (x, self.arenaTinggi))
            
        # Gambar baris
        for bariske in range(self.jumlahBaris):
            y = self.jarakBaris * bariske
            pygame.draw.line(self.surface, (128, 128, 128), (0, y), (self.arenaLebar, y))
    
    def copyRight(self) :
        font = pygame.font.Font('freesansbold.ttf', 20)
        welcome_font = font.render('Archive by Ardan', True, (255, 255, 255))
        welcome_rect = welcome_font.get_rect()
        welcome_rect.topleft = (self.arenaLebar -600 , self.arenaTinggi-60)
        self.surface.blit(welcome_font, welcome_rect)
        
    def mainMenu(self) :
        font = pygame.font.Font('freesansbold.ttf', 100)
        welcome_font = font.render('WELCOME TO', True, (255, 255, 255))
        welcome_rect = welcome_font.get_rect()
        welcome_rect.topleft = (self.arenaLebar - 850 , self.arenaTinggi - 700)
        self.surface.blit(welcome_font, welcome_rect)
        
        font = pygame.font.Font('freesansbold.ttf', 100)
        welcome_font = font.render('SNAKE', True, (255, 255, 255))
        welcome_rect = welcome_font.get_rect()
        welcome_rect.topleft = (self.arenaLebar - 700, self.arenaTinggi - 600)
        self.surface.blit(welcome_font, welcome_rect)
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        start_font = font.render('Press Space To Start The Game', True, (255, 255, 255))
        start_rect = start_font.get_rect()
        start_rect.topleft = (self.arenaLebar - 680, self.arenaTinggi - 400)
        self.surface.blit(start_font, start_rect)
         
    def getScore(self,score,hightScore, level, hightLevel):
        font = pygame.font.Font('freesansbold.ttf', 18)
        score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (self.arenaLebar - 300, 20)
        self.surface.blit(score_font, score_rect)
        
        font = pygame.font.Font('freesansbold.ttf', 18)
        hightScore_font = font.render('Hight Score: %s' % (hightScore), True, (255, 255, 255))
        hightScore_rect = hightScore_font.get_rect()
        hightScore_rect.topleft = (self.arenaLebar - 200, 20)
        self.surface.blit(hightScore_font, hightScore_rect)
        
        font = pygame.font.Font('freesansbold.ttf', 18)
        level_font = font.render('Level: %s' % (level), True, (255, 255, 255))
        level_rect = level_font.get_rect()
        level_rect.topleft = (self.arenaLebar - 300, 60)
        self.surface.blit(level_font, level_rect)
        
        
        font = pygame.font.Font('freesansbold.ttf', 18)
        hightLevel_font = font.render('Hight Level: %s' % (hightLevel), True, (255, 255, 255))
        hightLevel_rect = hightLevel_font.get_rect()
        hightLevel_rect.topleft = (self.arenaLebar - 200, 60)
        self.surface.blit(hightLevel_font, hightLevel_rect)
          
    def gameOver(self,score) :
        font = pygame.font.Font('freesansbold.ttf', 100)
        gameOver_font = font.render('GAME OVER', True, (255, 255, 255))
        gameOver_rect = gameOver_font.get_rect()
        gameOver_rect.topleft = (self.arenaLebar - 800, self.arenaTinggi - 700)
        self.surface.blit(gameOver_font, gameOver_rect)
        
        font = pygame.font.Font('freesansbold.ttf', 50)
        score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (self.arenaLebar - 600, self.arenaTinggi - 500)
        self.surface.blit(score_font, score_rect)
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        retrun_font = font.render('Press Return To Continue The Game', True, (255, 255, 255))
        retrun_rect = retrun_font.get_rect()
        retrun_rect.topleft = (self.arenaLebar - 680, self.arenaTinggi - 400)
        self.surface.blit(retrun_font, retrun_rect)
        
    def render_mainMenu(self,fps) :
        self.surface.fill((37,56,60))
        self.drawGrid()
        self.mainMenu()
        self.copyRight()
        pygame.display.update()
        self.clock.tick(fps)
        
    def render_game(self,fps,score,hightScore,level,hightLevel):
        self.surface.fill((37,56,60))
        for obj in self.objects:
            obj.draw()
        self.drawGrid()
        self.getScore(score, hightScore, level, hightLevel)
        self.copyRight()

        pygame.display.update()
        self.clock.tick(fps)
         
    def render_gameover(self,fps,score) :
        self.surface.fill((37,56,60))
        
        
        self.drawGrid()
        self.gameOver(score)
        self.copyRight()
        pygame.display.update()
        self.clock.tick(fps)
        
    def reset_member(self):
        self.objects = []