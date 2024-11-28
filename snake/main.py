import pygame 
from asset import arena, Ular, Makan, Enemy

#window
window = arena(800,800,50,50)

#object
ular = Ular(window,(25,25),user="ular")
listEnemy = []
makanan = Makan(window)

#indikator
memakan = 1
level = 1
speed = 5
score = 1
hightScore = 0
hightLevel = 0
endSkore = 0
createEnemy = True
ularCrash = None

#main Loop
mainProgram = True
mainMenu = True
game = False
gameOver = False

while mainProgram:
    # window name
    pygame.display.set_caption('Game Snake By Skyyy')
            
    # Main menu    
    while mainMenu :
        print("Main Menu")    
        # user input
        # exit
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                mainProgram = False
                mainMenu = False
                print("exit")
                
        # playgame
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] :
            game = True
            mainMenu = False
            
        # update and render
        window.render_mainMenu(30)
        
    # Main Game    
    while game :
        # user input
        # exit
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                mainProgram = False
                game = False
                print("exit")
        
        if score%2 == 0 and createEnemy :
            newEnemy = Enemy(window,(30,30),user="enemy")
            print("create enemy")
            for i in range(5):
                newEnemy.tambahKotak()
            listEnemy.append(newEnemy)
            createEnemy = False
        elif score % 2 != 0: createEnemy = True if len(listEnemy) < 3 else False


        # update object
        ular.move()  
        for enemy in listEnemy:
            enemy.move()
            
            # game over
            if ular.getPos() in enemy.getPosBadan():
                ularCrash = enemy
                print("Snake Crash")   
            
        # game over
        if ular.is_collide() or ularCrash:
            # reset snake
            window.reset_member()
            ular.reset()
            for enemy in listEnemy :
                enemy.reset()
            
            # food
            makanan = Makan(window)
            #indikator
            memakan = 1
            speed = 5
            endSkore = score
            if score > hightScore : hightScore = score
            if level > hightLevel : hightLevel = level 
            score = 1
            level = 1
            gameOver = True
            game = False
            
           
        # eat
        if ular.getPos() == makanan.getPos() :
            ular.tambahKotak()
            for enemy in listEnemy :
                enemy.tambahKotak()
                
            
            makanan.set_pos()
            memakan += 1
            score += 1
            # speed
            if memakan % 5 == 0 :
                speed +=2
                level +=1
        
        # render ke display
        window.render_game(speed,score,hightScore,level,hightLevel)    

    # game over
    while gameOver :
        print("GAME OVER")
        # user input
        #exit
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                mainProgram = False
                gameOver = False
                print("exit")
        
        # play game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] :
            game = True
            gameOver = False
            ularCrash = None
            listEnemy.clear()  
            createEnemy = True 
            
        # update and render˜
        window.render_gameover(30,endSkore)
    
       
pygame.quit()
    





